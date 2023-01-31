s1 = "Happy Birthday to"
s2 = "Shubham!"
# print(s1 + " " + s2)
s1 = "happy birthday TO unknown!"
# Magical Methods/Dunder Method
"""
s3 = 15
s4 = 20
# print(s3 + s4)
s3.__add__(s4)
print(s3.__add__(s1))
s1.__add__(s2)
"""
# Case - related methods
"""
s2 = s1.capitalize()
s1 = s1.capitalize()
print(s1)   # strings are immutable.
print(s2)   
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())
print(s1.casefold())

s3 = "What is ß"
s4 = "what is ss"
print(s3.lower())
print(s3.casefold())
s5 = "Yash"
s6 = "yash"
"""
# Allignment - related methods
"""
print(len(s1))
s2 = s1.center(100)
print(len(s2))
print(s2)
print(s1.center(70, "."))

print(s1.ljust(150, "$"))
print(s1.rjust(110, "_"))
"""
s3 = "Students of this batch are going to rock the software industry. They are Bill Gates, Elon Musk and Steve Jobs of the future. They have potential to create another microsoft in India. But, some of them always keep their camera off."
"""
print(s3.count("e"))
print(s3.count("are"))
print(s3.count(" are "))
print(s3.count("are", 25))
print(s3.count("are", 25, 55))
"""
# print(s1.encode())
"""
print(s3.endswith("off."))
print(s3.endswith("off"))
print(s3.endswith(".", 100))
print(s3.endswith(".", 35, 60))

print(s3.startswith("T"))
print(s3.startswith("this", 12))
print(s3.startswith("this", 12, 50))
"""
"""
print("Sr.No.\t" + "Subject\tMarks".expandtabs(20))
print("1\t" + "Maths\t90".expandtabs(20))
print("2\t" + "C++\t95".expandtabs(20))
print("3\t" + "Computer Science\t86".expandtabs(20))
print("4\t" + "Chemistry\t98".expandtabs(20))
print("5\t" + "Social Science\t87".expandtabs(20))
"""
print(s1.find("b"))
a = s1.find("y")
print(a)
print(s1.find("y", a+1))
x1 = int(input("Enter start index: "))
x2 = int(input("Enter end index: "))
print(f"Index number of 'are' between {x1} and {x2}:", s3.find("are", x1, x2))

print(s1.index("b"))
a = s1.index("y")
print(a)
print(s1.index("y", a+1))
x1 = int(input("Enter start index: "))
x2 = int(input("Enter end index: "))
print(f"Index number of 'are' between {x1} and {x2}:", s3.index("are", x1, x2))

# Next Class: Methods starting from f