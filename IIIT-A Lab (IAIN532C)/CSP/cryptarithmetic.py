def convert_to_number(string, mapping):
    '''CONVERTS STRING TO NUMERICAL FORM'''
    return sum((10 ** i) * mapping[string[-i - 1]] for i in range(len(string)))

def is_solvable(a, b, c, mapping):
    '''CHECKS IF THE CURRENT MAPPING IS IN A SOLVABLE CONFIGURATION'''
    return convert_to_number(a, mapping) + convert_to_number(b, mapping) == convert_to_number(c, mapping)

def backtrack(a, b, c, unique_characters, mapping, digit_count, index):
    '''BACKTRACKING CSP SOLVER'''
    if index == len(unique_characters):
        return is_solvable(a, b, c, mapping)
    for digit in range(10):
        if digit_count[digit] == 0:
            digit_count[digit] += 1
            mapping[unique_characters[index]] = digit
            if backtrack(a, b, c, unique_characters, mapping, digit_count, index + 1):
                return True
            digit_count[digit] = 0
            mapping[unique_characters[index]] = None

def main():
    '''MAIN FUNCTION'''
    a, b, c = input().strip().split()
    unique_characters = set(list(a + b + c))
    mapping = dict((character, None) for character in unique_characters)
    if backtrack(a, b, c, ''.join(list(unique_characters)), mapping, [0 for _ in range(10)], 0):
        print(mapping)
    else:
        print('NO SOLUTION')

if __name__ == '__main__':
    main()
