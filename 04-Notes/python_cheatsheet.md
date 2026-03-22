# Python Cheatsheet

A quick reference for the most commonly used Python syntax and concepts.

---

## Variables & Data Types

```python
name = "Phil"           # str
age = 25                # int
height = 5.11           # float
is_active = True        # bool

type(name)              # <class 'str'>

# Type conversion
int("25")               # 25
float(10)               # 10.0
str(100)                # "100"
bool(0)                 # False
```

---

## Strings

```python
name = "python"

name.upper()            # "PYTHON"
name.lower()            # "python"
name.capitalize()       # "Python"
name.replace("p", "j")  # "jython"
name.strip()            # remove whitespace
name.split(",")         # split into list
name.startswith("py")   # True
name.endswith("on")     # True
len(name)               # 6

# f-strings
print(f"Hello {name}")

# Slicing
name[0]                 # "p"
name[-1]                # "n"
name[0:3]               # "pyt"
name[:3]                # "pyt"
name[3:]                # "hon"
```

---

## Lists

```python
fruits = ["apple", "banana", "cherry"]

fruits[0]               # "apple"
fruits[-1]              # "cherry"
fruits[0:2]             # ["apple", "banana"]

fruits.append("mango")  # add to end
fruits.insert(1, "kiwi") # add at index
fruits.remove("apple")  # remove by value
fruits.pop()            # remove last item
fruits.pop(0)           # remove at index
fruits.sort()           # sort ascending
fruits.reverse()        # reverse list
fruits.clear()          # empty the list

len(fruits)             # number of items
"apple" in fruits       # True / False

# List comprehension
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

---

## Tuples

```python
coords = (10, 20)       # immutable list

coords[0]               # 10
x, y = coords           # unpacking

len(coords)             # 2
10 in coords            # True
```

---

## Dictionaries

```python
user = {
    "name": "Phil",
    "age": 25,
    "active": True
}

user["name"]            # "Phil"
user.get("name")        # "Phil" (safe, no error if missing)
user["email"] = "a@b.com"   # add key
user.pop("age")         # remove key

user.keys()             # all keys
user.values()           # all values
user.items()            # all key/value pairs

"name" in user          # True

# Loop through
for key, value in user.items():
    print(key, value)
```

---

## Sets

```python
tags = {"python", "code", "dev"}

tags.add("learn")       # add item
tags.remove("dev")      # remove item
tags.discard("x")       # remove safely (no error)

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}

a | b                   # union     {1, 2, 3, 4}
a & b                   # intersection {2, 3}
a - b                   # difference  {1}
```

---

## Conditionals

```python
age = 20

if age >= 18:
    print("adult")
elif age >= 13:
    print("teen")
else:
    print("child")

# One line
status = "adult" if age >= 18 else "minor"

# Operators
==  !=  >  <  >=  <=
and  or  not
```

---

## Loops

```python
# for loop
for i in range(5):
    print(i)             # 0 1 2 3 4

for item in ["a", "b", "c"]:
    print(item)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop controls
break                   # exit loop
continue                # skip to next iteration
pass                    # do nothing placeholder

# enumerate — index + value
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# zip — loop two lists together
for a, b in zip([1, 2], ["x", "y"]):
    print(a, b)
```

---

## Functions

```python
def greet(name):
    return f"Hello {name}"

greet("Phil")           # "Hello Phil"

# Default parameter
def greet(name="World"):
    return f"Hello {name}"

# Multiple return values
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([1, 5, 3])

# *args — variable arguments
def total(*nums):
    return sum(nums)

total(1, 2, 3)          # 6

# **kwargs — keyword arguments
def display(**info):
    for k, v in info.items():
        print(k, v)

display(name="Phil", age=25)

# Lambda
square = lambda x: x ** 2
square(4)               # 16
```

---

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No error")
finally:
    print("Always runs")

# Raise an error
raise ValueError("Invalid input")
```

---

## File Handling

```python
# Read
with open("file.txt", "r") as f:
    content = f.read()

# Write
with open("file.txt", "w") as f:
    f.write("Hello")

# Append
with open("file.txt", "a") as f:
    f.write("\nNew line")

# Read lines into list
with open("file.txt", "r") as f:
    lines = f.readlines()
```

---

## Classes & OOP

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def __str__(self):
        return f"Dog({self.name}, {self.age})"

# Create instance
dog = Dog("Rex", 3)
dog.bark()              # "Rex says woof!"
print(dog)              # Dog(Rex, 3)

# Inheritance
class Puppy(Dog):
    def __init__(self, name):
        super().__init__(name, 0)

    def bark(self):
        return f"{self.name} says yip!"
```

---

## Modules & Imports

```python
import math
import random
import os
import json
from datetime import datetime

math.sqrt(16)           # 4.0
math.pi                 # 3.14159
random.randint(1, 10)   # random int 1-10
random.choice(["a","b"]) # random item

os.getcwd()             # current directory
os.listdir(".")         # list files
os.path.exists("file")  # check if exists

datetime.now()          # current date/time
```

---

## JSON

```python
import json

# Dict to JSON string
data = {"name": "Phil", "age": 25}
json_str = json.dumps(data, indent=2)

# JSON string to dict
parsed = json.loads(json_str)

# Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Write JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## Requests (HTTP)

```python
import requests

# GET
response = requests.get("https://api.github.com", timeout=5)
response.status_code    # 200
response.json()         # parse JSON response

# GET with params
params = {"q": "python"}
response = requests.get(url, params=params)

# POST
data = {"name": "Phil"}
response = requests.post(url, json=data)

# Headers
headers = {"Authorization": "Bearer token"}
response = requests.get(url, headers=headers)

# Error handling
response.raise_for_status()  # raises error for 4xx/5xx
```

---

## List of useful built-in functions

```python
len(x)          # length
type(x)         # data type
print(x)        # output
input("msg")    # user input
range(n)        # sequence of numbers
int/float/str/bool(x)  # type conversion
sorted(x)       # return sorted copy
reversed(x)     # return reversed iterator
enumerate(x)    # index + value pairs
zip(a, b)       # pair two iterables
map(fn, x)      # apply function to each item
filter(fn, x)   # filter items by condition
sum(x)          # total
min(x)          # lowest value
max(x)          # highest value
abs(x)          # absolute value
round(x, n)     # round to n decimal places
isinstance(x, type)  # check type
```

---

## Common string methods

```python
.upper()        .lower()        .capitalize()
.strip()        .lstrip()       .rstrip()
.replace(a, b)  .split(sep)     .join(list)
.startswith()   .endswith()     .find()
.count()        .format()       .encode()
.isdigit()      .isalpha()      .isspace()
```

---

## Common list methods

```python
.append()       .insert()       .remove()
.pop()          .clear()        .copy()
.sort()         .reverse()      .extend()
.index()        .count()
```

---

*Keep this handy — updated as I learn more.*
