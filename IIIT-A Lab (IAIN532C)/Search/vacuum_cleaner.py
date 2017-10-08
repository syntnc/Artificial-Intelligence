from copy import deepcopy

GRID_SIZE = 0
DIRECTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'SUCK']
MOVES = {'UP':[-1, 0], 'DOWN':[1, 0], 'LEFT':[0, -1], 'RIGHT':[0, 1], 'SUCK':[0, 0]}

class Node(object):
    def __init__(self, grid, cleaner, move, parent):
        self.grid = grid
        self.cleaner = cleaner
        self.move = move
        self.parent = parent

    def is_goal(self):
        return not any(self.grid[i][j] == 1 for j in range(GRID_SIZE) for i in range(GRID_SIZE))

    def inside_grid(self):
        return self.cleaner['x'] >= 0 and self.cleaner['x'] < GRID_SIZE and\
               self.cleaner['y'] >= 0 and self.cleaner['y'] < GRID_SIZE

def get_state_tuple(node):
    return (tuple([tuple(row) for row in node.grid]), node.cleaner['x'], node.cleaner['y'])

def move_cleaner(node, direction):
    new_node = deepcopy(node)
    new_node.cleaner = dict(x=node.cleaner['x'] + MOVES[direction][0], y=node.cleaner['y'] + MOVES[direction][1])
    if new_node.inside_grid():
        if direction == 'SUCK':
            new_node.grid[new_node.cleaner['x']][new_node.cleaner['y']] = 0
        new_node.parent = node
        new_node.move = direction
        return new_node

def expand_nodes(node, visited):
    expanded_nodes = [move_cleaner(node, direction) for direction in DIRECTIONS]
    return [node for node in expanded_nodes if node is not None and get_state_tuple(node) not in visited]

def bfs(cleaner, grid):
    starting_node = Node(grid, cleaner, None, None)
    frontier = [starting_node]
    visited = {}
    visited[get_state_tuple(starting_node)] = True
    while frontier != []:
        node = frontier.pop(0)
        if node.is_goal():
            finishing_position = node.cleaner
            moves, temp = [], node
            while temp.parent != None:
                moves.insert(0, temp.move)
                temp = temp.parent
            return moves, finishing_position
        expanded_nodes = expand_nodes(node, visited)
        for node in expanded_nodes:
            visited[get_state_tuple(node)] = 1
        frontier.extend(expanded_nodes)

def main():
    global GRID_SIZE
    GRID_SIZE = int(input('ENTER GRID SIZE: ').strip())
    cleaner_x, cleaner_y = map(int, input('\nENTER CLEANER POSITION:\n').strip().split())
    cleaner = dict(x=cleaner_x, y=cleaner_y)
    print('\nENTER INITIAL GRID:')
    grid = [list(map(int, input().strip().split())) for _ in range(GRID_SIZE)]
    moves, finishing_position = bfs(cleaner, grid)
    print('\nSOLUTION:')
    print(' -> '.join(moves))
    print('CLEANER\'S FINAL POSTION IS AT (%d,%d)' % (finishing_position['x'], finishing_position['y']))

if __name__ == '__main__':
    main()
