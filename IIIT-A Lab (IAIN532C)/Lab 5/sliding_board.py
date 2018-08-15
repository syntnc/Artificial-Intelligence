from copy import deepcopy

STACK, VISITED = None, None
N = 0

def row_rotate(state, row):
    """Rotate row by 1 unit rightwards

    :param state: 2D list depicting the current board
    :param row: Row index to be rotated

    """
    state[row] = state[row][-1:] + state[row][:-1]

def column_rotate(state, column):
    """Rotate column by 1 unit downwards

    :param state: 2D list depicting the current board
    :param column: Column index to be rotated

    """
    saved = state[-1][column]
    for row in range(N - 2, -1, -1):
        state[row + 1][column] = state[row][column]
    state[0][column] = saved

def make_tuple(state):
    """Makes immutable form of a state

    :param state: 2D list depicting the current board
    :returns: Tuple depicting the current board

    """
    return tuple([tuple(row) for row in state])

def dls(state, goal, depth):
    """Depth-limited search from source to goal state

    :param state: 2D list depicting the current board
    :param goal: 2D list depicting the board in goal state
    :param depth: Depth limit for searching
    :returns: Booolean whether goal state is found

    """
    global STACK, VISITED
    if state == goal:
        if make_tuple(state) not in VISITED:
            VISITED.add(make_tuple(state))
            STACK += [state]
        return True
    
    if depth < 0:
        return False

    saved_state = deepcopy(state)
    for row in range(N):
        for rotation_units in range(N - 1):
            row_rotate(state, row)
            if dls(state, goal, depth - 1):
                if make_tuple(state) not in VISITED:
                    VISITED.add(make_tuple(state))
                    STACK += [state]
                return True
        state = deepcopy(saved_state)

    for column in range(N):
        for rotation_units in range(N - 1):
            column_rotate(state, column)
            if dls(state, goal, depth - 1):
                if make_tuple(state) not in VISITED:
                    VISITED.add(make_tuple(state))
                    STACK += [state]
                return True
        state = deepcopy(saved_state)
    return False

def iterative_deepening(source, goal):
    """Iterative deepening search from source to goal state

    :param source: 2D list depicting the current board
    :param goal: 2D list depicting the board in the goal state
    :returns: Boolean whether iterative deepening search finds goal state

    """
    for depth in range(100):
        if dls(source, goal, depth):
            return True
    return False

def print_state(state):
    """Displays the state

    :param state: 2D list depicting the current board

    """
    print(' '.join([' '.join([str(state[row][column]) for column in range(N)]) for row in range(N)]))

def main():
    """Main method"""
    global N, STACK, VISITED
    t = int(input())
    for _ in range(t):
        STACK, VISITED = [], set()
        N = int(input())
        source = [list(map(int, input().strip().split())) for __ in range(N)]
        goal = [list(map(int, input().strip().split())) for __ in range(N)]
        if iterative_deepening(source, goal):
            path = STACK[::-1]
            for state in path:
                print_state(state)
        else:
            print(-1)

if __name__ == '__main__':
    main()
