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