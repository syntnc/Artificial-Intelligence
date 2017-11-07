from copy import deepcopy
from functools import total_ordering

DIRECTIONS = ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE']
MOVES = {'NE':[-1, 1, 7], 'N':[-1, 0, 6], 'NW':[-1, -1, 5], 'W':[0, -1, 4], 'E':[0, 1, 0], 'SE':[1, 1, 1], 'S':[1, 0, 2], 'SW':[1, -1, 3]}
M, N = 0, 0
GRID = None
TIME = 0

@total_ordering
class Node(object):
    def __init__(self, cost, time, coordinate, parent, face):
        self.cost = cost
        self.time = time
        self.coordinate = coordinate
        self.parent = parent
        self.face = face

    def __hash__(self):
        return hash((self.coordinate['x'], self.coordinate['y'], self.face))

    def __eq__(self, other):
        return (self.cost, self.time) == (other.cost, other.time)

    def __lt__(self, other):
        return (self.cost, self.time) < (other.cost, other.time)

def move_next(node):
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
            TIME += 1
            turns = abs(node.face - MOVES[direction][2])
            turn_cost = min(turns, 8 - turns) * 5
            next_moves.append(Node(node.cost + step_cost + turn_cost, node.time + TIME, dict(x=next_x, y=next_y), node, MOVES[direction][2]))
    return next_moves

def is_goal(coordinate):
    '''CHECKS IF GEM IS PRESENT AT THE CURRENT COORDINATE'''
    return GRID[coordinate['x']][coordinate['y']] == 1

def search(source):
    '''DIJKSTRA SEARCH FROM SOURCE TO GOAL'''
    from queue import PriorityQueue
    queue = PriorityQueue()
    starting_node = Node(0, TIME, source, None, 0)
    queue.put(starting_node)
    path, visited = None, {}
    visited[starting_node] = (0, 0)
    while not queue.empty():
        node = queue.get()
        while node in visited and visited[node] != (node.cost, node.time):
            continue
        if is_goal(node.coordinate):
            if path is None:
                path = []
                while node is not None:
                    path += [node.coordinate]
                    node = node.parent
                break
        for next_node in move_next(node):
            if next_node in visited and (next_node.cost, next_node.time) >= visited[node]:
                continue
            visited[next_node] = (next_node.cost, next_node.time)
            queue.put(next_node)
    return path

def main():
    '''MAIN FUNCTION'''
    global M, N, GRID, TIME
    t = int(input())
    for _ in range(t):
        TIME = 0
        M, N = map(int, input().strip().split())
        GRID = [list(map(int, input().strip().split())) for __ in range(M)]
        source_x, source_y = map(int, input().strip().split())
        source = dict(x=source_x, y=source_y)
        path = search(source)
        if path is not None:
            path = path[::-1]
            for node in path:
                print(node['x'], node['y'], end=' ')
            print()
        else:
            print(-1)

if __name__ == '__main__':
    main()
