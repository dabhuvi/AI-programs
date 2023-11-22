from itertools import permutations

def is_valid_assignment(letters, assignment, equation):
    translated_equation = equation.translate(str.maketrans(letters, assignment))
    return eval(translated_equation)

def solve_cryptarithmetic(equation):
    unique_letters = set(char for char in equation if char.isalpha())
    if len(unique_letters) > 10:
        print("Invalid equation. Too many unique letters.")
        return

    letters = ''.join(unique_letters)
    digits = '0123456789'
    valid_assignments = []

    for perm in permutations(digits, len(unique_letters)):
        assignment = dict(zip(letters, perm))

        if assignment[letters[0]] == '0':
            continue  

        if is_valid_assignment(letters, assignment, equation):
            valid_assignments.append(assignment)

    return valid_assignments

if __name__ == "__main__":

    equation = "SEND + MORE == MONEY"

    solutions = solve_cryptarithmetic(equation)

    if solutions:
        print("Solutions found:")
        for solution in solutions:
            print(solution)
    else:
        print("No solution found.")
