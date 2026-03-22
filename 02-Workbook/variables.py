# ============================================================
# Variables & Data Types — Tutorial
# ============================================================


# ---- 1. WHAT IS A VARIABLE ----
# A variable is a container for storing a value
# You create one by giving it a name and assigning a value with =

name = "Phil"
age = 25
height = 6.02
is_developer = True

print(name)
print(age)
print(height)
print(is_developer)


# ---- 2. THE 4 BASIC DATA TYPES ----

# str  — String    — text, wrapped in quotes
# int  — Integer   — whole numbers
# float — Float   — decimal numbers
# bool — Boolean   — True or False only


# ---- 3. STRINGS (str) ----
# Text values — use single or double quotes

first_name = "Phil"
last_name = 'Carroll'
sentence = "I am learning Python"

print(first_name)
print(last_name)
print(sentence)

# Strings can use single or double quotes — just be consistent
# Use double quotes when your string contains an apostrophe
message = "it's a great day"
print(message)


# ---- 4. INTEGERS (int) ----
# Whole numbers — no decimal point

year = 2026
score = 100
temperature = -5
population = 1000000

print(year)
print(score)
print(temperature)
print(population)

# Basic arithmetic with integers
print(10 + 3)   # 13  addition
print(10 - 3)   # 7   subtraction
print(10 * 3)   # 30  multiplication
print(10 // 3)  # 3   integer division (no decimal)
print(10 % 3)   # 1   modulus (remainder)


# ---- 5. FLOATS (float) ----
# Numbers with a decimal point

price = 9.99
pi = 3.14159
weight = 72.5
temperature = -2.5

print(price)
print(pi)
print(weight)

# Arithmetic with floats
print(9.99 + 0.01)   # 10.0
print(10.0 / 3)      # 3.3333...
print(2 ** 8)        # 256 — exponent (power of)

# Mixing int and float always returns a float
print(5 + 2.0)       # 7.0


# ---- 6. BOOLEANS (bool) ----
# Only two possible values — True or False
# Note: always capitalised in Python

is_logged_in = True
has_error = False
is_admin = True

print(is_logged_in)
print(has_error)

# Booleans are often the result of comparisons
print(10 > 5)    # True
print(10 < 5)    # False
print(10 == 10)  # True
print(10 != 10)  # False


# ---- 7. CHECKING THE TYPE OF A VARIABLE ----
# Use type() to see what data type a variable is

print(type("Phil"))    # <class 'str'>
print(type(25))        # <class 'int'>
print(type(5.11))      # <class 'float'>
print(type(True))      # <class 'bool'>

# Or check a variable directly
name = "Phil"
age = 25
print(type(name))
print(type(age))


# ---- 8. TYPE CONVERSION ----
# You can convert between types using int(), float(), str(), bool()

# str to int
age_string = "25"
age_number = int(age_string)
print(age_number + 5)   # 30 — now we can do maths on it

# int to float
whole = 10
decimal = float(whole)
print(decimal)          # 10.0

# int to str
score = 100
message = "Your score is " + str(score)
print(message)

# float to int — drops the decimal, does NOT round
print(int(9.99))   # 9
print(int(3.1))    # 3


# ---- 9. NAMING RULES ----
# Variable names must follow these rules:
#   - Start with a letter or underscore
#   - No spaces — use underscores instead (snake_case)
#   - Case sensitive — name and Name are different variables
#   - Cannot use reserved words (if, for, while, print etc.)

first_name = "Phil"     # correct — snake_case
_private = "hidden"     # correct — underscore prefix
firstName = "Phil"      # works but not Python style (camelCase)

# These would cause errors:
# 2name = "Phil"        # cannot start with a number
# my-name = "Phil"      # hyphens not allowed
# for = "Phil"          # reserved word


# ---- 10. MULTIPLE ASSIGNMENT ----
# Assign multiple variables on one line

x, y, z = 1, 2, 3
print(x, y, z)   # 1 2 3

# Assign the same value to multiple variables
a = b = c = 0
print(a, b, c)   # 0 0 0