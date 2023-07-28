# Advanced topics in Python

"""
--SUMMARY
1. Regular expressions
2. Generators and iterators
3. Decorators
4. Context managers
5. multithreading and multiprocessing
"""
# Regular expressions
"""
summary
\d : Matches any digit(0-9)
\w : Matches any alphanumeric character(0-9, a-z, A-Z and underscore)
\s : Matches any whitespace character(space, tab, new line)
. : Matches any character except a newline
* : Matches zero or more ocuurances of the preceding character or group
+ : Matches one or more ocuurances of the preceding character or group
? : Matches zero or one ocuurances of the preceding character or group
[] : Matches any character within the square bracket
[^] : Matches any character not within the square bracket
^ : Matches the start of a line
$ : Matches the end of a line

"""
#Matching and Searching
#regex re.match(), re.search(), re.findall(),

# Exanple 1 Demonstrating regex | Match first word, match group word, match all numbers
"""
import re
text = "Hello, my name is Kukunda Lynn. I am a software engineering student at makerere university, Uganda."

# Match first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Match", match.group())

matches = re.findall(r"\d+", text)
print("Matches:", matches)
"""

# Example 2 validate email format or email address
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

print(validate_email("kukundalynn@gmail.com"))
print(validate_email("isabellalynn426@gmail.com"))

# Generators and iterators
# 'yeid' generator
# Iterator '__iter__' '__next__' iterator

def factorial(n):
    # Return the factorial of the number 
    if n == 0:
        yield 1
    else:
        yield n * factorial(n - 1)
    
# print the factorial of the number from 1-10
for i in range (1,10):
    print(factorial(i))

# Iterators
def squares():
    for i in range (1,10):
        yield i ** 2    

# create an iterator object that yeilds the square of numbers from 1-10
squares_iterator = squares()

# print the square of the first 5 numbers
for i in range(5):
    print(next(squares_iterator))

# Decorators @my_decorator
# Decorators in python allow you to modify the behaviour of functions or classes without 
#directly changing their source code 
"""
def my_decorator(func):
    def inner():
        print("This is a decorator")
        func()
    return inner()

@my_decorator
def outer_decorator(func):
    print("This is an outer decorator")

outer_decorator()    
"""
# context manager 
# Is an objesct that defines a temporary context for a block of code
# example 1
# demonstrating a context manager to open a file and return a context instance
"""
def open_file(filename):
    
   file = open(filename, 'r')
   def __enter__():
       return file
   
   def __exit__(self, exc_type, exc_val, exc_tb):
       file.close()
       return __enter__ .__exit__

with open_file("my_file.txt") as f:
    contents = f.read()
"""    
# example 2, context manager using time series
"""
import time

class Timer:
    def __enter__(self):
      self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        execution_time = execution_time
        print("Execution time:", execution_time)

# with example usage
with Timer():
    # measure execution time
    time.sleep(1)      
"""
# Multithreading and multi-multiplexing
# techeniques that can be used to improve performance of a python program

# Multithreading is a technique where multiple threads are created within a single process
# Multiplexing is a technique where multiple threads 

# example of multithreading
"""
import threading

def task(name):
    print (f"Running task {name}")

#create multiple threads
threads =[]
for i in range(10):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

# wait for all thraed to finish

for t in threads:
    t.join()
"""
# Example 4: demonstrate for multiprocessing
"""
import multiprocessing

def process_task(name):
    print (f"Processing task {name}")

# create a pool of processes
pool =multiprocessing.Pool(processes=5)

# submit the multiple task to the pool
for i in range (6):
    pool.apply_async(process_task, args=(f"Process {i}",))

# close the pool and wait for the processes to finish
pool.close()
pool.join()
"""
# Example 5: use of multithreading and multiprocessing
import threading
import multiprocessing

def task(name):
    print (f"Running task {name} thread {threading.current_thread().name}with process (multiprocessing.current_process().name)")

# craete multiple thraeds
threads =[]
for i in range(10):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

# Assignment 
# 1a) Show a context manager for file handling that automatically opens and closes a file

class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    #The __enter__ method opens the test.txt file in write mode(setup operation) and returns a file object to variable f.
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
    #The __exit__ method closes the test.txt file(teardown operation).

# loading a file
with File('test.txt', 'w') as f:
    f.write('Test')
 
print(f.closed)

# b) Show a context manager for managing a database connection
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

#The '_enter' method creates a new connection to the database and returns it, while the 'exit_' method closes the connection. 

with DatabaseConnection('my_database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# I use the `with` statement to create a new instance of the `DatabaseConnection` class, which automatically opens and closes the database connection.

# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.

import threading
import multiprocessing
import time

def my_function(seconds):
    print(f'Starting function for {seconds} seconds')
    time.sleep(seconds)
    print(f'Function finished after {seconds} seconds')

# Multi-threading
threads = []
for i in range(1, 6):
    t = threading.Thread(target=my_function, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Multi-processing
processes = []
for i in range(1, 6):
    p = multiprocessing.Process(target=my_function, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()


