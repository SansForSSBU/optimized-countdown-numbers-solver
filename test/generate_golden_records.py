import json
from countdown.solver import solve_puzzle
from countdown.generator import generate_puzzle

num_examples = 100

def generate_and_solve_puzzle():
    puzzle = generate_puzzle()
    print(puzzle.numbers, puzzle.target)
    result = solve_puzzle(puzzle)
    return puzzle, abs(result.target - result.best)

if __name__ == "__main__":
    record = []
    for i in range(num_examples):
        puzzle, solvable = generate_and_solve_puzzle()
        print("Solvable to within: ", solvable)
        record_entry = {
            "Numbers": puzzle.numbers, 
            "Target": puzzle.target, 
            "Difference": solvable,
        }
        record.append(record_entry)

    with open("test_puzzles.json", "w") as f:
        json.dump(record, f)