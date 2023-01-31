# def funcky(a, b, c = 10, d = 20, *args):
#     print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}\nargs = {args}")

# funcky(2, 3, 5, 7, 8, 9, Maths = 78, Physics = 94)
"""
def percentage(**kwargs):
    # print(kwargs)
    return sum(kwargs.values())/len(kwargs)


print(percentage(Maths = 78, Physics = 94, Computers = 100))
"""
# Common Mistakes:
# percentage(Maths : 78, Physics : 94, Computers : 100)
# percentage("Maths" = 78, "Physics" = 94, "Computers" = 100)
# percentage(1 = 75, 2 = 88, 3 = 45)

# maths_1 = 78
# maths2 = 94
# 3maths = 98

# Passing a dictionary to a function:
"""
def percentage(marks):
    return sum(marks.values())/len(marks)

result = {"Maths" : 78, "Physics" : 94, "Computers" : 100}
print("Percentage =", percentage(result))
"""
# Rule of Order: First Comes ALL POSITIONAL ARGUMENTS, then comes ALL DEFAULT ARGUMENTS, then comes args and finally comes kwargs

"""
a = 15
b = 37
c = 15
c += 1
d = 16
"""
# Organizing our code in modules and packages

# Mummy = import
"""
import important_functions

print(important_functions.factorial(6))
"""
"""
import important_functions as imp

print(imp.armstrong(257))
"""
# some examples:
"""
import speech_recognition as sr
import numpy as np
import pandas as pd
"""
"""
from important_functions import primeCheck as pc, armstrong as arm, avg

# print(primeCheck(97))
# print(armstrong(371))
print(pc(1377549))
print(arm(1377549))
"""
"""
import important_functions

print(dir(important_functions))
"""
"""
from important_functions import *

print(primeCheck(1017))
"""

# Packages

# Wrong way to import something from a package
"""
import myPackage

myPackage.myModule.myFunc()
"""
"""
from myPackage import myModule

myModule.myFunc()
"""
"""
from myPackage.myModule import myFunc

myFunc()
"""
"""
from myPackage.subPackage import subModule

subModule.subFunc()
"""
"""
from myPackage.subPackage.subModule import subFunc

subFunc()
"""

# Next Class: Very important built in modules