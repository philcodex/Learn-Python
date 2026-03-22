"""
PYTHON LOOPS – COMPLETE PRACTICE FILE
Author: Phil-style structured learning 😄

HOW TO USE:
- Run the file
- Uncomment sections one by one
- Modify exercises to practice
"""

# ==============================
# 1. BASIC FOR LOOP
# ==============================
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Exercise:
# Print only "banana"


# ==============================
# 2. RANGE LOOP
# ==============================
for i in range(5):
    print(i)

# Exercise:
# Print numbers 1–10


# ==============================
# 3. WHILE LOOP
# ==============================
i = 0
while i < 5:
    print(i)
    i += 1

# Exercise:
# Count down from 10 to 1


# ==============================
# 4. LOOP WITH ELSE
# ==============================
for i in range(3):
    print(i)
else:
    print("Done")

# Exercise:
# Print "Finished loop" after counting to 5


# ==============================
# 5. LOOP THROUGH STRING
# ==============================
for char in "python":
    print(char)

# Exercise:
# Count vowels in a string


# ==============================
# 6. BREAK
# ==============================
for i in range(10):
    if i == 5:
        break
    print(i)

# Exercise:
# Stop loop when number = 7


# ==============================
# 7. CONTINUE
# ==============================
for i in range(5):
    if i == 2:
        continue
    print(i)

# Exercise:
# Print only odd numbers


# ==============================
# 8. NESTED LOOPS
# ==============================
for i in range(3):
    for j in range(2):
        print(i, j)

# Exercise:
# Print multiplication table (1–5)


# ==============================
# 9. PASS
# ==============================
for i in range(5):
    pass

# Exercise:
# Add logic later


# ==============================
# 10. FILTERING IN LOOP
# ==============================
numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n % 2 == 0:
        print(n)

# Exercise:
# Print numbers divisible by 3


# ==============================
# 11. COUNTING PATTERN (IMPORTANT)
# ==============================
nums = [200, 500, 404, 200]

errors = 0
for n in nums:
    if n != 200:
        errors += 1

print("Errors:", errors)

# Exercise:
# Count numbers greater than 100


# ==============================
# 12. LOOP DICTIONARY
# ==============================
user = {"name": "Phil", "role": "Engineer"}

for key, value in user.items():
    print(key, value)

# Exercise:
# Print only keys


# ==============================
# 13. API LOOP (REAL WORLD 🔥)
# ==============================
import requests

urls = ["https://api.github.com"]

for url in urls:
    r = requests.get(url)
    print(url, r.status_code)

# Exercise:
# Print "OK" if 200 else "ERROR"


# ==============================
# 14. LIST COMPREHENSION
# ==============================
nums = [1, 2, 3, 4]

squared = [n**2 for n in nums]
print(squared)

# Exercise:
# Create list of even numbers


# ==============================
# 15. ENUMERATE
# ==============================
names = ["Phil", "Vicky"]

for i, name in enumerate(names):
    print(i, name)

# Exercise:
# Start index from 1 (hint: enumerate(..., start=1))


# ==============================
# 16. ZIP
# ==============================
names = ["Phil", "Vicky"]
ages = [35, 34]

for name, age in zip(names, ages):
    print(name, age)

# Exercise:
# Combine 2 lists


# ==============================
# 17. INFINITE LOOP (CONTROLLED)
# ==============================
count = 0

while True:
    print("Running...", count)
    count += 1

    if count == 5:
        break

# Exercise:
# Change stop condition


# ==============================
# 18. USER INPUT LOOP
# ==============================
# Uncomment to use (interactive)
"""
while True:
    text = input("Type exit: ")

    if text == "exit":
        break
"""

# Exercise:
# Count number of inputs


# ==============================
# 19. PERFORMANCE LOOP
# ==============================
for i in range(100000):
    pass

# Exercise:
# Compare with list comprehension


# ==============================
# 20. FINAL PROJECT – HTTP CHECKER 🚀
# ==============================
urls = [
    "https://api.github.com",
    "https://httpbin.org/status/500",
    "https://httpbin.org/status/404"
]

failures = 0

for url in urls:
    try:
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            print(url, "OK")

        elif r.status_code == 404:
            print(url, "NOT FOUND")
            failures += 1

        else:
            print(url, "ERROR", r.status_code)
            failures += 1

    except requests.exceptions.RequestException as e:
        print(url, "FAILED", e)
        failures += 1

print("Total failures:", failures)

# Exercise:
# - Add logging
# - Save results to file
# - Add retry logic
