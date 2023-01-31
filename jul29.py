"""
from random import choice

def random_walk(path_length):
    x, y = 0, 0
    for i in range(path_length):
        dx, dy = choice[(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = x + dx, y + dy
    return (x, y)

print("Length\tProbability")
for path_length in range(7, 35):
    number_of_walks = 10000
    no_taxi = 0

    for j in range(number_of_walks):
        x, y = random_walk(path_length)
        d = abs(x) + abs(y)
        if d <= 5:
            no_taxi += 1
    probability = round(no_taxi/number_of_walks, 2)
    print(f"{path_length}\t{probability}")
"""

# Object Oriented Programming with Python
"""
It is easy to program with this approach
"""
# Car showroom management
"""
x = 5
print(x)
print(type(x))
a = [1,2,3]
print(type(a))
# print(a / x)
a.replace(2, 22)
"""
class Car:
    # class variable
    seating_capacity = 5

    def displayDetails(self):
        print(self.name)
        print(self.price)
        print(self.fuel)
        print(self.seating_capacity)
        print(self.__dict__)

c1 = Car()

# Object Variables:
c1.name = "i20"
c1.price = 1000000
c1.fuel = "Petrol"
"""
print("---------Details of c1---------")
print(c1.name)
print(c1.price)
print(c1.fuel)
print(c1.seating_capacity)
print(c1.__dict__)
"""

c3 = Car()
c3.name = "Merc ML450"
c3.price = 15000000
c3.fuel = "Diesel"
c3.seating_capacity = 7
"""
print("---------Details of c3---------")
print(c3.name)
print(c3.price)
print(c3.fuel)
print(c3.seating_capacity)
print(c3.__dict__)

"""

c2 = Car()

# Object Variables:
c2.name = "Volvo XC40"
c2.price = 8500000
c2.fuel = "Electric"
"""
print("---------Details of c2---------")
print(c2.name)
print(c2.price)
print(c2.fuel)
print(c2.seating_capacity)
print(c2.__dict__)
"""
print("---------Details of c1---------")
c1.displayDetails()
print("---------Details of c2---------")
c2.displayDetails()