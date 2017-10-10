'''ALL POSSIBLE PATH PROBLEM FOR ROMANIAN CITIES'''

GRAPH = {\
            'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},\
            'Zerind': {'Arad': 75, 'Oradea': 71},\
            'Oradea': {'Zerind': 71, 'Sibiu': 151},\
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},\
            'Timisoara': {'Arad': 118, 'Lugoj': 111},\
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},\
            'Mehadia': {'Lugoj': 70, 'Drobeta': 75},\
            'Drobeta': {'Mehadia': 75, 'Craiova': 120},\
            'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},\
            'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},\
            'Fagaras': {'Sibiu': 99, 'Bucharest': 211},\
            'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},\
            'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},\
            'Giurgiu': {'Bucharest': 90},\
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},\
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},\
            'Eforie': {'Hirsova': 86},\
            'Vaslui': {'Iasi': 92, 'Urziceni': 142},\
            'Iasi': {'Vaslui': 92, 'Neamt': 87},\
            'Neamt': {'Iasi': 87}\
        }

def dfs_paths(source, destination, path=None):
    '''ALL POSSIBLE PATHS FROM SOURCE TO DESTINATION USING DEPTH-FIRST SEARCH'''
    if path is None:
        path = [source]
    if source == destination:
        yield path
    for next_node in set(GRAPH[source].keys()) - set(path):
        yield from dfs_paths(next_node, destination, path + [next_node])

def ucs(source, destination):
    '''CHEAPEST PATH FROM SOURCE TO DESTINATION USING UNIFORM COST SEARCH'''
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            if not next_node in visited or visited[next_node] >= current_cost:
                visited[next_node] = current_cost
                priority_queue.put((current_cost, next_node, path + [next_node]))

def a_star(source, destination):
    '''OPTIMAL PATH FROM SOURCE TO DESTINATION USING STRAIGHT LINE DISTANCE HEURISTIC'''
    # HERE THE STRAIGHT LINE DISTANCE VALUES ARE IN REFERENCE TO BUCHAREST AS THE DESTINATION
    straight_line = {\
                        'Arad': 366,\
                        'Zerind': 374,\
                        'Oradea': 380,\
                        'Sibiu': 253,\
                        'Timisoara': 329,\
                        'Lugoj': 244,\
                        'Mehadia': 241,\
                        'Drobeta': 242,\
                        'Craiova': 160,\
                        'Rimnicu': 193,\
                        'Fagaras': 176,\
                        'Pitesti': 100,\
                        'Bucharest': 0,\
                        'Giurgiu': 77,\
                        'Urziceni': 80,\
                        'Hirsova': 151,\
                        'Eforie': 161,\
                        'Vaslui': 199,\
                        'Iasi': 226,\
                        'Neamt': 234\
                    }
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[source], 0, source, [source]))
    visited[source] = straight_line[source]
    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return heuristic, cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic = current_cost + straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put((heuristic, current_cost, next_node, path + [next_node]))

def main():
    '''MAIN FUNCTION'''
    print('ENTER SOURCE :', end=' ')
    source = input().strip()
    print('ENTER GOAL :', end=' ')
    goal = input().strip()
    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        print('\nALL POSSIBLE PATHS:')
        paths = dfs_paths(source, goal)
        for path in paths:
            print(' -> '.join(city for city in path))
        print('\nCHEAPEST PATH:')
        cost, cheapest_path = ucs(source, goal)
        print('PATH COST =', cost)
        print(' -> '.join(city for city in cheapest_path))
        print('\nOPTIMAL PATH:')
        heuristic, cost, optimal_path = a_star(source, goal)
        print('HEURISTIC = ', heuristic)
        print('PATH COST =', cost)
        print(' -> '.join(city for city in optimal_path))

if __name__ == '__main__':
    main()
