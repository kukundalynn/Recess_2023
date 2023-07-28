# Inheritance
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")

class Dog(Animal):
    def bark(self):
        print(self.name + "is barking.....woof!")

class Cat(Animal):
    def meow(self):
        print(self.name + " is meowing")
        
# Create Animal instance
animal = Animal("Generic Animal")
dog =Dog("Sport")
cat =Cat("Fluffy")

# evoke call eat method
animal.eat()
dog.eat()
cat.eat()

# example 2 on inheritance
class Vehicle:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

    def display_info(self):
        print("Brand: " + self.brand)
        print("Colour: " + self.colour)

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def __init__(self, brand, colour, num_wheels):
        super().__init__(brand, colour)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print("Number of wheels: " + str(self.num_wheels))

    def honk(self):
        print("Car is honking")                

# Create Car instance
my_car = Car("Ford", "Blue", 4)

# Access and modify the car attributes
print("Brand: ", my_car.brand)
my_car.colour ="Black"

# invoke car methods
my_car.display_info()
my_car.move()
my_car.honk()

# exercise 1
import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius

    def calculate_perimeter(self):
        return 2* math.pi * self.radius

class Square (Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.length*self.width
    
    def calculate_perimeter(self):
        return 2*(self.length+self.width)
    
    my_circle = Circle(4)
    
    print(my_circle.calculate_area())
    print(my_circle.calculate_perimeter())
    

# Multiple Inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")

class Flyable(Animal):
    def fly(self):
        print(self.name + "is flying")

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        self. species=species

    def display_info(self):
        super(). display_info()
        print("Species: " + self.species)
        print("Name: " + self.name)

my_bird = Bird('Pigeon', 'bird',)

my_bird.eat()
my_bird.fly()
my_bird.display_info()
"""

# Overriding
class Animal:
    def make_sound(self):
        print("Animal is making sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")

class Cat (Animal):
    def make_sound(self):
        print("The cat is meowing")

def make_animal_sound(animal):
    animal.make_sound()

animal = Animal()
dog =Dog()
cat = Cat()

# Calling amke sound function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

# Polymorphism allows you to write code that can work with different objects

# methods overridiing occurs when a derived class, sub class provides its own implementation of a method that is already defined in the super class
# method overloading allows classto have multiple methods with the same name but different parameters

# example
"""
class Shape :
    def calculate_area(self):
        pass
   
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius
    
# create the shape objects
rectangle = Rectangle(4, 5)
circle = Circle(5)

# Calculate display area
print(rectangle.calculate_area())
print(circle.calculate_area())

# overloading functions
class Calculator:
    def add(self, x, y):
        return x + y
    def add(self, x, y, c):
        return x + y + c
    
# create object
calculator = Calculator()

#display output
print(calculator.add(1, 2))
print(calculator.add(1, 2, 3))

# Abstaction#
# Allows you focus on the essentials and hide the unnecessary ones
# example

class Vehicle(ABC):
    @abstactionmethod
    def start(self):
        pass

    @abstactionmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting car")

class Truck(Vehicle):
    def start(self):
        print("Starting truck")

# create vehicle object
car = Car()
truck = Truck()

# start the vehicle 
car.start()
truck.start()
"""

# Exercise 2
# calculating area ofa  circle
import math
import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

my_circle = Circle(2)
my_rectangle = Rectangle(4,5)

print(my_circle.calculate_area())
print(my_rectangle.calculate_area())


#Assignment
import tkinter as tk
import PIL
from PIL import ImageTk, Image

# Create main window

root = tk.Tk()
root.title("Receipt Printer")

# Define the function to generate the receipt
def generate_receipt():

# Create a new image
    
receipt = Image.new("RGB", (400, 200), (255, 255, 255))
draw = ImageDraw.Draw(receipt)

# Add text to the image
font = ImageFont.truetype("arial.ttf", 12)
draw.text((10, 10), "Sample Receipt", font=font, fill=(0, 0, 0))
draw.text((10, 30), "Item 1: $10", font=font, fill=(0, 0, 0))
draw.text((10, 30), "Item 1: $10", font=font, fill=(0, 0, 0))
draw.text((10, 50), "Item 2: $20", font=font, fill=(0, 0, 0))
draw.text((10, 70), "Total: $30", font=font, fill=(0, 0, 0))

# Save the image
receipt.save("receipt.png")
 # Open the image and display it
receipt.show()

# Create the button to generate the receipt
button = tk.Button(root, text="Generate Receipt", command=generate_receipt)
button.pack()

# Run the main loop
root.mainloop()





                        
     






    