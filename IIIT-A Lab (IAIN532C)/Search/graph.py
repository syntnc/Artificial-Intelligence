'''GRAPH ALGORITHMS'''

import heapq
from datastructures.queue import Queue

INFINITY = 10 ** 9

def get_adjacency_list(matrix):
    '''GENERATED ADJACENCY LIST FROM ADJACENCY MATRIX'''
    adj = [{} * len(matrix)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                adj[i][j] = matrix[i][j]
    return adj

def bfs(graph, source):
    '''BREADTH-FIRST SEARCH'''
    queue = Queue()
    visited, distance = set(), {}

    distance[source] = 0
    queue.enqueue(source)
    visited.add(source)

    while not queue.is_empty():
        u = queue.dequeue()
        for v in graph[u].keys():
            if v not in visited:
                visited.add(v)
                distance[v] = distance[u] + 1
                queue.enqueue(v)
    return distance

def bfs_paths(graph, source, destination):
    '''ALL POSSIBLE PATHS FROM SOURCE TO DESTINATION USING BREADTH-FIRST SEARCH'''
    queue = Queue()
    queue.enqueue((source, [source]))
    while not queue.is_empty():
        (vertex, path) = queue.dequeue()
        for next_node in graph[vertex].keys():
            if next_node == destination:
                yield path + [next_node]
            else:
                queue.enqueue((next_node, path + next_node))

def dijkstra(graph, source):
    '''DIJKSTRA'S SHORTEST PATH ALGORITHM'''
    global INFINITY
    priority_queue = []
    visited, distance = {}, {}

    visited[source], distance[source] = True, 0
    heapq.heappush(priority_queue, (0, source))

    while priority_queue:
        (distance, u) = heapq.heappop(priority_queue)
        if u in visited:
            continue
        visited[u] = True
        for v in graph[u].keys():
            if distance.setdefault(v, INFINITY) < distance[u] + graph[u][v]:
                distance[v] = distance[u] + graph[u][v]
                heapq.heappush(priority_queue, (distance[v], v))
    return distance

def dfs(graph, source, visited=None):
    '''DEPTH-FIRST SEARCH'''
    if visited is None:
        visited = set()
    visited.add(source)
    for next_node in graph[source].keys():
        if next_node not in visited:
            dfs(graph, next_node, visited)
    return visited

def dfs_paths(graph, source, destination, path=None):
    '''ALL POSSIBLE PATHS FROM SOURCE TO DESTINATION USING DEPTH-FIRST SEARCH'''
    if path is None:
        path = [source]
    if source == destination:
        yield path
    for next_node in set(graph[source].keys()) - set(path):
        yield from dfs_paths(graph, next_node, destination, path + [next_node])

def ucs(graph, source, destination):
    '''CHEAPEST PATH FROM SOURCE TO DESTINATION USING UNIFORM COST SEARCH'''
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return cost, path
        for next_node in graph[vertex].keys():
            current_cost = cost + graph[vertex][next_node]
            if not next_node in visited or visited[next_node] >= current_cost:
                visited[next_node] = current_cost
                priority_queue.put((current_cost, next_node, path + [next_node]))

def main():
    '''MAIN METHOD'''
    pass

if __name__ == '__main__':
    main()
