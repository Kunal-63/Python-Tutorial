"""
numbers = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]

n2 = numbers.copy()
print("number =", numbers)
print("n2 =", n2)
n3 = numbers
print("n3 =", n3)
numbers.append(1000)
print("number =", numbers)
print("n3 =", n3)
print("n2 =", n2)
# n3.clear()
del numbers
# print("number =", numbers)
print("n3 =", n3)
print("n2 =", n2)
"""
n1  = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]
print(n1.count(11))
print("len before: ", len(n1))
# n1.count(11, 3, 10)
n4 = ["ahm", "bom", "del", "rtp"]
# n1.append(n4)
n1.extend(n4)
print(n1)
print("len after: ", len(n1))
"""
print(n1.index(-43))
print(n1.index(11, 3, 10))
print(n1.index(-45))
print(n1.index(-43, 10))
"""
n1.insert(5, "Shubham")
print(n1)

print(n1.pop())
# n1.pop(78)
print(n1.pop(7))
print(n1)

x = 9
n1.pop(x)
n1.remove(-43)
n1.remove(11)
print(n1)

n1  = [11, 22, 33, 11, 45, 78, 11, -43, 98, 11, -23.32, 11, 500]
# sorted(n1)
n1.sort()
n1.reverse()
print(n1)
