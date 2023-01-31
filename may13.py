# Collections in Python:
"""
Special Collection:
String: Collection of characters : Ordered and Immutable            :   " " or ' '
Dictionary: Collection of key:value pair : Unordered and Mutable    :   { }

Ordered     Mutable         List        [ ]
Ordered     Immutable       Tuple       ( )
Unordered   Mutable         Set         { }
Unordered   Immutable       Frozenset
"""
# Tuples: Ordered and Immutable collection of members
"""
Ordered means:
+ve and -ve Index numbers
Access elements by index numbers
Slicing is possible
"""
"""
t1 = (11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500)
print(t1)
print(type(t1))
l1 = list(t1)
# print(l1)
# name = "Harshil"
# t2 = tuple(name)
# print(t2)
t3 = ("Ahmedabad", "Mumbai", "Delhi", "Bangaluru", "Surat")

# creating a single element tuple
country = ("India",)
print("t3 =", t3)
print(country)
print(type(country))
total = (768.68,)
print(total)
print(type(total))

t4 = "Ahmedabad", "Mumbai", "Delhi", "Bangaluru", "Surat"
print(t4)
t5 = "Mumbai",
t6 = 500,

print(t4[2])
# t4[2] = "New Delhi"       tuples are immutable

# Modifying a tuple by hook or by crook
l4 = list(t4)
l4[2] = "New Delhi"
t4 = tuple(l4)
print(t4)

# slicing of a tuple:
print(t1[2:7])
print(sorted(t1))
"""
# Methods of tuple:
"""
t1 = (11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500)
print(t1.count(11))
# print(sum(t1))
# print(t1.count(11, 4))        Not valid in tuples
print(t1.index(-43))
print(t1.index(11, 6 , 9))
# print(t1.index(511, 6 , 9))
"""
# Unpacking of a collection/Multiple Assignment
"""
a = 10
b = 20
c = 30
a, b, c = 10, 20, 30
print("a =", a)
print("b =", b)
print("c =", c)
a, b, c = b, c, a
print("a =", a)
print("b =", b)
print("c =", c)
"""
# student_data = ("Arhaan", 19)
# name = student_data[0]
# age = student_data[1]
# gender = student_data[2]

# name, age, gender = student_data
# print(f"Name: {name}\nAge: {age}\nGender: {gender}")

# name, age, gender = student_data
"""
result = [
    [81, 72],
    [74, 85],
    [79, 68]
]
i = 1
for x, y in result:        # x, y = [81, 72]
    print(f"Student-{i} got {x} in maths and {y} in Computers and {z} in Python.")
    i += 1

student_data = ("Arhaan", 23, "Male", "US", "Drawing", "M.Tech")
name, age, *others = student_data
print(f"Name: {name}\nAge: {age}\nOther Details: {others}")

*data, hobby, qualification = student_data
print(f"Hobby: {hobby}\nQualification: {qualification}\nOther Details: {data}")

name, *info, hobby, qualification = student_data
print(f"Name: {name}\nQualification: {qualification}\nHobby: {hobby}\nOther Details: {info}")

student_data = ("Arhaan", 23, "Male", "US", "Drawing", "M.Tech", "MIT")
name, *info1, country, *info2, college = student_data         Error
"""
# Set: Unordered and Mutable collection of members in which repeatition is eliminated

s1 = {12, 34, 56, 78, 90}
print(s1)
print(type(s1))
"""
Unordered means:
order is not import
no index numbers
no -ve index
no slicing
no accessing through index
"""
# print(s1[2])
s1.add(100)
s1.add(34)
s1.add(56)
print(s1)

s2 = {55}
print(s2)
"""
s3 = {}
print(s3)
print(type(s3))

result = {"Physics":87, "Maths":92, "Python":99}
result = {}
"""
# creating an empty set
"""
s3 = set()
print(s3)
print(type(s3))
print(len(s3))

s4 = set([1,2,3,4])
print(s4)
"""
# Next Class: set methods, frozensets & dictionaries