from python.src.state import State
import random
large_numbers = [25, 50, 75, 100]
small_numbers = list(range(1, 11))*2
target_numbers = list(range(100, 1000))

def generate_puzzle(num_large=None):
    if num_large is None:
        num_large = random.randint(0, 4)

    if num_large < 0 or num_large > 4:
        raise ValueError

    num_small = 6 - num_large
    numbers = []
    numbers.extend(random.sample(large_numbers, num_large))
    numbers.extend(random.sample(small_numbers, num_small))
    target = random.choice(target_numbers)
    puzzle = State(numbers, target)
    return puzzle