# a
trials = 1

r1 = 12
r2 = 12

t = r1 * r2

c = 0

for i in range(1, r1):
    c += i

print(c / t)


# b

import random


def simulation(trials):
    c = 0
    for _ in range(trials):
        first = random.randint(1, 12)
        second = random.randint(1, 12)
        if second > first:
            c += 1
    return c / trials


print(simulation(100))
