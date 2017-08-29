'''ALL POSSIBLE PATH PROBLEM FOR ROMANIAN CITIES'''

GRAPH = {\
            'Arad': {'Sibiu': 140, 'Zerind': 75, 'Tumiscara': 118},\
            'Zerind': {'Arad': 75, 'Oradea': 71},\
            'Oradea': {'Zerind': 71, 'Sibiu': 151},\
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Faragas': 99, 'Rimnicu': 80},\
            'Tumiscara': {'Arad': 118, 'Lugoj': 111},\
            'Lugoj': {'Tumiscara': 111, 'Mehadia': 70},\
            'Mehadia': {'Lugoj': 70, 'Dobreta': 75},\
            'Dobreta': {'Mehadia': 75, 'Cralova': 120},\
            'Cralova': {'Dobreta': 120, 'Rimnicu': 146, 'Pitesti': 138},\
            'Rimnicu': {'Sibiu': 80, 'Cralova': 146, 'Pitesti': 97},\
            'Faragas': {'Sibiu': 99, 'Bucharest': 211},\
            'Pitesti': {'Rimnicu': 97, 'Cralova': 138, 'Bucharest': 101},\
            'Bucharest': {'Faragas': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},\
            'Giurgiu': {'Bucharest': 90},\
            'Urziceni': {'Bucharest': 85, 'Vashui': 142, 'Hirsova': 98},\
            'Hirsova': {'Urziceni': 98, 'Eforic': 86},\
            'Eforic': {'Hirsova': 86},\
            'Vashui': {'Iasi': 92, 'Urziceni': 142},\
            'Iasi': {'Vashui': 92, 'Neamt': 87},\
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

def main():
    '''MAIN FUNCTION'''
    print('ENTER SOURCE :', end=' ')
    source = input().strip()
    print('ENTER GOAL :', end=' ')
    goal = input().strip()
    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        paths = dfs_paths(source, goal)
        for path in paths:
            print(' -> '.join(city for city in path))

if __name__ == '__main__':
    main()
