from countdown.calculation import operators, commutative_operators, calculate, encode_calculation, decode_calculation
from countdown.state import State
import itertools

def solve_puzzle(state):
    state.recompute_best()
    best_state = state
    if state.target in state.numbers:
        return state
    for op_idx, op in enumerate(operators):
        if op in commutative_operators:
            space = itertools.combinations(enumerate(state.numbers), 2)
        else:
            space = itertools.permutations(enumerate(state.numbers), 2)
        for (idx1, n1), (idx2, n2) in space:
            new_num = calculate(n1, op_idx, n2)
            calc = encode_calculation(idx1, op_idx, idx2)
            if new_num is None:
                continue
            new_numbers = [n for idx, n in enumerate(state.numbers) if idx != idx1 and idx != idx2]
            new_numbers.append(new_num)
            new_calculations = state.calculations + (calc,)
            new_state = State(new_numbers, state.target, new_calculations)
            new_state.recompute_best()
            if new_num == state.target:
                return new_state
            result = solve_puzzle(new_state)
            if result.best == result.target:
                return result
            if abs(result.target - result.best) < abs(best_state.target - best_state.best):
                best_state = result
    return best_state