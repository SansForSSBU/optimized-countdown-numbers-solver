import json
from countdown.solver import solve_puzzle
from countdown.generator import generate_puzzle

num_examples = 100

def generate_and_solve_puzzle():
    puzzle = generate_puzzle()
    print(puzzle.numbers, puzzle.target)
    result = solve_puzzle(puzzle)
    if result:
        for calculation in result.calculations:
            print(calculation.__str__())
    else:
        print("No solution found")
        return puzzle, False
    return puzzle, True

if __name__ == "__main__":
    record = []
    for i in range(num_examples):
        puzzle, solvable = generate_and_solve_puzzle()
        record_entry = {
            "Numbers": puzzle.numbers, 
            "Target": puzzle.target, 
            "Solvable": solvable,
        }
        record.append(record_entry)

    with open("test_puzzles.json", "w") as f:
        json.dump(record, f)