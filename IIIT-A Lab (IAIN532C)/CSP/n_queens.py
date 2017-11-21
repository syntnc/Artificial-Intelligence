N, BOARD, SOLUTION = None, None, []

def check(column_a, column_b, domains, row):
    '''CHECKS IF THERE IS ANY REMAINING FEASIBLE CONFIGURATION'''
    return any(b != row for b in domains[column_b]) and \
            any(abs(column_a - column_b) != abs(b - row) for b in domains[column_b])

def ac3(column, domains):
    '''MAINTAINS ARC CONSISTENCY'''
    queue = [(neighbour, column) for neighbour in range(N) if neighbour > column]
    while queue != []:
        column_a, column_b = queue.pop(0)
        remaining = [row for row in domains[column_a] if not check(column_a, column_b, domains, row)]
        for row in remaining:
            if row in domains[column_a]:
                domains[column_a].remove(row)
        if domains[column_a] == []:
            return False
        if remaining != []:
            for neighbour in set(range(N)) - {column_a, column_b}:
                if (neighbour, column_a) not in queue:
                    queue.append((neighbour, column_a))
    return True                

def backtrack(column, domains):
    '''BACKTRACKING CSP SOLVER'''
    global BOARD, SOLUTION
    from copy import deepcopy
    if column == N:
        return True
    for row in domains[column]:
        BOARD[row][column] = 'Q'
        copied_domains = deepcopy(domains)
        del copied_domains[column][:]
        copied_domains[column].append(row)
        if ac3(column, copied_domains):
            SOLUTION.append(row)
            if backtrack(column + 1, copied_domains):
                return True
            SOLUTION.pop()
        BOARD[row][column] = '-'
    return False

def main():
    '''MAIN FUNCTION'''
    global N, BOARD
    N = int(input())
    BOARD = [['-' for _ in range(N)] for __ in range(N)]
    domains = [list(range(N)) for _ in range(N)]
    if backtrack(0, domains):
        print(SOLUTION)
    else:
        print('NO SOLUTION')

if __name__ == '__main__':
    main()
