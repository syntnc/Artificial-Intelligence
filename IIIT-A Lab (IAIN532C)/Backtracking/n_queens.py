BOARD_SIZE = 8

def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens) - i for i, x in enumerate(queens))

def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = (solution + [i+1]
                     for solution in solutions
                     for i in range(BOARD_SIZE)
                     if not under_attack(i+1, solution))
    return solutions

def main():
    answers = solve(BOARD_SIZE)
    #first_answer = next(answers)
    for answer in answers:
        print(list(enumerate(answer, start=1)))

if __name__ == '__main__':
    main()
