"""
1. Perfect number check
30 : 1, 2, 3, 5, 6, 10, 15 = 42
28 : 1, 2, 4, 7, 14 = 28 
"""
"""
n = int(input("Enter any positive integer: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
# factors = []
# for i in range(1, n):
#     if n % i == 0:
#         factors.append(i)
# factors = [i for i in range(1, n) if n % i == 0]
print("Perfect.") if sum([i for i in range(1, n) if n % i == 0]) == n else print("Not Perfect.")
"""
# Find inverse of a nxn matrix using Gauss Jordan Method in C
# Multiple Assignment/Unpacking of collections using for loop
# 3 x 3 matrix using lists:
"""
result = [
    [81, 72],
    [74, 85],
    [79, 68]
]
i = 1
for x, y in result:        # x = 81, y = 72; x = 74, y = 85; x = 79, y = 68
    print(f"student-{i} got {x} in C and {y} in Python.")
    i += 1
"""
"""
result = [
    [81, 72, 93],
    [74, 85, 69],
    [79, 68, 90]
]
i = 1
for x, y, z in result:        # x = 81, y = 72; x = 74, y = 85; x = 79, y = 68
    print(f"student-{i} got {x} in C, {y} in Python and {z} in java.")
    i += 1
"""
# List comprehension
"""
numbers = []
for i in range(1, 101):
    numbers.append(i)
"""
# numbers = [i for i in range(1, 101)]
# print(numbers)
# set theory:
"""
Set builder form:
set = {x / 1 <= x <= 100}
"""
# Armstron number check
"""
1358 - 4 digit
1 ^ 4 = 1
3 ^ 4 = 81
5 ^ 4 = 625
8 ^ 4 = 4096
------------
      = 1358

1. count number of digits
2. sum of powers of each digit
"""
"""
n = int(input("Enter any positive integer: "))      # 1358
temp = n
power = 0
while temp > 0:
    temp = temp//10      # 135, 13, 1,  0
    power += 1           # 1,   2,  3,  4
temp = n
sum = 0
while temp > 0:
    digit = temp % 10       # 8
    sum = sum + digit ** power
    temp = temp//10
if sum == n:
    print("Armstrong.")
else:
    print("Not Armstrong.")
"""
"""
     35
   ______
10 | 357
    -350
    -----
       7


"""
"""
n = int(input("Enter any positive integer: "))      # 1358
# power = len(str(n))
# digits = []
# for x in str(n):
#     digits.append(int(x) ** power)
# digits = [int(x)**power for x in str(n)]
print("Armstrong") if sum([int(x)**len(str(n)) for x in str(n)]) == n else print("Not Armstrong")
"""
# Next Class: tuples, unpacking of collections/multiple assignment, sets, frozensets