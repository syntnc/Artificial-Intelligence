from copy import deepcopy
from functools import total_ordering

DIRECTIONS = ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE']
MOVES = {'NE':[-1, 1], 'N':[-1, 0], 'NW':[-1, -1], 'W':[0, -1], 'E':[0, 1], 'SE':[1, 1], 'S':[1, 0], 'SW':[1, -1]}
M, N = 0, 0
GRID = None
TIME = 0

@total_ordering
class Node(object):
    def __init__(self, cost, time, coordinate, path):
        self.cost = cost
        self.time = time
        self.coordinate = coordinate
        self.path = path
    
    def __eq__(self, other):
        return (self.cost, self.time) == (other.cost, other.time)

    def __lt__(self, other):
        return (self.cost, self.time) < (other.cost, other.time)

def move_next(node, current_path):
    '''GETS NEXT VALID MOVES IN ALL EIGHT DIRECTIONS FROM CURRENT COORDINATE'''
    from math import sqrt
    global TIME
    next_moves = []
    for direction in DIRECTIONS:
        step_cost = 1 if direction in {'N', 'E', 'W', 'S'} else sqrt(2)
        next_x, next_y = node.coordinate['x'] + MOVES[direction][0], node.coordinate['y'] + MOVES[direction][1]
        if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
            continue
        if GRID[next_x][next_y] == 0 or GRID[next_x][next_y] == 1:
            GRID[next_x][next_y] = 2 - GRID[next_x][next_y]
            next_moves.append(Node(node.cost + step_cost, TIME, dict(x=next_x, y=next_y), current_path))
        TIME += 1
    return next_moves

def is_goal(coordinate):
    '''CHECKS IF GEM IS PRESENT AT THE CURRENT COORDINATE'''
    return GRID[coordinate['x']][coordinate['y']] == 1

def search(source):
    '''BREADTH-FIRST SEARCH FROM SOURCE TO GOAL'''
    from queue import PriorityQueue
    queue = PriorityQueue()
    queue.put(Node(0, TIME, source, []))
    path = None
    while queue:
        node = queue.get()
        current_path = deepcopy(node.path)
        current_path.append(node.coordinate)
        if is_goal(node.coordinate):
            if path is None:
                path = current_path
                break
        for node in move_next(node, current_path):
            queue.put(node)
    return path

def main():
    '''MAIN FUNCTION'''
    global M, N, GRID
    t = int(input())
    for _ in range(t):
        M, N = map(int, input().strip().split())
        GRID = [list(map(int, input().strip().split())) for __ in range(M)]
        source_x, source_y = map(int, input().strip().split())
        source = dict(x=source_x, y=source_y)
        path = search(source)
        if path is not None:
            for node in path:
                print(node['x'], node['y'], end=' ')
            print()
        else:
            print(-1)

if __name__ == '__main__':
    main()
