"""
a = 10
b = 20
c = 30
print("Before:")
print("a =", a, "\nb =", b, "\nc =", c)
a, b, c = b, c, a
print("After:")
print("a =", a, "\nb =", b, "\nc =", c)
"""
"""
5. Assignment Operators
    = 
        x = 5
        x = a + b
    
    a = a + b   =>  a += b
    a = a - b   =>  a -= b
    a = a * b   =>  a *= b
    a = a / b   =>  a /= b
    a = a % b   =>  a %= b
    a = a // b   =>  a //= b
    a = a ** b   =>  a **= b
    a = a & b   =>  a &= b
    a = a | b   =>  a |= b
    a = a ^ b   =>  a ^= b
    a = a << b   =>  a <<= b
    a = a >> b   =>  a >>= b

    # There is nothing like i++/i-- in Python, we've to use i += 1 instead

6. Identity operators
    is
    is not

7. Membership Operators
    in
    not in
"""
"""
a = [1,2,3,4]
b = a
c = a.copy()
# print(a is b)
# print(a == c)
# print(a is c)
# print(6 in a)
# print(7 not in a)
print(3 in a)
"""
"""
myString = "Net is down."
print("s" in myString)
print("Net" in myString)
"""
# Decision Making: if-else
"""
if (a < b)
{
    //code line 1
    //code line 2
    // code line 3
}
// code line 4

"""
"""
a = int(input("Enter a number: "))
if a > 0:
    print(f"{a} is positive.")
    a += 1
    print(a)
elif a == 0:
    print(f"It's zero.")
else:
    print(f"{a} is negative.")

print("Thanks!")
"""
# shorthand if
"""
a = int(input("Enter a number: "))
if a > 0: print(f"{a} is positive.")
"""
# shorthand if-else
"""
a = int(input("Enter a number: "))
print("positive") if a > 0 else print("negative")
"""
# shorthand if-elif-else does not exist.

# Loops in Python: while, for
"""
We use loops if and only if we want to execute some instructions multiple times.
We put those and only those instructions inside the loop which we want to execute multiple times.
"""
# write a Python code to print multiplicative table of a given number.
"""
a = float(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{a} x {i} = {a * i}")
    i += 1
"""
# print(2500/365)
# print(round(2500/365, 3))
# print(round(2500/365, 2))

# infinite loops:
print("Enter two integers:")
a = int(input())
b = int(input())
while True:
    choice = input("What do you want to do? +, -, * or / ?\n")
    if choice == "+":
        print(f"{a} + {b} = {a+b}")
    elif choice == "-":
        print(f"{a} - {b} = {a-b}")
    elif choice == "*":
        print(f"{a} * {b} = {a*b}")
    elif choice == "/":
        print(f"{a} / {b} = {a/b}")
    else:
        print("Invalid operation, please try again...")
    quit = input("Press 'q' to quit, any other key to repeat: ").lower()
    if quit == "q":
        break

"""
False for Python:
False, 0, 0.0, "", [], (), set(), {}
"""
# Next Class: for loop, pass, break, continue statement