import json
import time
from countdown.solver import solve_puzzle
from countdown.state import State
from countdown.calculation import Calculation

def test_countdown_puzzles():
    puzzle_times = {}
    with open("test/puzzles.json", "r") as f:
        records = json.load(f)
        for idx, r in enumerate(records):
            numbers = r["Numbers"]
            target = r["Target"]
            difference = r["Difference"]
            puzzle = State(numbers, target)
            before = time.time()
            best_num, steps = solve_puzzle(puzzle)
            after = time.time()
            elapsed = after - before
            puzzle_times[idx] = elapsed
            calculations = [Calculation.from_encoded(step) for step in steps]
            puzzle.show_working(calculations)
            print(f"Puzzle number {idx} took {elapsed} seconds")
            #assert difference == abs(solution.target - solution.best)
    with open("performance_logs/results.json", "w") as f:
        json.dump(puzzle_times, f)

if __name__ == "__main__":
    test_countdown_puzzles()