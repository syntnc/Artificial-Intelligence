from copy import deepcopy
from functools import total_ordering
from math import sqrt
from queue import PriorityQueue

INFINITY = 10 ** 9
DIRECTIONS = ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE']
MOVES = {'NE':[-1, 1], 'N':[-1, 0], 'NW':[-1, -1], 'W':[0, -1], 'E':[0, 1], 'SE':[1, 1], 'S':[1, 0], 'SW':[1, -1]}
M, N = 0, 0
GRID = None
TIME = 0

@total_ordering
class Node(object):
    """State class"""
    def __init__(self, cost, coordinate, path, parent):
        self.cost = cost
        self.coordinate = coordinate
        self.path = path
        self.parent = parent

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

def move_next(node, current_path):
    """Gets next valid moves in all eight directions from current coordinate

    :param node: Current state object
    :param current_path: List of coordinates already visited in the current path
    :returns: List of valid moves in all directions from current state

    """
    global TIME
    next_moves = []
    for direction in DIRECTIONS:
        step_cost = 1 if direction in {'N', 'E', 'W', 'S'} else sqrt(2)
        next_x, next_y = (node.coordinate[0] + MOVES[direction][0]) % M, (node.coordinate[1] + MOVES[direction][1]) % N
        next_x = M - 1 if next_x < 0 else next_x
        next_y = N - 1 if next_y < 0 else next_y
        if GRID[next_x][next_y] == 0 or GRID[next_x][next_y] == 1:
            TIME += 1
            next_moves.append(Node((node.cost[0] + step_cost, node.cost[1] + TIME), (next_x, next_y), current_path, node))
    return next_moves

def is_goal(coordinate):
    """Checks if gem is present at the current coordinate

    :param coordinate: Tuple of x and y coordinates
    :returns: Boolean whther the gem is present at the given coordinate

    """
    return GRID[coordinate[0]][coordinate[1]] == 1

def search(source):
    """Search from source to goal

    :param source: Tuple of x and y coordinates of the initial position
    :returns: Path traversed from source to goal position

    """
    queue, visited = PriorityQueue(), {}
    queue.put(Node((0, TIME), source, [], None))
    distance = {}
    distance[source] = (0, 0)
    path = None
    while not queue.empty():
        node = queue.get()

        if node.coordinate in visited:
            continue

        current_path = deepcopy(node.path)
        current_path.append(node.coordinate)
        visited[node.coordinate] = True

        if is_goal(node.coordinate):
            if path is None:
                path = ''
                while node is not None:
                    path = str(node.coordinate[0]) + ' ' + str(node.coordinate[1]) + ' ' + path
                    node = node.parent
            break
        
        for next_node in move_next(node, current_path):
            if next_node.cost < distance.setdefault(next_node.coordinate, (INFINITY, INFINITY)):    
                distance[next_node.coordinate] = next_node.cost
                queue.put(next_node)
    return path

def main():
    """Main method"""
    global M, N, GRID
    t = int(input())
    for _ in range(t):
        M, N = map(int, input().strip().split())
        GRID = [list(map(int, input().strip().split())) for __ in range(M)]
        source_x, source_y = map(int, input().strip().split())
        source = (source_x, source_y)
        path = search(source)
        if path is not None:
            print(path)
        else:
            print(-1)

if __name__ == '__main__':
    main()
