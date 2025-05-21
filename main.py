import streamlit as st

# Page config
st.set_page_config(page_title="Comprehensive Python Learning", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    /* General */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
        background-color: #f5f7fa;
        color: #333333;
    }
    .main-container {
        max-width: 900px;
        margin: auto;
        padding: 2rem 1rem;
        background-color: white;
        box-shadow: 0 4px 15px rgb(0 0 0 / 0.1);
        border-radius: 8px;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    h1 {
        font-weight: 900;
        font-size: 3rem;
        margin-bottom: 0.3rem;
    }
    h2 {
        border-left: 6px solid #007acc;
        padding-left: 10px;
        margin-top: 2rem;
        font-weight: 700;
        font-size: 2rem;
    }
    h3 {
        font-weight: 600;
        font-size: 1.4rem;
        margin-top: 1.5rem;
        color: #007acc;
    }
    p {
        line-height: 1.6;
        font-size: 1.1rem;
    }
    code {
        background-color: #eeeeee;
        padding: 3px 6px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
        color: #c7254e;
    }
    pre {
        background-color: #272822;
        padding: 10px;
        border-radius: 8px;
        overflow-x: auto;
        color: #f8f8f2;
        font-family: 'Source Code Pro', monospace;
        font-size: 0.95rem;
    }
    ul, ol {
        margin-left: 1rem;
        margin-bottom: 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #ffffffcc;
        border-radius: 8px;
        padding: 1rem;
    }
    a {
        color: #007acc;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Python Learning Navigator")
sections = [
    "Introduction",
    "Python Basics",
    "Control Flow",
    "Functions",
    "Modules & Packages",
    "File Handling",
    "Object-Oriented Programming",
    "Exception Handling",
    "Standard Libraries",
    "Useful Tips & Resources"
]
choice = st.sidebar.radio("Go to section:", sections)

# Title
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("Comprehensive Python Learning Web App")

# Content per section
if choice == "Introduction":
    st.header("Introduction to Python")
    st.write("""
    Python is a high-level, interpreted, and general-purpose programming language.
    It is known for its readability and versatility. Python supports multiple programming paradigms,
    such as procedural, object-oriented, and functional programming.
    
    Created by Guido van Rossum and first released in 1991, Python has become one of the most popular programming languages in the world.
    
    Python is used in many fields, including web development, data science, artificial intelligence, scientific computing, automation, and more.
    """)
    
elif choice == "Python Basics":
    st.header("Python Basics")
    st.subheader("Variables and Data Types")
    st.write("""
    In Python, you don't need to declare the variable type explicitly. Some common data types include:
    - Integers (`int`): Whole numbers
    - Floating point numbers (`float`): Numbers with decimals
    - Strings (`str`): Text enclosed in quotes
    - Boolean (`bool`): `True` or `False`
    """)
    st.subheader("Examples")
    st.code('''# Variable assignments
x = 10           # int
price = 99.99    # float
name = "Alice"   # string
is_active = True # boolean
''')

elif choice == "Control Flow":
    st.header("Control Flow")
    st.subheader("Conditional Statements")
    st.write("""
    Python uses `if`, `elif`, and `else` statements for conditional execution.
    """)
    st.code('''x = 10
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")
''')
    st.subheader("Loops")
    st.write("Python supports `for` and `while` loops.")
    st.code('''# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
''')

elif choice == "Functions":
    st.header("Functions")
    st.write("""
    Functions are reusable blocks of code that perform a specific task.
    They are defined using `def` keyword.
    """)
    st.code('''def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
''')
    st.subheader("Return Values")
    st.code('''def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7
''')

elif choice == "Modules & Packages":
    st.header("Modules and Packages")
    st.write("""
    - **Modules** are Python files with `.py` extension that contain functions, variables, and classes.
    - **Packages** are directories containing one or more modules and a special `__init__.py` file.
    - Use `import` statement to include modules/packages in your code.
    """)
    st.code('''# Importing a module
import math

print(math.sqrt(16)) # Output: 4.0

# Importing specific functions
from math import sqrt

print(sqrt(25)) # Output: 5.0
''')

elif choice == "File Handling":
    st.header("File Handling")
    st.write("""
    Python provides built-in functions to read from and write to files.
    Always close files or use `with` statement to manage file context.
    """)
    st.code('''# Writing to a file
with open('example.txt', 'w') as f:
    f.write("Hello World!")

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
''')

elif choice == "Object-Oriented Programming":
    st.header("Object-Oriented Programming (OOP)")
    st.write("""
    OOP allows structuring programs using classes and objects.
    It supports encapsulation, inheritance, and polymorphism.
    """)
    st.subheader("Example Class")
    st.code('''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}.")

p = Person("Alice", 30)
p.greet()
''')

elif choice == "Exception Handling":
    st.header("Exception Handling")
    st.write("""
    Use `try` and `except` blocks to handle run-time errors gracefully.
    """)
    st.code('''try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
''')

elif choice == "Standard Libraries":
    st.header("Python Standard Libraries")
    st.write("""
    Python comes with many useful standard libraries:
    - `os` for operating system tasks
    - `sys` for system-specific parameters
    - `math` for mathematical functions
    - `datetime` for working with dates and times
    - `random` for generating random numbers
    - `json` for JSON serialization and deserialization
    """)
    st.subheader("Example")
    st.code('''import os
print(os.name)

import datetime
now = datetime.datetime.now()
print(now)
''')

elif choice == "Useful Tips & Resources":
    st.header("Useful Tips & Resources")
    st.write("""
    - Use [Official Python Docs](https://docs.python.org/3/) for detailed info.
    - Practice problems on [LeetCode](https://leetcode.com/), [HackerRank](https://www.hackerrank.com/).
    - Learn with video tutorials on [freeCodeCamp](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and YouTube.
    - Use interactive notebooks with Jupyter or Google Colab.
    - Follow PEP8 style guide for readable code.
    """)
st.markdown('</div>', unsafe_allow_html=True)

 