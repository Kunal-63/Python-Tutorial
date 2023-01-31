"""
7. Write a Python function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and prints all the Prime numbers between those two integers using that function.

8. Write a Python function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.
"""
"""
def primeCheck(n):
    if n == 1: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

print("Enter two integers:")
a = int(input())
b = int(input())
print(f"Prime numbers between {a} and {b} are:")
for x in range(a, b+1):
    if primeCheck(x):
        print(x, end="\t")
"""
# 30 : 1, 2, 3, 5, 6, 10, 15,
# 1000000039
# 2 till 10000000038
"""
641
Method - 1 : 2 to 640
Method - 2 : 2 to 321
Method - 3 : 2 to 26
"""
"""
def armstrong(n):           # n = 153
    power = len(str(n))
    sum = 0
    for x in str(n):        # str(n) = "153"; x = "1", "5", "3"
        sum = sum + int(x) ** power
    if sum == n:
        return True
    else:
        return False
"""
"""
def armstrong(n):           # n = 153
    # digits = [int(x)**len(str(n)) for x in str(n)]
    return (True if sum([int(x)**len(str(n)) for x in str(n)]) == n else False)

armstrong(154)
"""
# Built in functions
# round()
"""
number = float(input("Enter any number: "))
print(round(number, 2))
print(round(number, 3))
print(round(number, 0))
print(round(number))
"""
# sum()
"""
print(sum(range(5, 15)))
# print(sum(5,6,7,8))
print(sum([5,6,7,8,9,10], 100))
"""
# zip()
"""
from sys import getsizeof


l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
# print(dict(zip(l1, l2)))
# for x, y in list(zip(l1, l2)):
#     print(f"{x}\t{y}")

obj = zip(l1, l2)
list_of_obj = list(zip(l1, l2))
print("size of object:", getsizeof(obj))
print("size of list:", getsizeof(list_of_obj))
"""
"""
from sys import getsizeof

l1 = [x for x in range(100)]
t1 = tuple(l1)
print("size of l1:", getsizeof(l1))
print("size of t1:", getsizeof(t1))
"""
"""
We type () after a function only when we want to call it.
"""
# Deleting & Copying a function:
"""
def primeCheck(n):
    if n == 1: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

# print(primeCheck(177))
isPrime = primeCheck
del primeCheck
# primeCheck(5)
print(isPrime(5))
"""
# map
"""
def cube(n):
    return n**3

numbers = [1,2,3,4,5,6,7,8,9,10]
cubes = list(map(cube, numbers))
print(cubes)
"""
# map function in detail, filter, reduce, lambda functions, recursive functions