
# Functions
# group blocks of code
# def function_name():

from math import *
import math


def afternoon(first_name, last_name):
    print("Good afternoon, " + first_name + " " + last_name)
    print("Attendees present")


# call function
afternoon("Lynn", "Kukunda")

# arguments and parameters
# argument
# parameters


print(sqrt(16))
print(factorial(6))

# input and output in python
# input('prompt')

# example of input
"""
name = input("Enter your name:")
print("My name is " + name)

# example 2
number = int(input("enter number: "))
product = number * 10
print(product)

# multiple inputs
s, r, w = map(int, input("Enter the values: ").split())
print("The values are:", end="")
print(s, r, w)
"""

# How to capture input from a tuple
w = (2, 4, 6, 8)
print("Current tuple")
print(w)
print(type(w))

E = list(w)
E.append(int(input("Enter new value: ")))
w = tuple(E)
print("Updated tuple")
print(w)

my_list = list(map(int, input("Enter the list value: ").split()))
my_set = set(map(int, input("Enter the set value: ").split()))

print(my_list)
print(type(my_list))
print(my_set)
print(type(my_set))
