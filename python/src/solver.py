from copy import deepcopy
from python.src.calculation import operators, Calculation
from python.src.state import State

def solve_puzzle(state):
    for idx1, n1 in enumerate(state.numbers):
        for idx2, n2 in enumerate(state.numbers):
            if idx1 == idx2:
                continue
            for op in operators:
                calc = Calculation(n1, op, n2)
                new_num = calc.result()
                if new_num is None:
                    continue
                new_numbers = [n for idx, n in enumerate(state.numbers) if idx not in [idx1, idx2]]
                new_numbers.append(new_num)
                new_calculations = deepcopy(state.calculations)
                new_calculations.append(calc)
                new_state = State(new_numbers, state.target, new_calculations)
                if new_num == state.target:
                    return new_state
                result = solve_puzzle(new_state)
                if result:
                    return result
    return False