from python.src.solver import solve_puzzle
from python.src.generator import generate_puzzle

puzzle = generate_puzzle()
print(puzzle.numbers, puzzle.target)
result = solve_puzzle(puzzle)
if result:
    for calculation in result.calculations:
        print(calculation.__str__())
else:
    print("No solution found")