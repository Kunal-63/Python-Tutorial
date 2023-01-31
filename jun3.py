"""
1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.

3. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.

5. Ask user to give names and marks of 10 different students. Store them in dictionary.

6. Sort the above dictionary by the names of students.

7. Sort the dictionary in ex-5 by the marks.

8. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.

9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""
"""
words = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
string = input("Enter a string: ")      # bug
temp = []
for phrase in words:    # phrase = 'no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy'
    count = phrase.count(string)    # = 0_no bun, 4_bug bun bug bun bug bug, 1_bunny bug, 4_buggy bug bug buggy
    temp.append(str(count) + "_" + phrase)
    # temp = [0_no bun, 4_bug bun bug bun bug bug, 1_bunny bug, 4_buggy bug bug buggy]
temp.sort(reverse=True)
# print(temp)
sorted_list = []
for phrase in temp:
    split_list = phrase.split("_")
    sorted_list.append(split_list[1])
print("Sorted List =", sorted_list)
"""
# 8. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.
"""
word = input("Enter any word: ")
frequency = {}
for letter in word:
    frequency[letter] = word.count(letter)
print(frequency)
"""
# 9. Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""
raw_result = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
final_result = []
for i in range(4):      # i = 0,1,2,3
    student_result = {}
    for x in raw_result:		# x = 'Science', 'Language'
        student_result[x] = raw_result[x][i]		# [88, 89, 62, 95]
    # print(student_result)
    final_result.append(student_result)
print(final_result)
"""
"""
m1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(m1[2][0])
print(m1[1][2])
"""
# Write a Python code that takes 5 integers from user and prints sum of their factorial using function.
# import random

# print(random.choice.__doc__)
def factorial(n):           # 5
    """This function returns factorial of the number given in the argument.
        And this is my first docstring
    """
    fact = 1
    for i in range(1, n+1):      # for i in range(1, 6): i = 1,2,3,4,5
        fact = fact * i
    return fact

# print("Enter 5 integers:")
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# sum = factorial(a) + factorial(b) + factorial(c) + factorial(d) + factorial(e)
# print(f"{a}! + {b}! + {c}! + {d}! + {e}! = {sum}")
print(factorial.__doc__)

# single line comment
'''
This
'''
# or
"""
This
"""
# Docstring
# myString = '''I would'nt be so sure to say "I am bullet proof"'''
# print(myString)
# print(type(myString))

# Next Class: 
"""
We type () after a function only when either we want to call it or to define it.
"""