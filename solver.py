from copy import deepcopy
import operator
operators = [operator.add, operator.sub, operator.mul, operator.floordiv]

def solve_puzzle(numbers, target):
    state = numbers
    for idx1, n1 in enumerate(state):
        for idx2, n2 in enumerate(state):
            if idx1 == idx2:
                continue
            for op in operators:
                if op == operator.floordiv:
                    if n1 % n2 != 0:
                        continue
                new_num = op(n1, n2)
                if new_num <= 0:
                    continue
                if new_num == target:
                    return True
                new_state = [n for idx, n in enumerate(state) if idx not in [idx1, idx2]]
                new_state.append(new_num)
                if solve_puzzle(new_state, target):
                    return True
    return False

numbers = [1, 2, 3, 4, 5, 6]
target = 200
print(solve_puzzle(numbers, target))