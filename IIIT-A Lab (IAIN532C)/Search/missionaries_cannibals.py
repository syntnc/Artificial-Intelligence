class State():
    def __init__(self, cannibal_left, missionary_left, boat, cannibal_right, missionary_right):
        self.cannibal_left = cannibal_left
        self.missionary_left = missionary_left
        self.boat = boat
        self.cannibal_right = cannibal_right
        self.missionary_right = missionary_right
        self.parent = None

    def is_goal(self):
        return self.cannibal_left == 0 and self.missionary_left == 0

    def is_valid(self):
        return self.missionary_left >= 0 and self.missionary_right >= 0 \
                   and self.cannibal_left >= 0 and self.cannibal_right >= 0 \
                   and (self.missionary_left == 0 or self.missionary_left >= self.cannibal_left) \
                   and (self.missionary_right == 0 or self.missionary_right >= self.cannibal_right)

    def __eq__(self, other):
        return self.cannibal_left == other.cannibal_left and self.missionary_left == other.missionary_left \
                   and self.boat == other.boat and self.cannibal_right == other.cannibal_right \
                   and self.missionary_right == other.missionary_right

    def __hash__(self):
        return hash((self.cannibal_left, self.missionary_left, self.boat, self.cannibal_right, self.missionary_right))

TRAVEL = [[0, 2], [2, 0], [1, 1], [0, 1], [1, 0]]

def successors(cur_state):
    children = []
    if cur_state.boat == 'LEFT':
        for scenario in TRAVEL:
            new_state = State(cur_state.cannibal_left - scenario[0], cur_state.missionary_left - scenario[1], 'RIGHT',\
                              cur_state.cannibal_right + scenario[0], cur_state.missionary_right + scenario[1])
            if new_state.is_valid():
                new_state.parent = cur_state
                children.append(new_state)
    else:
        for scenario in TRAVEL:
            new_state = State(cur_state.cannibal_left + scenario[0], cur_state.missionary_left + scenario[1], 'LEFT',\
                              cur_state.cannibal_right - scenario[0], cur_state.missionary_right - scenario[1])
            if new_state.is_valid():
                new_state.parent = cur_state
                children.append(new_state)
    return children

def breadth_first_search():
    initial_state = State(3, 3, 'LEFT', 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = list()
    explored = set()
    frontier.append(initial_state)
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None

def print_solution(solution):
    path = [solution]
    parent = solution.parent
    while parent:
        path.insert(0, parent)
        parent = parent.parent

    for state in path:
        print('BOAT SIDE:', state.boat)
        print('LEFT SIDE:')
        print('CANNIBALS = %d, MISSIONARIES = %d' % (state.cannibal_left, state.missionary_left))
        print('RIGHT SIDE:')
        print('CANNIBALS = %d, MISSIONARIES = %d' % (state.cannibal_right, state.missionary_right))
        print()

def main():
    solution = breadth_first_search()
    print("SOLUTION:\n")
    print_solution(solution)

if __name__ == "__main__":
    main()
