DIRECTIONS = ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE']
MOVES = {'NE':[-1, 1], 'N':[-1, 0], 'NW':[-1, -1], 'W':[0, -1], 'E':[0, 1], 'SE':[1, 1], 'S':[1, 0], 'SW':[1, -1]}
M, N = 0, 0
GRID = None
STACK = None

class Node(object):
    def __init__(self, cost, coordinate):
        self.cost = cost
        self.coordinate = coordinate
        
def move_next(node):
    '''GETS NEXT VALID MOVES IN ALL EIGHT DIRECTIONS FROM CURRENT COORDINATE'''
    from math import sqrt
    next_moves = []
    for direction in DIRECTIONS:
        step_cost = 1 if direction in {'N', 'E', 'W', 'S'} else sqrt(2)
        next_x, next_y = node.coordinate['x'] + MOVES[direction][0], node.coordinate['y'] + MOVES[direction][1]
        if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
            continue
        if GRID[next_x][next_y] != -1:
            next_moves.append(Node(step_cost, dict(x=next_x, y=next_y)))
    return next_moves

def is_goal(coordinate):
    '''CHECKS IF GEM IS PRESENT AT THE CURRENT COORDINATE'''
    return GRID[coordinate['x']][coordinate['y']] == 1

def dls(node, depth):
    '''DEPTH-LIMITED SEARCH FROM SOURCE TO GOAL'''
    global STACK
    if depth < 0:
        return False
    if is_goal(node.coordinate):
        STACK += [node.coordinate]
        return True
    for next_node in move_next(node):
        if dls(next_node, depth - next_node.cost):
            STACK += [node.coordinate]
            return True
    return False

def iterative_deepening(source):
    '''ITERATIVE DEEPENING SEARCH'''
    for depth in range(100):
        if dls(source, depth):
            return True
    return False

def main():
    '''MAIN FUNCTION'''
    global M, N, GRID, STACK
    t = int(input())
    for _ in range(t):
        STACK = []
        M, N = map(int, input().strip().split())
        GRID = [list(map(int, input().strip().split())) for __ in range(M)]
        source_x, source_y = map(int, input().strip().split())
        source = Node(0, dict(x=source_x, y=source_y))
        if iterative_deepening(source):
            path = STACK[::-1]
            for node in path:
                print(node['x'], node['y'], end=' ')
            print()
        else:
            print(-1)

if __name__ == '__main__':
    main()