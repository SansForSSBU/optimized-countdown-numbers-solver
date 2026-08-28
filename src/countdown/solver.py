from countdown.calculation import operators, commutative_operators, calculate, encode_calculation, decode_calculation
from countdown.state import State
import itertools

def solve_puzzle(state, curr_best_num=None):
    state.recompute_best()
    if curr_best_num is None:
        best_num = 0
        for num in state.numbers:
            if abs(state.target - num) < abs(state.target - best_num):
                best_num = num
    else:
        best_num = curr_best_num
    best_state = state
    best_steps = ()
    if state.target in state.numbers:
        return (state, ())
    for op_idx, op in enumerate(operators):
        if op in commutative_operators:
            space = itertools.combinations(enumerate(state.numbers), 2)
        else:
            space = itertools.permutations(enumerate(state.numbers), 2)
        for (idx1, n1), (idx2, n2) in space:
            new_num = calculate(n1, op_idx, n2)
            step = encode_calculation(idx1, op_idx, idx2)
            if new_num is None:
                continue
            new_numbers = [n for idx, n in enumerate(state.numbers) if idx != idx1 and idx != idx2]
            new_numbers.append(new_num)
            new_state = State(new_numbers, state.target)
            new_state.recompute_best()
            if new_num == state.target:
                return (new_state, (step,))
            (result, steps) = solve_puzzle(new_state, curr_best_num=best_num)
            if result.best == result.target:
                return (result, (step,) + steps)
            if abs(result.target - result.best) < abs(best_state.target - best_state.best):
                best_state = result
                best_steps = (step,) + steps
    return (best_state, best_steps)