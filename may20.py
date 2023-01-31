# set: Unordered and Mutable
"""
s1 = {11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500}

print(s1.add(100))
# print(s1)
# s1.clear()
# print(s1)
# del s1
# s1

s2 = s1.copy()
s3 = s1
print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
s1.discard(-23.32)
print(s1)
s1.remove(-43)
print(s1)
# print(s1.discard(5000))
# s1.remove(5000)
print(s1.pop())
print(s1)

print(len(s1))
s4 = {1000, 78, 2000, 45, 3000}
s1.update(s4)
print(len(s1))
"""
# Set operation methods
"""
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
universal = {i for i in range(1, 11)}

union = s1.union(s2)
print(union)
union = s2.union(s1)
print(union)

print(s1.intersection(s2))

diff1 = s1.difference(s2)    # s1 - s2
print(diff1)
diff2 = s2.difference(s1)    # s2 - s1
print(diff2)
print(diff1.union(diff2))   # {1,2,5,6}
print(s1.symmetric_difference(s2))

# s1 = s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
# s2.symmetric_difference_update(s1)
s1.difference_update(s2)    # s1 = s1 - s2
s2 = s1.difference(s2)

s1.intersection_update(s2)  # s1 = s1.intersection(s2)

print(s1.isdisjoint(s3))
print(s1.issubset(universal))
print(universal.issuperset(s1))
"""
# Frozenset: Immutable version of set
"""
fs1 = frozenset({1,2,3,4})
print(fs1)
t1 = (3,4,5,6)
fs2 = frozenset(t1)
print(fs2)
fs3 = frozenset([5,6,7,8])
print(fs3)
fs4 = frozenset((7,8,9,10))
print(fs4)
fs5 = frozenset("Neet")
print(fs5)
"""

# Dictionary: Unordered and Mutable collection of key:value pairs
"""
result = {"Physics":87, "Maths":92, "Python":99}
print(result["Maths"])
result["Maths"] = 29
print(result)

batch = {1:"Yug", 2:"Naitik", 3:"Chinmay", 4: "Madhav", 2:"Manthan"}
print(batch)

sample = {1:"number", "Physics":45, {"Physics":87, "Maths":92} :"fzst" }
print(sample)
"""
# key of a dictionary must be immutable and unique.
"""
working: number, string, tuple, frozenset
not working: list, set, dictionary
"""
party = {
    "Jap":"Maggie",
    "Tejas":13,
    "Dhiraj" : ("Khichdi", "Sabji", "Buttermilk"),
    "Krishna" : ["soup", "main course", "browny"],
    "Alakh" : {"soup", "main course", "browny"},
    "Madhusudan Sir" : frozenset({"Khichdi", "Sabji", "Buttermilk"}),
    "Rahul" : {"BF":"Poha", "Lunch":"Punjabi", "Dinner":"South indian"}
}
print(party)

# Homework
"""
1. Try nesting collections of Python in one another and deduce a conclusion.
l1 = [13, "Python", [1,2,3], {7,8,9}]
print(l1)

2. Program based on the above dictionary.
"""
