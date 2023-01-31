# result = {"Nishit":68, "Keyur":72, "Riddh":84, "Parikshit":95}
"""
result["Bhargav"] = 38
print(result)

# Dictionary methods:
# result.clear()
# del result

r1 = result.copy()
r2 = result
print(result)

# result.fromkeys()
beneficiaries = ["Yug", "Madhav", "Jainam", "Prince", "Daksh"]
subsidy = dict.fromkeys(beneficiaries, 20000)
print(subsidy)

print(result.get("Parikshit"))
print(result["Parikshit"])

print(result.get("Akshi", "Sorry, this key is not found..."))
# print(result["Akshi"])
"""
"""
result = {"Nishit":68, "Keyur":72, "Riddh":84, "Parikshit":95}
print(result.keys())
# for name in result.keys(): # x = "Nishit"     same as: for name in result:
#     print(name.upper())

print(result.values())
# for marks in result.values():    # x = 
#     print(marks)

print(result.items())
# for student, percentage in result.items():
#     print(f"{student} got {percentage}% in final exams.")

print(result)
# print(result.pop("Riddh"))
# print(result)

print(result.popitem())

full_pyramid = {"Prakash":72, "Pavan":77, "Karishma":82, "Dipa":64}
result.update(full_pyramid)
print(result)
"""
"""
result = {"Nishit":68, "Keyur":72, "Riddh":84, "Parikshit":95}
student = input("Enter student name: ")     # Alakh, Keyur
percentage = int(input("Percentage: "))     # 15,    27
old_percentage = result.setdefault(student, percentage)     # 72
if percentage == old_percentage:
    print(f"Student {student} successfully added with {percentage}%!")
else:
    print(f"Student {student} already exists with {old_percentage}%...")
    overwrite = input("Do you want to overwrite? Y/N? ").lower()
    if overwrite == "y":
        result[student] = percentage
        print(f"Student {student} successfully overwritten with {percentage}%!")
    else:
        print(f"Student {student} could not be added...")
print(result)
"""
# Functions:
"""
1. without argument, without return
2. with arguments, without return
3. without argument, with return
4. with arguments, with return
"""
"""
def printReview():
    print("Remind us again, what is it that they say about women and disgruntlement?\nOh, yes, “Hell hath no fury like a woman scorned.”\nDown there at the ‘Bhool Bhulaiyaa 2’ camp, for writer Aakash Kaushik and director Anees Bazmee, that aphorism takes a life of its own.\nYes, we all have our thoughts and feelings about this sequel but separate yourself from the memories of Akshay Kumar’s debut instalment for a bit and allow the latest rendition to introduce itself.\n")

print("Enter two integers:")
a = int(input())
b = int(input())
if a > b:
    printReview()
if a > 0:
    printReview()
if b > 0:
    printReview()
if (a/b) > 0:
    printReview()
"""

def avg(x, y):
    ans = (x+y)/2
    print(f"Average of {x} and {y} is:", ans)
    return ans

# avg(5, 10)
print("Enter two integers:")
a = int(input())    # 10
b = int(input())    # 20
p = avg(a, b)

print("Enter two integers:")
c = int(input())    # 30
d = int(input())    # 40
q = avg(c, d)
print("sum =", p + q)