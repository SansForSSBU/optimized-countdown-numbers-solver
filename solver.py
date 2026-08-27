from copy import deepcopy
import operator
operators = [operator.add, operator.sub, operator.mul, operator.floordiv]
op_str_lookup = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "*",
    operator.floordiv: "/"
}

class Calculation:
    def __init__(self, n1, op, n2):
        self.n1 = n1
        self.op = op
        self.n2 = n2

    def result(self):
        if self.op == operator.floordiv:
            if self.n1 % self.n2 != 0:
                return None
        ans = self.op(self.n1, self.n2)
        if ans <= 0:
            return None
        return ans

    def __str__(self):
        return f"{self.n1} {op_str_lookup[self.op]} {self.n2} = {self.result()}"

    def __repr__(self):
        return self.__str__()

class State:
    def __init__(self, numbers, target, calculations):
        self.numbers = numbers
        self.target = target
        self.calculations = calculations


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

numbers = [1, 2, 3, 4, 5, 6]
target = 200
state = State(numbers, target, [])
result = solve_puzzle(state)
if result:
    for calculation in result.calculations:
        print(calculation.__str__())
else:
    print("No solution found")