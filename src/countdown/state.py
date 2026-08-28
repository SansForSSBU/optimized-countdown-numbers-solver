class State:
    def __init__(self, numbers, target, calculations=None):
        self.numbers = numbers
        self.target = target
        self.best = None
        if calculations is not None:
            self.calculations = calculations
        else:
            self.calculations = ()

    def recompute_best(self):
        self.best = 0
        for num in self.numbers:
            self._update_best(num)

    def show_working(self, calcs):
        numbers = list(self.numbers)
        for calc in calcs:
            calc.print(numbers)
            result = calc.get_result(numbers)
            for idx in sorted([calc.n1_idx, calc.n2_idx], reverse=True):
                numbers.pop(idx)
            numbers.append(result)

    def _update_best(self, new_num):
        if abs(self.target - self.best) > abs(self.target - new_num):
            self.best = new_num