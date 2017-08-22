import sys

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Node:
    def __init__( self, state, parent, operator, depth, cost ):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost

def get_inversion_count(arr):
    return sum(1 for i in range(9) for j in range(i + 1, 10)\
                if arr[j] and arr[i] and arr[i] > arr[j])

def solvable(state):
    flattened_state = sum(state, [])
    return True if get_inversion_count(flattened_state) % 2 == 0 else False

def display_board(state):
    print('-----' * 3)
    for row in state:
        print(' | '.join(str(i) for i in row))
        print('-----' * 3)

def move_up(state):
    pass

def move_down(state):
    pass

def move_left(state):
    pass

def move_right(state):
    pass

def expand_node(node, nodes):
    """Returns a list of expanded nodes"""
    expanded_nodes = []
    expanded_nodes.append(Node( move_up(node.state), node, "up", node.depth + 1, 0 ) )
    expanded_nodes.append(Node( move_down(node.state), node, "down", node.depth + 1, 0 ) )
    expanded_nodes.append(Node( move_left(node.state), node, "left", node.depth + 1, 0 ) )
    expanded_nodes.append(Node( move_right(node.state), node, "right", node.depth + 1, 0 ) )
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
    return expanded_nodes

def bfs(state):
    global goal
    queue = [Node(state, None, None, 0, 0)]
    
    while queue != []:
        node = queue.pop(0)
        if node.state == goal:
            moves, temp = [], node
            while True:
                moves.insert(0, temp.operator)
                if temp.depth == 1:
                    break
                temp = temp.parent
            return moves
        queue.extend(expand_node(node, queue))
    return None 

def heuristic_mismatch(state):
    pass

def heuristic_manhattan(state):
    pass

def main():
    start = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    if not solvable:
        print('NOT SOLVABLE')
    else:
        print(bfs(start))

if __name__ == '__main__':
    main()