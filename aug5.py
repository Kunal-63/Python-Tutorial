"""
class Car:
    # class variable
    seating_capacity = 5
    def __init__(self, name, price, fuel):
        self.name = name
        self.price = price
        self.fuel = fuel

    def displayDetails(self):
        print(self.name)
        print(self.price)
        print(self.fuel)
        print(self.seating_capacity)


c1 = Car("BMW 750i", 12000000, "Petrol")
c1.displayDetails()
c2 = Car("XUV700", 2500000, "Diesel")
c2.displayDetails()
"""

# 4 pillars of OOP: Inheritance, Polymorphism, Abstraction, Encapsulation

# Inheritance:
# Simple Inheritance/Single Inheritance
"""
Parent Class --> Child Class
"""
"""
class Papa:
    vehicle = "Car"

    def Possessions(self):
        print("Vehicle:", self.vehicle)

class Daughter(Papa):
    pass

d1 = Daughter()
# print(d1.vehicle)
d1.Possessions()
"""


# Multi level inheritance:
"""
Parents Class --> Child Class --> Grand Child Class ........
"""
"""
class GrandPa():
    home = "Farm House"

class Papa(GrandPa):
    vehicle = "Car"

class Son(Papa):
    pass

s1 = Son()
print(s1.home)
print(s1.vehicle)
"""

# Hierarchical Inheritance
"""

                --> Child Class 1
Parent Class    --> Child Class 2
                --> Child Class 3



class A():
    ratings = "4 star"

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass


d1 = D()
print(d1.ratings)
"""

# Multiple Inheritance
"""
Base Class 1
Base Class 2
Base Class 3    --> Child Class
.
.
.
.
"""
"""
class Base1():
    hobby = "Guitar"

class Base2():
    Vehicle = "Bike"
    hobby = "Cricket"

class Derived1(Base2, Base1):
    pass

class Derived2(Base1, Base2):
    pass

class subDerived(Derived1, Derived2):
    pass

d1 = Derived1()
print(d1.hobby)
print(d1.Vehicle)
"""

# Hybrid Inheritance
"""
class Base1():
    pass

class D1(Base1):
    pass

class D2(Base1):
    pass

class D3(Base1):
    pass

class F1(D2):
    pass

class G1(F1):
    pass
"""
# Employee Management System

class Employee:
    leaves = 8

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayDetails(self):
        print(f"-------- Details of {self.name} --------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Leaves:", self.leaves)

class Manager(Employee):
    education = "MBA"
    # leaves = 10
    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    
    def displayDetails(self):
        super().displayDetails()
        print("Education:", self.education)
        print("Experience:", self.experience)

class Peon(Employee):
    pass

class SalesExecutive(Employee):
    target = 1500000
    
    def __init__(self, name, age, gender, territory):
        super().__init__(name, age, gender)
        self.territory = territory

    def displayDetails(self):
        super().displayDetails()
        print("Target:", self.target)
        print("Territory:", self.territory)

class GeneralManager(Manager):
    team_size = 100

# m1 = Manager("Roshan", 26, "Male", 4)
# print(m1.leaves)
# m1.displayDetails()
# p1 = Peon("Sunder", 19, "Male")
# p1.displayDetails()
# m2 = Manager("Urmi", 24, "Female", 1)
# m2.leaves = 20
# print(m2.leaves)
# m2.displayDetails()

s1 = SalesExecutive("Roshni", 23, "Female", "Gandhinagar")
s1.displayDetails()