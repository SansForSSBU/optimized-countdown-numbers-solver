import json
import time
from countdown.solver import solve_puzzle
from countdown.state import State

def test_countdown_puzzles():
    puzzle_times = {}
    with open("test/puzzles.json", "r") as f:
        records = json.load(f)
        for idx, r in enumerate(records):
            numbers = r["Numbers"]
            target = r["Target"]
            solvable = r["Solvable"]
            puzzle = State(numbers, target)
            before = time.time()
            solution = solve_puzzle(puzzle)
            after = time.time()
            elapsed = after - before
            puzzle_times[idx] = elapsed
            print(f"Puzzle number {idx} took {elapsed} seconds")
            solved = solution is not False
            assert solvable == solved
    with open("results.json", "w") as f:
        json.dump(puzzle_times, f)