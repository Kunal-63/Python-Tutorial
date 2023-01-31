# Collections in Python:
"""
Special Collection:
String: Collection of characters : Ordered and Immutable
Dictionary: Collection of key:value pair : Unordered and Mutable

Ordered     Mutable         List
Ordered     Immutable       Tuple
Unordered   Mutable         Set
Unordered   Immutable       Frozenset
"""
# list: Ordered and Mutable collection of members
# l1 = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]
# print(l1)
# print(type(l1))
# Ordered Means:
"""
Each and every element has positive and negative index number
access through index numbers (positive and negative both)
slicing (with positive and negative indices)
slicing with step (positive and negative)
"""
"""
print(l1[5])
print(l1[-5])
print(l1[3 : -3 : 2])
print(l1[-1 : 3 : -1])
print(l1)               # slicing will always give you a new collection

l1[5] = 780
print(l1)

print(min(l1))
print(max(l1))
print(sorted(l1))          # sorted() always give you a NEW LIST
# print(l1)
print(round(sum(l1), 2))

vegetables = ["capsicum", "tomato", "onions", "corn", "olive", "mushrooms", "carrot", "cabbage", "Potato"]
print(vegetables)
print(min(vegetables))
print(max(vegetables))
print(sorted(vegetables))
# sum(vegetables)

mix_veg = ["capsicum", 2, "tomato", 5, "onions", -3.5, "corn", 0.75]
mix_veg = ["capsicum", "2", "tomato", "5", "onions", "-3.5", "corn", "0.75"]
print(mix_veg)
print(sorted(mix_veg))
"""
# List methods
numbers = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]
myString = "Next friday we will go to watch a movie."
yourString = "Above sentence is False."
myString.split().append("For sure.")

numbers.append(1000)
print(numbers)

# numbers.clear()
# print(numbers)
# del numbers
# print(numbers)

print(numbers.count(11))

myFavoriteStudent = "Chinmay"
print(min("Chinmay"))
print(max("Chinmay"))
print(sorted("Chinmay"))

# Next Class: .copy() method

