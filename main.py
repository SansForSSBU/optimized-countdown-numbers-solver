from python.src.solver import solve_puzzle
from python.src.generator import generate_puzzle

def generate_and_solve_puzzle():
    puzzle = generate_puzzle()
    print(puzzle.numbers, puzzle.target)
    result = solve_puzzle(puzzle)
    if result:
        for calculation in result.calculations:
            print(calculation.__str__())
    else:
        print("No solution found")
        return False
    return True

if __name__ == "__main__":
    puzzles_solved = 0
    while True:
        print("Puzzles solved", puzzles_solved)
        found_solution = generate_and_solve_puzzle()
        if found_solution:
            puzzles_solved += 1