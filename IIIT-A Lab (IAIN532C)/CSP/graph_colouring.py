GRAPH , COLOURED_STATES , N_COLOURS = {}, {}, None

def get_graph():
    '''TAKES INPUT FROM USER'''
    global GRAPH, COLOURED_STATES, N_COLOURS
    n = int(input().strip())
    for vertex in range(n):
        GRAPH[vertex], COLOURED_STATES[vertex] = set(), None
    while True:
        vertex_a, vertex_b = map(int, input().strip().split())
        if vertex_a == -1:
            break
        GRAPH[vertex_a].add(vertex_b)
        GRAPH[vertex_b].add(vertex_a)
    N_COLOURS = int(input().strip())

def heuristic_variable(domains):
    '''MINIMUM REMAINING VAlUE AND DEGREE HEURISTIC'''
    return min([state for state in GRAPH if COLOURED_STATES[state] is None], key=lambda x: (len(domains[x]), -len(GRAPH[x])))       

def heuristic_value(domains, state):
    '''LEAST CONSTRAINED VLAUE HEURISTIC'''
    from queue import PriorityQueue
    priority_queue = PriorityQueue()
    for colour in domains[state]:
        priority_queue.put((sum(1 for neighbour in GRAPH[state] if colour in domains[neighbour]), colour))
    ordered_values = []
    while not priority_queue.empty():
        ordered_values.append(priority_queue.get()[1])
    return ordered_values

def ac3(level, domains):
    '''MAINTAINS ARC CONSISTENCY'''
    queue = []
    for vertex in set(GRAPH.keys()) - {level}:
        for neighbour in GRAPH[vertex]:
            queue.append((vertex, neighbour))
    while not queue == []:
        vertex_a, vertex_b = queue.pop(0)
        changed = False
        if COLOURED_STATES[vertex_b] is not None and COLOURED_STATES[vertex_b] in domains[vertex_a]:
            domains[vertex_a].remove(COLOURED_STATES[vertex_b])
            changed = True
        if changed:
            for vertex in set(GRAPH.keys()) - {vertex_a}:
                if vertex_a in GRAPH[vertex]:
                    queue.append((vertex, vertex_a))
    return not any(domain == [] for domain in domains)

def colour_graph(level, domains):
    '''BACKTRACKING CSP SOLVER'''
    from copy import deepcopy
    global COLOURED_STATES
    if level == len(GRAPH.keys()):
        return True
    selected_state = heuristic_variable(domains)
    ordered_domain = heuristic_value(domains, selected_state)
    for colour in ordered_domain:
        COLOURED_STATES[selected_state] = colour
        new_domains = deepcopy(domains)
        if ac3(level, new_domains):
            if colour_graph(level + 1, new_domains):
                return True
        COLOURED_STATES[selected_state] = None
    return False

def main():
    '''MAIN FUNCTION'''
    t = int(input())
    for _ in range(t):
        get_graph()
        domains = [list(range(N_COLOURS)) for _ in range(len(GRAPH.keys()))]
        if colour_graph(0, domains):
            for node in GRAPH:
                print(node, ':', COLOURED_STATES[node])
        else:
            print('CANNOT COLOUR GRAPH')

if __name__ == '__main__':
    main()
