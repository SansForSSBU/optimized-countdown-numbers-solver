from copy import deepcopy
from countdown.calculation import operators, commutative_operators, Calculation
from countdown.state import State

def solve_puzzle(state):
    state.recompute_best()
    best_state = state
    if state.target in state.numbers:
        return state
    for idx1, n1 in enumerate(state.numbers):
        for idx2, n2 in enumerate(state.numbers):
            if idx1 == idx2:
                continue
            for op in operators:
                if op in commutative_operators and idx1 > idx2:
                    continue
                calc = Calculation(n1, op, n2)
                new_num = calc.result()
                if new_num is None:
                    continue
                new_numbers = [n for idx, n in enumerate(state.numbers) if idx not in [idx1, idx2]]
                new_numbers.append(new_num)
                new_calculations = deepcopy(state.calculations)
                new_calculations.append(calc)
                new_state = State(new_numbers, state.target, new_calculations)
                new_state.recompute_best()
                if new_num == state.target:
                    return new_state
                result = solve_puzzle(new_state)
                if result.best == result.target:
                    return result
                if abs(result.target - result.best) < (best_state.target - best_state.best):
                    best_state = result
    return best_state