"""
..BASIC OPERATORS AND EXPRESSSIONS (INPUT AND OUTPUT OPERATORS)

Arthmetic Operators
+ Addition
- subtraction
* multiplication
/ division
// divide
% modulus
** exponentiation

..Comparison Operators
== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to

..Logical operators
logical AND 'and'
logical OR 'or'
logical NOT 'not'

..Assignment Operators
Assign value '='
add value '+'
add and assign value '+='
subtract and assign value '-='
multiply and assign value '*='
divide and assign value '/='
modulus and assign value '%='
exponentiate and assign value '**='

..Membership Operators
In: 'in' operator: checks if a value exists in a sequence
Not in :'not in'operator: checks if a value does not exisit in a sequence

..Identity operators
'is' checks if two values are the same 
'is not' checks if two values are not the same
"""

#+ Addition
from base64 import decode


#x=(100+20)
#print(x)
#- subtraction
y=(100-20)
print(y)
#* multiplication
z=(100*20)
print(z)
#/ division
a=(100/20)
print(a)
#// divide
b=(100//20)
print(b)
#% modulus
c=(100%20)
print(c)
#** exponentiation
d=(100**20)
print(d)

#comparison operators
x = 10
# Equal to
if x == 10:
    print('X is equal to 10')
# Greater than
if x > 4:
    print('X is greater than 4')
# Greater than or equal to
if x >= 10:
    print('X is greater than or equal to 10')
# Less than
if x < 11:
    print('X is less than 11')
# Less than or equal to
if x <= 11:
    print('X is less than or equal to 11')
# Not equal
if x != 6:
    print('X is not equal to 6')

#logical operators
f = 5
#and
print(f > 3 and f < 10)
#or
print(f > 3 or f < 4)
#not
print(not(f > 3 and f < 10))

#Membership operators
cars=['jeep','BMW', 'tesla']

if 'jeep' in cars:
    print('true')

#identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # returns True because z is the same object as x

print(x is y) 

# Bitwise operations
#used to perform operations on individual bits in of binary numbers
"""
Bitwise AND ('&')
Bitwise OR ('|')
Bitwise XOR ('^')
Bitwise NOT ('-')
Bitwise LEFT SHIFT('<<')
Bitwise RIGHT SHIFT('>>')

"""
g= 10
j= 20

print(g&j)
print (g|j)

#EXERCISE (calculator)

import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry field
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"))
button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)
button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)

# Position the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

# Start the main event loop
window.mainloop()