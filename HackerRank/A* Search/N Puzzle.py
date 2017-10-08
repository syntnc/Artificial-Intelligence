from copy import deepcopy
from queue import PriorityQueue
import math

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

    def mismatch(self, state):
        '''HEURISTIC FUNCTION BASED ON THE NUMBER OF MISMATCHED TILES'''
        return sum(1 for i in range(SIZE)\
                for j in range(SIZE) if state[i][j] != self.goal[i][j])

    @staticmethod
    def get_row_index(tile):
        return tile / SIZE

    @staticmethod
    def get_column_index(tile):
        return tile % SIZE

    def manhattan(self, state):
        return sum(abs(self.get_row_index(state[i][j]) - i) \
                    + abs(self.get_column_index(state[i][j] - j))\
                    for j in range(SIZE)\
                    for i in range(SIZE))

    def heuristic(self, node):
        return node.depth + self.manhattan(node.state) + math.sqrt(self.mismatch(node.state))

    def a_star(self):
        '''START TO GOAL OF PUZZLE USING A-STAR SEARCH'''
        start_node = Node(self.start, None, None, 0, 0)
        start_node.cost = self.heuristic(start_node)
        priority_queue = PriorityQueue()
        priority_queue.put(start_node)
        visited = {}
        visited[Puzzle.get_state_tuple(self.start)] = 1
        while not priority_queue.empty():
            node = priority_queue.get()
            if node.state == self.goal:
                self.moves, temp = [], node
                while True:
                    if temp.parent is None:
                        break
                    self.moves.insert(0, temp.operation)
                    temp = temp.parent
                return
            expansion = Puzzle.expand_node(node, visited)
            for node in expansion:
                visited[Puzzle.get_state_tuple(node.state)] = 1
                node.cost = self.heuristic(node)
                priority_queue.put(node)
        self.moves = None

def main():
    board_dimension = int(input())
    initial_board = [[] for _ in range(board_dimension)]
    for i in range(board_dimension * board_dimension):
        initial_board[i // board_dimension].append(int(input()))
    goal_board = [[0, 1, 2],\
                  [3, 4, 5],\
                  [6, 7, 8]]
    puzzle = Puzzle(initial_board, goal_board)
    puzzle.a_star()
    print(len(puzzle.moves))
    print('\n'.join(puzzle.moves))

if __name__ == '__main__':
    main()
