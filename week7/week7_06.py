import itertools
import random

iter_binary = itertools.cycle([0, 1])
iter_directions = iter((lambda: random.choice(("N", "E", "S", "W"))), 1)
iter_days = itertools.cycle([x for x in range(7)])

list_binary, list_directions, list_days = [], [], []
for i in range(10):
    list_binary.append(next(iter_binary))
    list_directions.append(next(iter_directions))
    list_days.append(next(iter_days))

print(f"Binary: {list_binary}")
print(f"Directions: {list_directions}")
print(f"Days: {list_days}")