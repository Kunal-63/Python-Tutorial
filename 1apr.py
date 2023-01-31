# s1 = "Students of this batch are going to rock the software industry. They are Bill Gates, Elon Musk and Steve Jobs of the future. They have potential to create another microsoft in India. But, some of them always keep their camera off."

"""
a = s1.find("are")
print(s1.find("are", 24))
print(s1.find("are", 24, 49))
print(s1.index("are", 24, 49))
"""
"""
print(s1.find("of"))
print(s1.rfind("of"))
print(s1.rfind("of", 50))
print(s1.rfind("of", 30, 200))
print(s1.rfind("of", 50, 100))

print(s1.rindex("of"))
print(s1.rindex("of", 50))
print(s1.rindex("of", 30, 200))
print(s1.rindex("of", 50, 100))
"""
# Methods starting with "is" always returns either True or False
"""
s2 = "987654321"
print(s2.isnumeric())
s3 = "AlakhPandya"
print(s3.isalpha())
print(s1.isalpha())
print(s2.isalpha())
s4 = "987Alakh321Pandya654"
print(s4.isalnum())
print(s2.isalnum())
print(s3.isalnum())
"""
"""
s5 = "2022"
s6 = "2⁸"
s7 = "②⓪②②"
s8 = "Ⅳ"
s9 = "¾"
s10 = "二千二十二"
# print(s8.isdecimal())   # strictly considers only digits 0 to 9 as numbers.
# print(s8.isdigit())     # also considers subscript, superscript, circled numbers
# print(s10.isnumeric())   # also considers roman numerals, vulgar fractions, numbers from other languages
"""
"""
s11 = "ifisforwhile"
print(s11.isidentifier())
print(s1.islower())
print(s11.islower())
print(s1.isupper())
print(s1.istitle())
s12 = "Darshil is a good boy.\nHe keeps camera on."
print(s12.isprintable())
s13 = "                \n\n\n\n\n     \t\t\t\t        \n"
print(s13.isspace())
"""
s1 = "Students of this batch are going to rock the software industry. They are Bill Gates, Elon Musk and Steve Jobs of the future. They have potential to create another microsoft in India. But, some of them always keep their camera off."
# print(s1.split())
# print(s1.split("o"))
# print(s1.split("are"))
# print(s1.split("of", 3))
# print(s1.split(" ", 5))

# print(s1.rsplit("o"))
# print(s1.rsplit("of", 3))

# print(s1.partition("industry."))
# print(s1.partition("of"))
# print(s1.rpartition("of"))
"""
myList = ["I", "Love", "India"]
print(" ".join(myList))
print("#".join(myList))
print("Python".join(myList))
print("".join(myList))

s2 = "                           Good Night!"
s3 = s2.lstrip()
print(s3)
s4 = "&&&&&&&&&&&&&&&&&&&&Python is fun!&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
print(s4.lstrip("&"))
print(s4.rstrip("&"))
print(s4.strip("&"))

print(s1.replace("of", "for"))
print(s1.replace("of", "for", 4))

s4 = "Harshil has started packing his bags.\nHe will go to home from here.\nAtleast, he has told this to his parents."
print(s4.splitlines())

date = input("Enter date: ")
month = input("Enter month number: ")
year = "2022"
print(f"Date in dd/mm/yyyy format: {date.zfill(2)}/{month.zfill(2)}/{year}")

Homework:
1. Ask user for the first name, middle name and surname. Then print his/her name by converting first and middle names to their initials as given in example.
Example:
First Name: Alakh
Middle Name: Janakkumar
Surname: Pandya
Output:
A.J.Pandya

first_name = input("Enter first name: ")
middle_name = input("Enter middle name: ")
surname = input("Enter surname: ")
print(first_name[0] + "." + middle_name[0] + "." + surname)

2. Make a Python program to convert first occurrences of "h" into uppercase in given string. 

input_string = input("Enter any string: ")
print(input_string.replace("h", "H", 1))


3. Write a program in Python that asks 2 strings from the user and interchanges first 3 characters of both the strings.
eg:
input strings:
color
full
Output:
fulor
coll

string1 = input("Enter two strings:\n") # color
string2 = input()                       # full
output_string1 = string2[:3] + string1[3:]
output_string2 = string1[:3] + string2[3:]
print("Output:")
print(output_string1)
print(output_string2)

4. Write a program in Python that asks 2 strings from user and interchange their first 3 and last 3 characters
eg:
input strings:
string1: superstar
string2: rocking

Output:
string1: ingerstar
string2: rocksup

5. Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".
Example:
input string: Keep yourself muted while not speaking.
output: Keep_yourself mute while not#speaking.
"""

# sentence = input("Enter a sentence: ")
sentence = "Keep yourself muted while not speaking."
# sentence = sentence.replace(" ", "_", 1)
# sentence = sentence[::-1]
# sentence = sentence.replace(" ", "#", 1)
# sentence = sentence[::-1]
# print(sentence)
print(sentence.replace(" ", "_", 1)[::-1].replace(" ", "#", 1)[::-1])
"""
6. Write a program to find the number of vowels, white space and other characters in a given string.
Example:
input string: Python Programming
output:
vowels: 4
whitel spaces: 1
consonents: 13

string1 = "Keep yourself muted while not speaking."
temp = string1.lower()
vowels = temp.count("a") + temp.count("e") + temp.count("i") + temp.count("o") + temp.count("u")
spaces = temp.count(" ")
others = len(string1) - vowels - spaces
print(f"Vowels: {vowels}\nWhite Spaces: {spaces}\nOther Characters: {others}")

7. Write a program to make a new string with the word "the" deleted in the given string.
eg:
input string: This is the lion in the cage.
output: This is  lion in  cage.

input_string = "This is the lion in the cage."
print(input_string.replace("the", ""))
"""