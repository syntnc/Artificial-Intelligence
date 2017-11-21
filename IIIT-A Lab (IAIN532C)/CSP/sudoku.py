def get_board():
    '''TAKES USER INPUT OF THE INITIAL BOARD CONFIGURATION'''
    return [list(map(int, input().strip().split())) for _ in range(9)]

def validate(board, domains):
    '''REDUCES DOMAIN FOR THE ENTIRE BOARD'''
    for row in range(9):
        for column in range(9):
            if board[row][column] != 0:
                ac3(row, column, board, domains)
    return not any(domains[i][j] == [] for j in range(9) for i in range(9))

def get_first_unassigned_position(board):
    '''RETURNS THE FIRST UNASSIGNED POSITION IN THE BOARD'''
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column
    return -1, -1

def row_reduce(row, column, board, domains):
    '''REDUCES DOMAIN IN A ROW'''
    for other_column in set(range(9)) - {column}:
        if board[row][column] in domains[row][other_column]:
            domains[row][other_column].remove(board[row][column])

def column_reduce(row, column, board, domains):
    '''REDUCES DOMAIN IN A COLUMN'''
    for other_row in set(range(9)) - {row}:
        if board[row][column] in domains[other_row][column]:
            domains[other_row][column].remove(board[row][column])

def box_reduce(row, column, board, domains):
    '''REDUCES DOMAIN IN A 3x3 SUBGRID'''
    box_row, box_column = (row // 3) * 3, (column // 3) * 3
    for other_row in set(range(box_row, box_row + 3)) - {row}:
        for other_column in set(range(box_column, box_column + 3)) - {column}:
            if board[row][column] in domains[other_row][other_column]:
                domains[other_row][other_column].remove(board[row][column])

def ac3(row, column, board, domains):
    '''MAINTAINS ARC CONSISTENCY'''
    box_reduce(row, column, board, domains)
    row_reduce(row, column, board, domains)
    column_reduce(row, column, board, domains)
    return not any(domains[i][j] == [] for j in range(9) for i in range(9))

def backtrack(board, domains):
    '''BACKTRACKING CSP SOLVER'''
    from copy import deepcopy
    row, column = get_first_unassigned_position(board)
    if (row, column) == (-1, -1):
        return True
    for value in domains[row][column]:
        board[row][column] = value
        new_domains = deepcopy(domains)
        if ac3(row, column, board, new_domains):
            if backtrack(board, new_domains):
                return True
        board[row][column] = 0
    return False

def print_board(board):
    '''DISPLAYS THE BOARD'''
    for row in board:
        print(' '.join(str(i) for i in row))

def main():
    '''MAIN FUNCTION'''
    board = get_board()
    domains = [[[j + 1 for j in range(9)] for k in range(9)] for i in range(9)]
    if validate(board, domains):
        if backtrack(board, domains):
            print_board(board)
    else:
        print('NO SOLUTION')

if __name__ == '__main__':
    main()
