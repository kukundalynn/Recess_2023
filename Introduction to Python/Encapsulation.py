#example 1
class Car:
    def __init__(self, make, model, year) :
        self.make=make
        self.model=model
        self.year=year

    def start_engine(self):
        print("Engine has started")

    def stop_engine(self):
        print("Engine stopped")

#create object
my_car = Car("Toyota","Corola", 2022)
print(my_car.make)    
print(my_car.model) 
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

#example 2
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-=amount
        else:
            print ("Insufficient funds")

    def display_balance(self):
        print("Account number :", self.account_number)
        print("Balance:", self.balance)

# create bank account object
my_account = BankAccount("123456789",1000) 

# perform operations on account
my_account.display_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.display_balance()

# example 3
class Rectangle:
    def __init__(self, length, width) :
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2* (self.length + self.width)

# create a rectangle
my_rectangle = Rectangle(15,5)
print(my_rectangle.length)
print(my_rectangle.width)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())

# example 4 for 
class Student:
    def __init__(self, name, year, course ):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Year:", self.year)
        print("Course:", self.course)   
#create a student object
my_student = Student("Kukunda", 3, "BSSE")
my_student.display_details()

# example 5
class Person:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)    
        print("I am", self.age, "years old")

#create person object
my_person1 = Person("Kukunda", 20)
my_person2 = Person("Lynn", 21)

# accessing the object attributes
print(my_person1.name)
print(my_person1.age)
print(my_person2.name)
print(my_person2.age)

# object method
my_person1.greet()
my_person2.greet()

# exercise 1 circle
class circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159*(self.radius*self.radius)

    def calculate_circumference(self):
        return 2* 3.14159*(self.radius)


my_circle = circle (7)
print(my_circle.radius)
print(my_circle.calculate_area())
print(my_circle.calculate_circumference())

# exercise 2 employees bonuses
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary *0.15
        
e1 = Employee("Lynn",25000)
print(e1.bonus())
e2 = Employee("Isabella",35000)
print(e2.bonus())

#Encapsulation
#Key main goals of encapsulation are;
#1. To hide the implementation details of an object
#2. to protect the object from changes
#3. to protect the object from external changes

#example 1
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount    

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance-=amount
        else:
            print ("Insufficient funds")

    def get_balance(self):
       return self._balance

# create bank account object
my_account = BankAccount("123456789",1000)

#access the bank object and modify encapsulation
print(my_account.get_balance())
my_account.deposit(500)
print(my_account.get_balance())
my_account.withdraw(200)
print(my_account.get_balance())
      
# exercise 1 temp converter
class TempConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius
    
    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
temp1 = TempConverter(34)

celsius_temp = temp1.get_celsius()

fahrenheit_temp = temp1.get_fahrenheit()
print(fahrenheit_temp)

# exercise 2 employees pay increament
#class Employe:
   # def __init__(self, name, salary):
       # self._name = name
       # self._salary = salary

    #def increment_salary(self):
        #self._salary += 150,000
        #return self._salary

#employee1 = Employe("Lynn Kukunda",850,000)
#print(employee1.increment_salary())

        
