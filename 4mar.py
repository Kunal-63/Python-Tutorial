"""
1. Write a Python program that takes 5 integers from user and prints their average. The output MUST BE EXACTLY as given in example:
example:
Enter 5 integers:
2
3
4
5
6
Output:
The average of 2, 3, 4, 5 and 6 is: 4.0
"""
"""
print("Enter 5 integers:")
a  = int(input())
b  = int(input())
c  = int(input())
d  = int(input())
e  = int(input())
avg = (a + b + c + d + e)/5
# f-string
print(f"The average of {a}, {b}, {c}, {d} and {e} is: {avg}")
"""

# print("Faizan,Chundarigar")
"""
i = 1
a = int(input(f"Enter number - {i}: "))
i = i + 1
"""
# There is NO "char" datatype in Python.
# string data type (str)

# string: Ordered and Immutable collection of characters
a = "You all are invited to our grand opening at Gandhinagar."
"""
print(a)
print(type(a))
b = 	"Welcome to Royal."
# index: 0123456789.......
#-ve in:-........987654321

print(b[15])
# print(b[150])
print(b[-6])
print(b[11])

print(b[0])
# slicing
c = a[5 : 25]
print(a)	# slicing never changes the original data.
print(c)
print(a[10 : 30])
print(a[10])
print(a[30])

print(a[-40 : -5])
print(a[12 : 350])
print(b[-3 : -12])
print("Don't type anything in chat.")
d = ""
print(a[4 : -3])
print(len(a))

print(a[4:50:2])
print("Good Night")

print(a[5 : ])
print(a[ : -5])
print(a[ : ])
print(a[5 : -5 : 1])
print(a[5 : -5 : ])

print(a[-5 : 5 : -1])
print(a[ : : -1])
print(a[ : : -3])
print(a[-5 : 5 : -2])
"""

# difference between methods and functions
a = "You all are invited to our grand opening at Gandhinagar."
len(a)
print(a.lower())

