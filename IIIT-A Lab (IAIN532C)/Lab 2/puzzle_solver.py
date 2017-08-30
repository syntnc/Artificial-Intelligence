'''GENERALIZED PUZZLE SOLVER'''

class Node(object):
    '''NODE OF PUZZLE STATE TREE'''
    def __init__(self, state, parent, operation, depth, cost):
        self.state = state
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost

class Puzzle(object):
    '''GENERALIZED PUZZLE'''
    def __init__(self, goal):
        self.state = []
        self.goal = goal
        self.moves = []
        self.dimension = len(goal)

    def display_board(self):
        '''DISPLAYS THE CURRENT STATE OF THE BOARD'''
        print('-----' * self.dimension)
        for row in self.state:
            print(' | '.join(str(i) for i in row))
            print('-----' * 3)
    
    def get_inversion_count(self, arr):
        return sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr) + 1)\
                if arr[j] and arr[i] and arr[i] > arr[j])

    def move_up(self, state):
        pass

    def move_down(self, state):
        pass

    def move_left(self, state):
        pass

    def move_right(self, state):
        pass

    def expand_node(self, node):
        """Returns a list of expanded nodes"""
        expanded_nodes = []
        expanded_nodes.append(Node( move_up(node.state), node, "up", node.depth + 1, 0 ))
        expanded_nodes.append(Node( move_down(node.state), node, "down", node.depth + 1, 0 ))
        expanded_nodes.append(Node( move_left(node.state), node, "left", node.depth + 1, 0 ))
        expanded_nodes.append(Node( move_right(node.state), node, "right", node.depth + 1, 0 ))
        # Filter the list and remove the nodes that are impossible (move function returned None)
        expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
        return expanded_nodes

    def bfs(self, state):
        queue = [Node(state, None, None, 0, 0)]
    
        while queue != []:
            node = queue.pop(0)
            if node.state == self.goal:
                self.moves, temp = [], node
                while True:
                    self.moves.insert(0, temp.operator)
                    if temp.depth == 1:
                        break
                    temp = temp.parent
                return self.moves
            queue.extend(self.expand_node(node))
        return None

    def dfs(self, state):
        pass

    def heuristic_mismatch(self, state):
        '''HEURISTIC FUNCTION BASED ON THE NUMBER OF MISMATCHED TILES'''
        return sum(1 for i in range(self.dimension)\
                for j in range(self.dimension) if state[i][j] != self.goal[i][j])

    def heuristic_manhattan(self, state):
        # ERROR
        '''HEURISTIC FUNCTION BASED ON THE SUM MANHATTAN DISTANCES OF CURRENT AND GOAL STATE'''
        return sum(abs(state[i][j] % self.dimension - i) + abs(state[i][j] % self.dimension - j)\
                for i in range(self.dimension) for j in range(self.dimension))

    def comparator(self, x, y):
        return (x.depth + self.heuristic_mismatch(x.state))- (y.depth + self.heuristic_mismatch(x.state))
    
    def best_first(self):
        pass
    
    def a_star(self):
        pass
