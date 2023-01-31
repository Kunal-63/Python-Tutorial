# a = 98 
# b = 77

"""
a : 98 : 0110 0010
b : 77 : 0100 1101
a : ^  : 0010 1111

a :    : 0010 1111
b : 77 : 0100 1101
b : ^  : 0110 0010

a :    : 0010 1111
b :    : 0110 0010
a : ^  : 0100 1101
"""
# a = a^b
# b = a^b
# a = a^b

# for loop

# fruits = ["banana", "apple", "mango", "orange", "grapes", "kiwi", "guava", "sapota"]
"""
i = 0
while i < len(fruits):      # i = 0, 1, 2, 3, 4, 5, 6, 7
    print(fruits[i])
    i += 1
"""
# for i in fruits:        # i = "banana", "apple", "mango", "orange", "grapes", "kiwi", "guava", "sapota"
#     print(i)
"""
for fruit in fruits:
    if fruit == "orange":
        # break
        # continue
        pass
    print(fruit)
print("Thanks!")
"""
"""
choice = int(input("Enter Choice: "))
if choice == 1:
    print("Your balance")
elif choice == 2:
    print("Your Due")
elif choice == 3:
    print("Loan emi")
elif choice == 4:
    print("Interest amount")
elif choice == 5:
    pass
elif choice == 6:
    pass
elif choice == 7:
    pass
elif choice == 8:
    pass
elif choice == 9:
    print("Your Call is being diverted to customer care executive.")
else:
    print("Invalid option")
"""
# India = ("New Delhi", "Mumbai", "Chennai", "Kolkata", "Bangluru", "Ahmedabad")
# for city in India:
#     print(city)

# India = {"New Delhi", "Mumbai", "Chennai", "Kolkata", "Bangluru", "Ahmedabad"}
"""
myName = "Python Rossum"
for character in myName:
    print(character)
"""

"""
for(i = 0; i < 20; i = i + 2)
{

}
"""
# range(5) = 0,1,2,3,4
# for i in range(10):
#     print(i)

# for i in range(5, 15):
#     print(fruits[i])

# for i in range(5, 15, 2):
#     print(fruits[i])

# User defined list:
"""
myList = []
print("Enter the elements to be added in the list:")
while True:
    quit = input("Press 'q' to quit, 'Enter' to enter member: ").lower()
    if quit == "q":
        break
    member = input()
    if member.isnumeric():
        member = float(member)
    myList.append(member)
print(myList)
"""
# counting number of digits in a given number
"""
number = int(input("Enter the number: "))       # 5672
digits = len(str(number))
print("number of digits:", digits)
"""
# list comprehension:

# numbers = []
# for i in range(1, 101):
#     numbers.append(i)
"""
numbers = [i for i in range(1, 101)]
print(numbers)
"""
"""
Perfect numbers:
30 = 1, 2, 3, 5, 6, 10, 15
28 = 

Armstrong numbers:
1634
if (1^4)+(6^4)+(3^4)+(4^4) == 1634: armstrong
"""
"""
n = int(input("Enter n: "))
flag = 1
for i in range(2, n):
    if n % i == 0:
        flag = 0
        print("Not Prime.")
        break
if flag == 1:
    print("Prime.")
"""
# break - else
n = int(input("Enter n: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime.")
        break
else:
    print("Prime.")