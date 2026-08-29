import operator

commutative_operators = [operator.add, operator.mul]
operators = [operator.add, operator.sub, operator.mul, operator.floordiv]
op_str_lookup = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "*",
    operator.floordiv: "/"
}

# TODO: We should instead encode calculations in 1-byte.
# First 3 bits should be idx1.
# Second 3 bits should be idx2.
# Third 2 bits should be operator.

def calculate(n1, op_idx, n2):
    if operators[op_idx] == operator.floordiv:
        if n1 % n2 != 0:
            return None
    ans = operators[op_idx](n1, n2)
    if ans <= 0:
        return None
    return ans

def encode_calculation(n1_idx, op_idx, n2_idx):
    # Encodes the calculation into one byte. Assumes n1_idx between 0-7, n2_idx between 0-7 and op_idx between 0-3
    return ((n1_idx & 0x7) << 5) | ((n2_idx & 0x7) << 2) | (op_idx & 0x3)

def decode_calculation(encoded_calculation):
    n1_idx = (encoded_calculation >> 5) & 0x7
    n2_idx = (encoded_calculation >> 2) & 0x7
    op_idx = encoded_calculation & 0x3
    return n1_idx, op_idx, n2_idx

class Calculation:
    def __init__(self, n1_idx, op_idx, n2_idx):
        self.n1_idx = n1_idx
        self.op_idx = op_idx
        self.n2_idx = n2_idx

    def from_encoded(encoded):
        n1_idx, op_idx, n2_idx = decode_calculation(encoded)
        return Calculation(n1_idx, op_idx, n2_idx)

    def get_result(self, numbers_arr):
        return calculate(numbers_arr[self.n1_idx], self.op_idx, numbers_arr[self.n2_idx])

    def print(self, numbers_arr):
        print(f"{numbers_arr[self.n1_idx]} {op_str_lookup[operators[self.op_idx]]} {numbers_arr[self.n2_idx]} = {self.get_result(numbers_arr)}")