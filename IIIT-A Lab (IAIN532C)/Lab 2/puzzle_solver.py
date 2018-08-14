"""Generic puzzle solver"""
import argparse
import sys
from copy import deepcopy
from functools import total_ordering
from queue import PriorityQueue


@total_ordering
class Node(object):
    """Node of puzzle state tree"""
    def __init__(self, state, parent, operation, depth, cost):
        self.state = state
        self.parent = parent
        self.operation = operation
        self.depth = depth
        self.cost = cost
    
    def __eq__(self, other):
        return self.cost == other.cost
    
    def __lt__(self, other):
        return self.cost < other.cost

SIZE = 0
DIRECTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']
MOVES = {'UP':[-1, 0], 'LEFT':[0, -1], 'RIGHT':[0, 1], 'DOWN':[1, 0]}

class Puzzle(object):
    """Generic puzzle class"""
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.moves = []
        self.search_algorithm = None
        global SIZE
        SIZE = len(goal)
    
    @staticmethod
    def parse_arguments():
        """Parser of command line arguments to get requested search alogrithm
        
        :returns: Arguments object contianing all command line arguments

        """
        argparser = argparse.ArgumentParser(description='Puzzle Solver')
        argparser.add_argument(
            '-s', '--search',
            dest='algorithm',
            help='Search alogrithm to find goal state',
            default='a_star',
            type=str
        )
        argparser.add_argument(
            '-d', '--depth',
            dest='depth',
            help='Depth limit for DFS',
            default=10,
            type=int
        )
        return argparser.parse_args()
    
    def search(self):
        """Calls the user-requested search function"""
        algorithms = {'bfs': self.bfs,
                      'dfs': self.dfs, 
                      'best_first': self.best_first,
                      'a_star': self.a_star}
        
        arguments = self.parse_arguments()
        self.search_algorithm = arguments.algorithm
        search_function = algorithms[self.search_algorithm]
        depth = arguments.depth
        if self.search_algorithm not in algorithms.keys():
            sys.exit('ERROR: INVALID SEARCH ALGORITHM')

        if self.search_algorithm != 'dfs':
            search_function()
        else:
            search_function(depth)

    @staticmethod
    def display_board(board):
        """Displays the current state of the board

        :param board: 2D list depicting the current board

        """
        output_file = open('out.txt', 'a')
        output_file.write('------' * SIZE + '\n')
        for row in board:
            output_file.write('\t|\t'.join(str(i) for i in row) + '\n')
            output_file.write('------' * SIZE + '\n')
        output_file.write('\n')
        output_file.close()

    @staticmethod
    def get_inversion_count(arr):
        """Returns number of inversions in an array

        :param arr: Generic array (list)
        :returns: Number of inversions in the array

        """
        return sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr))\
                if arr[j] and arr[i] and arr[i] > arr[j])

    @staticmethod
    def get_blank_position(state):
        """Returns the blank position in the board

        :param state: 2D list depicting the current board
        :returns: Tuple depicting coordinates of the first blank position in the board

        """
        for row_index, row in enumerate(state):
            if 0 in row:
                return (row_index, row.index(0))

    @staticmethod
    def move(direction, state):
        """Moves from one state to next state

        :param direction: Direction in which the blank space should move
        :param state: 2D list depicting the current board
        :returns: 2D list depicting the new state of the board

        """
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
        """Returns state in tuple form

        :param state: 2D list depicting the current board
        :returns: Tuple depicting the current board

        """
        return tuple([tuple(row) for row in state])

    @staticmethod
    def expand_node(node, visited):
        """Returns a list of expanded nodes

        :param node: Current node object being scanned
        :param visited: List of nodes previously visited
        :returns: List of expanded nodes currently and previously visited

        """
        expanded_nodes = []
        for direction in DIRECTIONS:
            new_state = Puzzle.move(direction, node.state)
            expanded_nodes.append(Node(new_state, node, direction, node.depth + 1, 0))
        # Filter the list and remove the nodes that are impossible (move function returned None)
        expanded_nodes = [node for node in expanded_nodes if node.state != None and Puzzle.get_state_tuple(node.state) not in visited] #list comprehension!
        return expanded_nodes

    def bfs(self):
        """Traversal form start to goal of puzzle using breadth-first search"""
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
        """Traversal from start to goal of puzzle using depth-first search

        :param depth: Depth limit for DFS (Default value = 10)

        """
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
        """heuristic function based on the number of mismatched tiles

        :param state: 2D list depicting the current board
        :returns: Heuristic value of mismatches of current state from goal state

        """
        return sum(1 for i in range(SIZE)\
                for j in range(SIZE) if state[i][j] != self.goal[i][j])

    def get_best_first_node(self, x):
        """Create node for best-first search priority queue

        :param x: Node object being scanned
        :returns: Heuristic value of mismatches of state of current node from goal state

        """
        return self.heuristic_mismatch(x.state)

    def get_a_star_node(self, x):
        """Create node for a-star search priority queue

        :param x: 2D list depicting the current board
        :returns: Sum of depth of the current state and heuristic value of mismatches of state of current node from goal state

        """
        return x.depth + self.heuristic_mismatch(x.state)

    def best_first(self):
        """Traversal from start to goal of puzzle using best-first search"""
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
        """Traversal from start to goal of puzzle using a-star search"""
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
