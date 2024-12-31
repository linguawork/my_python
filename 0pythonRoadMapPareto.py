
'''
To learn Python effectively using the Pareto Principle (80/20 rule), 
we’ll focus on mastering the 20% of Python concepts that will give you 80% of the results, 
meaning the essential tools, libraries, and skills that are most commonly used in real-world programming. 
By mastering these, you'll be able to tackle most Python projects with confidence, whether you're 
focusing on web development, data analysis, automation, or general-purpose programming.
'''

Pareto-Based Python Learning Roadmap
1. Master the Basics (20%)

    Goal: Understand the core syntax, data structures, and basic programming concepts.
    Why: These are the building blocks for everything else in Python. 
    Without these, you won’t be able to write basic programs or understand more advanced topics.

Action Steps:

    Syntax: Learn how to write and run Python code.
    Variables & Data Types: Integers, floats, strings, booleans.
    Operators: Arithmetic, comparison, and logical operators.
    Control Flow: if, else, elif, loops (for, while).
    Functions: Writing functions, parameters, return values, and understanding scope.
    Error Handling: Learn how to handle errors using try, except, finally.
    Basic I/O: Learn how to read from and write to the console, as well as working with files.

# Basic example
def greet(name):
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!

2. Data Structures (20%)

    Goal: Master essential data structures such as lists, dictionaries, sets, and tuples.
    Why: These data structures are foundational and will allow you to manipulate data efficiently. 
    They are used in nearly every Python project.

Action Steps:

    Lists: Learn how to store and manipulate ordered data (e.g., adding/removing items, slicing).
    Dictionaries: Store key-value pairs, an essential structure for most applications.
    Sets: Learn how to store unique items and use set operations.
    Tuples: Understand immutable sequences of items.
    Comprehensions: List and dictionary comprehensions for cleaner, more Pythonic code.

# Data structures examples
my_list = [1, 2, 3, 4]
my_dict = {"name": "John", "age": 30}
my_set = {1, 2, 3}
my_tuple = (1, 2, 3)

# List comprehension
squares = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]

3. Object-Oriented Programming (OOP) (15%)

    Goal: Learn to create classes and objects, which is critical for writing clean, modular, and reusable code.
    Why: OOP is a common paradigm used in Python and many large-scale applications. Understanding classes, inheritance, and polymorphism will help you structure your code more effectively.

Action Steps:

    Classes & Objects: Understand the concept of classes and create objects.
    Methods & Attributes: Learn to define functions (methods) inside classes and access object attributes.
    Inheritance & Polymorphism: Learn how one class can inherit from another and override methods.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says woof!

4. Libraries and Frameworks (15%)

    Goal: Learn how to leverage powerful Python libraries to handle common tasks (web scraping, data analysis, automation, etc.).
    Why: Python has a huge ecosystem of libraries that allow you to accomplish complex tasks with minimal code. Familiarity with key libraries will accelerate your development process.

Action Steps:

    NumPy: Learn the basics of numerical computing and handling arrays.
    Pandas: Master data manipulation, cleaning, and analysis with data frames.
    Requests: Make HTTP requests to interact with APIs and fetch data.
    BeautifulSoup/Scrapy: Learn how to scrape web data.
    Flask/Django: (Optional) Basic introduction to web development frameworks.

import pandas as pd

# Simple data manipulation with pandas
data = {'name': ['John', 'Jane'], 'age': [28, 32]}
df = pd.DataFrame(data)
print(df)

5. File Handling and Regular Expressions (10%)

    Goal: Understand how to work with files and use regular expressions (regex) for text parsing.
    Why: File handling is essential for reading and writing data, and regex is incredibly useful for pattern matching and text manipulation.

Action Steps:

    Reading and Writing Files: Learn to handle files (open(), read(), write(), with).
    Regular Expressions: Learn the basics of regex for pattern matching, text extraction, and manipulation.

# File handling example
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Regex example
import re
pattern = r"\d+"  # Matches digits
text = "The house number is 123."
result = re.findall(pattern, text)  # Output: ['123']

6. Testing (5%)

    Goal: Learn to write unit tests to ensure your code is reliable and maintainable.
    Why: Writing tests is essential for professional software development. Python’s built-in unittest and pytest libraries make it easy to write and run tests.

Action Steps:

    Learn basic testing with unittest.
    Understand how to write assertions and run test suites.

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

7. Documentation and Code Style (5%)

    Goal: Learn to write clean, readable code and document it well.
    Why: Writing well-documented and consistent code is essential for collaboration and maintaining projects.

Action Steps:

    Follow Python’s PEP 8 guidelines for code style.
    Write docstrings for functions and classes.
    Use comments effectively to explain complex sections of code.

def greet(name):
    """
    This function greets the user with their name.
    
    Args:
        name (str): The name of the user.
    """
    print(f"Hello, {name}!")

Summary of the Pareto Roadmap:

    Master the Basics (20%): Learn Python syntax, control flow, functions, and basic I/O.
    Data Structures (20%): Understand lists, dictionaries, sets, and tuples, and use comprehensions.
    Object-Oriented Programming (15%): Master classes, objects, inheritance, and polymorphism.
    Libraries and Frameworks (15%): Learn NumPy, Pandas, Requests, BeautifulSoup, and basic web frameworks.
    File Handling and Regular Expressions (10%): Work with files and learn basic regex.
    Testing (5%): Understand how to write unit tests to ensure code quality.
    Documentation and Code Style (5%): Follow Python’s best practices for writing clean, readable code.

By focusing on these core areas, you’ll be well-equipped to tackle most Python projects, 
from scripting and automation to web development and data analysis.