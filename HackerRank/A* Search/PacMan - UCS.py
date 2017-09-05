'''SOLVING PACMAN PROBLEM USING UCS'''

from copy import deepcopy

DIRECTIONS = ['UP', 'LEFT', 'RIGHT', 'DOWN']
MOVES = {'UP':[-1, 0], 'LEFT':[0, -1], 'RIGHT':[0, 1], 'DOWN':[1, 0]}
ROWS, COLUMNS = 0, 0

def move_next(grid, coordinate):
    '''GETS NEXT VALID MOVES IN ALL FOUR DIRECTIONS FROM CURRENT COORDINATE'''
    next_moves = []
    for direction in DIRECTIONS:
        next_x, next_y = coordinate['x'] + MOVES[direction][0], coordinate['y'] + MOVES[direction][1]
        if next_x < 0 or next_x >= ROWS or next_y < 0 and next_y >= COLUMNS:
            continue
        if grid[next_x][next_y] == '-' or grid[next_x][next_y] == '.':
            cost = 0 if grid[next_x][next_y] == '.' else 1
            grid[next_x][next_y] = '='
            next_moves.append((dict(x=next_x, y=next_y), cost))
    return [move[0] for move in sorted(next_moves, key=lambda x:x[1])]

def ucs(grid, source, goal):
    '''CHEAPEST-FIRST SEARCH FROM SOURCE TO GOAL'''
    queue = [[source, []]]
    path = None
    while queue:
        coordinate, previous_path = queue.pop(0)
        current_path = deepcopy(previous_path)
        current_path.append(coordinate)
        if coordinate == goal:
            if path is None:
                path = current_path
                break
        queue += [[node, current_path] for node in move_next(grid, coordinate)]
    return path

def main():
    '''MAIN METHOD'''
    pacman_row, pacman_column = map(int, input().strip().split())
    food_row, food_column = map(int, input().strip().split())
    global ROWS, COLUMNS
    ROWS, COLUMNS = map(int, input().strip().split())

    grid = []
    for _ in range(ROWS):
        grid.append(list(input().strip()))

    source = dict(x=pacman_row, y=pacman_column)
    goal = dict(x=food_row, y=food_column)
    path = ucs(grid, source, goal)

    print(len(path) - 1)
    for node in path:
        print(node['x'], node['y'])

if __name__ == '__main__':
    main()
