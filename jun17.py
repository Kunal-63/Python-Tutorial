"""
def cube(n):
    return n**3

numbers = [1,2,3,4,5,6,7,8,9,10]
# cubes = [cube(x) for x in numbers]
# cubes = []
# for x in numbers:
#     cubes.append(cube(x))

cubes = list(map(cube, numbers))
"""
# filter
# filter(function, collection)
"""
def output(x):
    # return (True if x > avg else False)
    if x >= avg:
        return False
    else:
        return True

sensor_data = [1.5, 2.5, 5.9, 3.5, 34.2, -5.7, 12.8, 44.6, 20.1]
avg = sum(sensor_data)/len(sensor_data)
print("Average =", avg)
print(list(filter(output, sensor_data)))
"""
# reduce
"""
Write a program to multiply all the members of a list.
"""
# myList = [1.5, 2.5, 5.9, 3.5, 34.2, -5.7, 12.8, 44.6, 20.1]
# temp = 1
# for x in myList:
#     temp = temp * x
# print(temp)

# reduce(function, collection)
"""
from functools import reduce

def mul(a, b):
    return a * b

myList = [2,3,4,3,2]
print(reduce(mul, myList))

print(mul(mul(mul(mul(2,3), 4), 3), 2))
"""
# lambda functions/Anonymous functions/In-line functions
# def cube(n):
#     return n**3
"""
cube = lambda n : n ** 3
mul = lambda a, b : a * b

print(cube(5))
print(mul(3,6))

numbers = [1,2,3,4,5,6,7,8,9,10]
print(tuple(map(lambda n : n**3, numbers)))

sensor_data = [1.5, 2.5, 5.9, 3.5, 34.2, -5.7, 12.8, 44.6, 20.1]
avg = sum(sensor_data)/len(sensor_data)
print(tuple(filter(lambda n : True if n >= avg else False, sensor_data)))
"""

# Nesting of functions & scope:
"""
# def avg_of_fact(p,q,r,s,t):
#     def fact(n):
#         f = 1
#         for x in range(1, n+1):
#             f = f * x
#         return f
#     sum = fact(p) + fact(q) + fact(r) + fact(s) + fact(t)
#     return sum/5

def avg(p,q,r,s,t):
    return (p+q+r+s+t)/5

def fact(n):
    f = 1
    for x in range(1, n+1):
        f = f * x
    return f


print("Enter 5 numbers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
# print("Average of their factorials =", avg_of_fact(a,b,c,d,e))
print("Average of their factorials =", avg(fact(a), fact(b), fact(c), fact(d), fact(e)))
"""

# scope of a variable, global variables, local variables and global keyword:
"""
a = 10              # global variable
d = 40

def func1():
    global d, a
    a -= 1
    print("'a' through func1 =", a)
    c = 30          # local variable of func1
    print("'c' through func1 =", c)
    def func3():
        print("'c' through func3 =", c)
    func3()
    # d = 50
    d += 1
    print("'d' through func1 =", d)


def func2():
    print("'b' through func2 =", b)
    # print("'c' through func2 =", c)


print("'a' through main =", a)
func1()
b = 20              # can be used by all the functions those are CALLED after this point
func2()
# print("'c' through main =", c)
print("'d' through main =", d)
"""

# Next Class: Recursive Function, positional arguments, default arguments, variable length arguments, keyword arguments