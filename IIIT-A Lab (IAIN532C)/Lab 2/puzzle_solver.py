'''GENERALIZED PUZZLE SOLVER'''
from copy import deepcopy
from queue import PriorityQueue

class Node(object):
    '''NODE OF PUZZLE STATE TREE'''
    def __init__(self, state, parent, operation, depth, cost):
        self.state = state
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost
    
    def __eq__(self, other):
        return self.cost == other.cost

    def __ne__(self, other):
        return self.cost != other.cost
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __ge__(self, other):
        return self.cost >= other.cost

SIZE = 0
DIRECTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']
MOVES = {'UP':[-1, 0], 'LEFT':[0, -1], 'RIGHT':[0, 1], 'DOWN':[1, 0]}

class Puzzle(object):
    '''GENERALIZED PUZZLE'''
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.moves = []
        global SIZE
        SIZE = len(goal)

    @staticmethod
    def display_board(board):
        '''DISPLAYS THE CURRENT STATE OF THE BOARD'''
        output_file = open('out.txt', 'a')
        output_file.write('------' * SIZE + '\n')
        for row in board:
            output_file.write('\t|\t'.join(str(i) for i in row) + '\n')
            output_file.write('------' * SIZE + '\n')
        output_file.write('\n')
        output_file.close()

    @staticmethod
    def get_inversion_count(arr):
        '''RETURNS NUMBER OF INVERSIONS IN AN ARRAY '''
        return sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr))\
                if arr[j] and arr[i] and arr[i] > arr[j])

    @staticmethod
    def get_blank_position(state):
        '''RETURNS THE BLANK POSITION IN THE BOARD'''
        for row_index, row in enumerate(state):
            if 0 in row:
                return (row_index, row.index(0))

    @staticmethod
    def move(direction, state):
        '''MOVES FROM ONE STATE TO NEXT STATE'''
        blank = Puzzle.get_blank_position(state)
        new_state = deepcopy(state)
        old_x, old_y = blank[0], blank[1]
        new_x, new_y = old_x + MOVES[direction][0], old_y + MOVES[direction][1]
        if new_x < SIZE and new_x >= 0 and new_y < SIZE and new_y >= 0:
            new_state[old_x][old_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[old_x][old_y]
            return new_state
        else:
            return None

    @staticmethod
    def get_state_tuple(state):
        '''RETURNS STATE IN TUPLE FORM'''
        return tuple([tuple(row) for row in state])

    @staticmethod
    def expand_node(node, visited):
        """Returns a list of expanded nodes"""
        expanded_nodes = []
        for direction in DIRECTIONS:
            new_state = Puzzle.move(direction, node.state)
            expanded_nodes.append(Node(new_state, node, direction, node.depth + 1, 0))
        # Filter the list and remove the nodes that are impossible (move function returned None)
        expanded_nodes = [node for node in expanded_nodes if node.state != None and Puzzle.get_state_tuple(node.state) not in visited] #list comprehension!
        return expanded_nodes

    def bfs(self):
        '''START TO GOAL OF PUZZLE USING BREADTH-FIRST SEARCH'''
        queue = [Node(self.start, None, None, 0, 0)]
        visited = {}
        visited[Puzzle.get_state_tuple(self.start)] = 1
        while True:
            if queue == []:
                return
            node = queue.pop(0)
            if node.state == self.goal:
                self.moves, temp = [], node
                while True:
                    if temp is None:
                        break
                    self.moves.insert(0, temp.state)
                    temp = temp.parent
                return
            expansion = Puzzle.expand_node(node, visited)
            for node in expansion:
                visited[Puzzle.get_state_tuple(node.state)] = 1
            queue.extend(expansion)
        self.moves = None

    def dfs(self, depth=10):
        '''START TO GOAL OF PUZZLE USING DEPTH-FIRST SEARCH'''
        depth_limit = depth
        stack = [Node(self.start, None, None, 0, 0)]
        visited = {}
        visited[Puzzle.get_state_tuple(self.start)] = 1
        while True:
            if stack == []:
                return
            node = stack.pop(0)
            visited[Puzzle.get_state_tuple(node.state)] = 1
            if node.state == self.goal:
                self.moves, temp = [], node
                while True:
                    if temp is None:
                        break
                    self.moves.insert(0, temp.state)
                    temp = temp.parent
                return
            if node.depth < depth_limit:
                expanded_stack = Puzzle.expand_node(node, visited)
                expanded_stack.extend(stack)
                stack = expanded_stack
        self.moves = None

    def heuristic_mismatch(self, state):
        '''HEURISTIC FUNCTION BASED ON THE NUMBER OF MISMATCHED TILES'''
        return sum(1 for i in range(SIZE)\
                for j in range(SIZE) if state[i][j] != self.goal[i][j])

    def get_best_first_node(self, x):
        '''CREATE NODE FOR BEST-FIRST SEARCH PRIORITY QUEUE'''
        return self.heuristic_mismatch(x.state)

    def get_a_star_node(self, x):
        '''CREATE NODE FOR A-STAR SEARCH PRIORITY QUEUE'''
        return x.depth + self.heuristic_mismatch(x.state)

    def best_first(self):
        '''START TO GOAL OF PUZZLE USING BEST-FIRST SEARCH'''
        start_node = Node(self.start, None, None, 0, 0)
        start_node.cost = self.get_best_first_node(start_node)
        priority_queue = PriorityQueue()
        priority_queue.put(start_node)
        visited = {}
        visited[Puzzle.get_state_tuple(self.start)] = 1
        while not priority_queue.empty():            
            node = priority_queue.get()
            if node.state == self.goal:
                self.moves, temp = [], node
                while True:
                    if temp is None:
                        break
                    self.moves.insert(0, temp.state)
                    temp = temp.parent
                return
            expansion = Puzzle.expand_node(node, visited)
            for node in expansion:
                visited[Puzzle.get_state_tuple(node.state)] = 1
                node.cost = self.get_best_first_node(node)
                priority_queue.put(node)
        self.moves = None

    def a_star(self):
        '''START TO GOAL OF PUZZLE USING A-STAR SEARCH'''
        start_node = Node(self.start, None, None, 0, 0)
        start_node.cost = self.get_a_star_node(start_node)
        priority_queue = PriorityQueue()
        priority_queue.put(start_node)
        visited = {}
        visited[Puzzle.get_state_tuple(self.start)] = 1
        while not priority_queue.empty():            
            node = priority_queue.get()
            if node.state == self.goal:
                self.moves, temp = [], node
                while True:
                    if temp is None:
                        break
                    self.moves.insert(0, temp.state)
                    temp = temp.parent
                return
            expansion = Puzzle.expand_node(node, visited)
            for node in expansion:
                visited[Puzzle.get_state_tuple(node.state)] = 1
                node.cost = self.get_a_star_node(node)
                priority_queue.put(node)
        self.moves = None
