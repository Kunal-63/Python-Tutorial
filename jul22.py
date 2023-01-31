# Difference between a tuple & a list
"""
from time import time

t1 = time()
for i in range(100000):
    t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = time()
t = t2 - t1
"""
"""
import timeit

tuple_time = timeit.timeit(stmt="t1 = (1,2,3,4,5,6,7,8,9,10)", number=100000)
list_time = timeit.timeit(stmt="l1 = [1,2,3,4,5,6,7,8,9,10]", number=100000)
print("Tuple time:", tuple_time)
print("List time:", list_time)
"""
# Random module
"""
Let us tell sir that his voice is not coming

voice -> zsmgi

a + 4 = e
b + 4 = f
c + 4 = g
d + 4 = h
e + 4 = i
f

"""

# import random

# print(dir(random))
"""
for i in range(20):
    # print(random.random())      # [0, 1)
    print((random.random()*4) + 3)      # 3.0 to 6.99999
"""
"""
counter1=0
counter2=0
for i in range(10000):
    n = random.uniform(3, 7)
    if 3 <= n < 5:
        counter1 += 1
    else:
        counter2 += 1 
print("counter-1:", counter1)
print("counter-2:", counter2)
"""

# for i in range(20):
#     print(random.normalvariate(15, 0.5))
"""
for i in range(20):
    print(random.randint(1, 6))
    # print(random.randrange(1, 7))
"""
# option = ["stone", "paper", "scissors"]
"""
c1 = 0
c2 = 0
c3 = 0
for i in range(10000):
    c = random.choice(option)
    if c == "stone":
        c1 += 1
    elif c == "paper":
        c2 += 1
    else:
        c3 += 1
print("c1 =", c1)
print("c2 =", c2)
print("c3 =", c3)
"""

# Monte Carlo simulation
from random import choice

def random_walk(path_length):
    x = 0
    y = 0
    directions = ["N", "E", "W", "S"]

    for i in range(path_length):
        d = choice(directions)
        if d == "N":
            y += 1
        elif d == "S":
            y -= 1
        elif d == "W":
            x -= 1
        else:
            x += 1

    # print(f"x = {x}\ty = {y}")
    return (x, y)


# path_length = 9
print("Length\tProbability")
for path_length in range(7, 35):
    number_of_walks = 10000
    no_taxi = 0

    for j in range(number_of_walks):
        x, y = random_walk(path_length)
        d = abs(x) + abs(y)
        if d <= 5:
            no_taxi += 1
    probability = round(no_taxi/number_of_walks, 2)
    print(f"{path_length}\t{probability}")