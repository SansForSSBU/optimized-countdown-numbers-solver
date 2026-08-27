class State:
    def __init__(self, numbers, target, calculations=None):
        self.numbers = numbers
        self.target = target
        if calculations is not None:
            self.calculations = calculations
        else:
            self.calculations = []