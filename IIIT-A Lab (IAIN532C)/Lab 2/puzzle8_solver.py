"""8-puzzle solver"""

from puzzle_solver import Puzzle


class Puzzle8(Puzzle):
    """8-puzzle"""
    def __init__(self, start):
        super(Puzzle8, self).__init__(start, [[1, 2, 3], \
                                        [4, 5, 6], \
                                        [7, 8, 0]])

    def solvable(self):
        """Checks if 8-puzzle is solvable from current state to goal state"""
        flattened_state = sum(self.start, [])
        return True if self.get_inversion_count(flattened_state) % 2 == 0 else False

def main():
    """Main method"""
    input_file = open('input_8.txt', 'r')
    start = [list(map(int, input_file.readline().strip().split())) for _ in range(3)]
    input_file.close()
    puzzle = Puzzle8(start)
    if puzzle.solvable():
        puzzle.search()
        output_file = open('out.txt', 'w')
        output_file.write('SEARCH ALGORITHM : ' + puzzle.search_algorithm + '\n')
        output_file.write('NUMBER OF MOVES : ' + str(len(puzzle.moves) - 1) + '\n')
        output_file.close()
        for move in puzzle.moves:
            puzzle.display_board(move)
    else:
        print('PUZZLE IS NOT SOLVABLE.')

if __name__ == '__main__':
    main()
