from python.src.solver import solve_puzzle
from python.src.state import State

numbers = [1, 2, 3, 4, 5, 6]
target = 200
state = State(numbers, target, [])
result = solve_puzzle(state)
if result:
    for calculation in result.calculations:
        print(calculation.__str__())
else:
    print("No solution found")