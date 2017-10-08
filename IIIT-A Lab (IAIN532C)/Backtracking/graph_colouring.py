STATES = {\
            0: "Western Australia", \
            1: "Northern Territory", \
            2: "South Australia", \
            3: "Queensland", \
            4: "New South Wales", \
            5: "Victoria", \
            6: "Tasmania"\
        }

GRAPH = {\
            0: {1, 2}, \
            1: {0, 2, 3}, \
            2: {0, 1, 3, 4, 5}, \
            3: {1, 2, 4}, \
            4: {2, 3, 5}, \
            5: {2, 4}, \
            6: {}\
        }

COLOURS = ['RED', 'GREEN', 'BLUE']
COLOURED_GRAPH = {}

def check_valid(state, colour):
    return not any(neighbour in COLOURED_GRAPH and COLOURED_GRAPH[neighbour] == colour \
                    for neighbour in GRAPH[state])

def set_colour(state, colour):
    global COLOURED_GRAPH
    COLOURED_GRAPH[state] = colour

def colour_state(state):
    for colour in range(3):
        if check_valid(state, colour):
            set_colour(state, colour)
            return True
    return False

def change_previous_state(state):
    for offset in range(3):
        previous_state = state - 1
        alternate_colour = (COLOURED_GRAPH[previous_state] + offset) % 3
        if check_valid(previous_state, alternate_colour):
            set_colour(previous_state, alternate_colour)
            return True
    return False

def colour_graph():
    state = 0
    while state < len(STATES):
        if colour_state(state):
            state += 1
        elif not change_previous_state(state):
            state -= 1

def print_coloured_graph():
    for key, value in COLOURED_GRAPH.items():
        print(STATES[key], ":", COLOURS[value])

def main():
    colour_graph()
    print_coloured_graph()

if __name__ == '__main__':
    main()
