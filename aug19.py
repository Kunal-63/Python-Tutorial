# Abstraction
"""
We use abstraction if and only if we want to achieve both the followings:
1. We want to disable instantiation in a class
2. We want to make at least one method compulsary for all child classes to have
"""
from datetime import datetime
from abc import ABC, abstractmethod                      # abc: abstract base classes, ABC: Abstract Base Class

staff = []

class Employee(ABC):
    leaves = 8

    @abstractmethod
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayDetails(self):
        print(f"-------- Details of {self.name} --------")
        print("Name:", self.name)
        print("Position:", self.position)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Leaves:", self.leaves)

    @staticmethod
    @abstractmethod
    def addEmployee():
        print("Enter the following details:")
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        return (name, age, gender)

    def generateID(self):
        # sample id: 082022M002
        year = str(datetime.now().year)
        month = str(datetime.now().month).zfill(2)
        sr = str(len(staff)).zfill(3)
        self.id = month + year + emp_type + sr

class Manager(Employee):
    education = "MBA"
    position = "Manager"                    # polymorphism

    # leaves = 10
    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    
    def displayDetails(self):           # e1.displayDetails()
        super().displayDetails()
        print("Education:", self.education)
        print("Experience:", self.experience)

    @classmethod
    def addEmployee(cls):              # Manager.addEmployee()      polymorphism
        name, age, gender = super().addEmployee()
        experience = int(input("Experience: "))
        return cls(name, age, gender, experience)

class Peon(Employee):
    position = "Peon"                   # polymorphism
    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    @classmethod
    def addEmployee(cls):               # polymorphism
        name, age, gender = super().addEmployee()
        return cls(name, age, gender)

class SalesExecutive(Employee):
    target = 1500000
    position = "Sales Executive"
    
    def __init__(self, name, age, gender, territory):
        super().__init__(name, age, gender)
        self.territory = territory

    def displayDetails(self):
        super().displayDetails()
        print("Target:", self.target)
        print("Territory:", self.territory)

    @staticmethod
    def emiCalculator():
        amount = int(input("Enter the billing amount: "))
        tenure = int(input("Tenure (in years): "))
        interest = float(input("Rate of interest (yearly) in %: ")) / 100
        months = tenure * 12
        total_amount = amount + (amount * interest * tenure)
        emi = total_amount/months
        print("EMI =", emi)
        return emi

    @classmethod
    def addEmployee(cls):
        name, age, gender = super().addEmployee()
        territory = input("Territory: ")
        return cls(name, age, gender, territory)

class GeneralManager(Manager):
    team_size = 100
    position = "General Manager"


e0 = Manager("Roshan", 26, "Male", 4)
emp_type = "M"
e0.generateID()
e1 = SalesExecutive("Roshni", 23, "Female", "Gandhinagar")
emp_type = "S"
e1.generateID()
# e2 = Peon("Sunder", 19, "Male")
# emp_type = "P"
# e2.generateID()

# e3 = Employee("Hetal", 29, "F")

staff.append(e0)
staff.append(e1)
# staff.append(e2)

while True:
    print("Press 1 to add new employee")
    print("Press 2 to view details of an employee")
    print("Press 9 to exit")
    choice = int(input())
    if choice == 1:
        print("Press M to add a manager")
        print("Press G to add a general manager")
        print("Press P to add a peon")
        print("Press S to add a sales executive")
        emp_type = input().upper()                  # m/g/p/s
        type_lookup = {"M": Manager.addEmployee, "G": GeneralManager.addEmployee, "P":Peon.addEmployee, "S":SalesExecutive.addEmployee}
        new_emp = type_lookup[emp_type]()
        new_emp.generateID()
        staff.append(new_emp)

    elif choice == 2:
        id = input("Enter id: ")
        sr_no = int(id[-3:])
        staff[sr_no].displayDetails()

    elif choice == 9:
        break
    
    else:
        print("Sorry, this option is not available at present. Please try again...")

# Upcoming Class: Encapsulation, File Handling, Exception Handling, Resource Management