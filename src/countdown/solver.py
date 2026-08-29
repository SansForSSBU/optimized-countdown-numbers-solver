from countdown.calculation import operators, commutative_operators, calculate, encode_calculation, decode_calculation
from countdown.state import State
import itertools
import functools

def solve_puzzle(numbers, target):
    if target in numbers:
        return (target, ())
    best_num1, best_steps1 = solve_puzzle_bfs(tuple(sorted(numbers)), target)
    #best_num2, best_steps2 = solve_puzzle_recursive(tuple(sorted(numbers)), target)
    return best_num1, best_steps1

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

            new_numbers = tuple(n for idx, n in enumerate(numbers) if idx != idx1 and idx != idx2) + (new_num,)
            (result_best_num, steps) = solve_puzzle_recursive(new_numbers, target)
            if abs(target - result_best_num) < abs(target - best_num):
                best_num = result_best_num
                best_steps = (encode_calculation(idx1, op_idx, idx2),) + steps
                if best_num == target:
                    return (best_num, best_steps)
    return (best_num, best_steps)

def get_next_states(numbers, instructions):
    next_states = {} # lookup: state -> instructions
    numbers_made = {} # lookup: number -> instructions
    for op_idx, op in enumerate(operators):
        if op in commutative_operators:
            space = itertools.combinations(enumerate(numbers), 2)
        else:
            space = itertools.permutations(enumerate(numbers), 2)
        for (idx1, n1), (idx2, n2) in space:
            instruction = encode_calculation(idx1, op_idx, idx2)
            new_num = calculate(n1, op_idx, n2)
            if new_num is None:
                continue
            new_numbers = tuple(n for idx, n in enumerate(numbers) if idx != idx1 and idx != idx2) + (new_num,)
            next_states[(tuple(sorted(new_numbers)))] = instructions + (instruction, )
            numbers_made[new_num] = instructions + (instruction, )
    return next_states, numbers_made

def solve_puzzle_bfs(numbers, target):
    states = {numbers: tuple()}
    numbers_found = {}
    for i in range(len(numbers) - 1):
        next_states = {}
        for state, instructions in states.items():
            new_states, new_numbers = get_next_states(state, instructions)
            next_states.update(new_states)
            if target in new_numbers.keys():
                return target, new_numbers[target]
            next_states.update(next_states)
            numbers_found.update(new_numbers)
        states = next_states
    for num_away in range(1, 999):
        nums_to_check = [target - num_away, target + num_away]
        for num in nums_to_check:
            if num in numbers_found.keys():
                return num, numbers_found[num]