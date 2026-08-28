from countdown.calculation import operators, commutative_operators, calculate, encode_calculation, decode_calculation
from countdown.state import State
import itertools
def solve_puzzle(numbers, target):
    if target in numbers:
        return (target, ())
    return solve_puzzle_recursive(numbers, target)

def solve_puzzle_recursive(numbers, target):
    best_num = 0
    best_steps = ()        
    for op_idx, op in enumerate(operators):
        if op in commutative_operators:
            space = itertools.combinations(enumerate(numbers), 2)
        else:
            space = itertools.permutations(enumerate(numbers), 2)
        for (idx1, n1), (idx2, n2) in space:
            new_num = calculate(n1, op_idx, n2)
            if new_num is None:
                continue
            if abs(target - new_num) < abs(target - best_num):
                best_num = new_num
                best_steps = (encode_calculation(idx1, op_idx, idx2),)
                if best_num == target:
                    return (best_num, best_steps)

            new_numbers = [n for idx, n in enumerate(numbers) if idx != idx1 and idx != idx2]
            new_numbers.append(new_num)
            (result_best_num, steps) = solve_puzzle_recursive(new_numbers, target)
            if abs(target - result_best_num) < abs(target - best_num):
                best_num = result_best_num
                best_steps = (encode_calculation(idx1, op_idx, idx2),) + steps
                if best_num == target:
                    return (best_num, best_steps)
    return (best_num, best_steps)