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
    best_steps = ()
    if state.target in state.numbers:
        return (state.target, ())
    for op_idx, op in enumerate(operators):
        if op in commutative_operators:
            space = itertools.combinations(enumerate(state.numbers), 2)
        else:
            space = itertools.permutations(enumerate(state.numbers), 2)
        for (idx1, n1), (idx2, n2) in space:
            new_num = calculate(n1, op_idx, n2)
            if new_num is None:
                continue
            new_numbers = [n for idx, n in enumerate(state.numbers) if idx != idx1 and idx != idx2]
            new_numbers.append(new_num)
            if new_num == state.target:
                return (new_num, (encode_calculation(idx1, op_idx, idx2),))
            if abs(state.target - new_num) < abs(state.target - best_num):
                best_num = new_num
                best_steps = ()
            (result_best_num, steps) = solve_puzzle(State(new_numbers, state.target), curr_best_num=best_num)
            if result_best_num == state.target:
                return (result_best_num, (encode_calculation(idx1, op_idx, idx2),) + steps)
            if abs(state.target - result_best_num) < abs(state.target - best_num):
                best_num = result_best_num
                best_steps = (encode_calculation(idx1, op_idx, idx2),) + steps
    return (best_num, best_steps)