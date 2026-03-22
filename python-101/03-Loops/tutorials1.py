"""
PYTHON LOOPS – COMPLETE PRACTICE FILE (WITH ANSWERS)
"""

# ==============================
# 1. BASIC FOR LOOP
# ==============================
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        print(fruit)


# ==============================
# 2. RANGE LOOP
# ==============================
for i in range(1, 11):
    print(i)


# ==============================
# 3. WHILE LOOP
# ==============================
i = 10
while i > 0:
    print(i)
    i -= 1


# ==============================
# 4. LOOP WITH ELSE
# ==============================
for i in range(5):
    print(i)
else:
    print("Finished loop")


# ==============================
# 5. LOOP THROUGH STRING
# ==============================
word = "python"
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Vowels:", count)


# ==============================
# 6. BREAK
# ==============================
for i in range(10):
    if i == 7:
        break
    print(i)


# ==============================
# 7. CONTINUE
# ==============================
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


# ==============================
# 8. NESTED LOOPS
# ==============================
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")


# ==============================
# 9. PASS
# ==============================
for i in range(5):
    pass  # Placeholder for future logic


# ==============================
# 10. FILTERING IN LOOP
# ==============================
numbers = [1, 2, 3, 4, 5, 6, 9]

for n in numbers:
    if n % 3 == 0:
        print(n)


# ==============================
# 11. COUNTING PATTERN
# ==============================
nums = [50, 120, 200, 30, 500]

count = 0
for n in nums:
    if n > 100:
        count += 1

print("Greater than 100:", count)


# ==============================
# 12. LOOP DICTIONARY
# ==============================
user = {"name": "Phil", "role": "Engineer"}

for key in user.keys():
    print(key)


# ==============================
# 13. API LOOP
# ==============================
import requests

urls = ["https://api.github.com", "https://httpbin.org/status/500"]

for url in urls:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(url, "OK")
        else:
            print(url, "ERROR")
    except:
        print(url, "FAILED")


# ==============================
# 14. LIST COMPREHENSION
# ==============================
nums = [1, 2, 3, 4, 5, 6]

even_numbers = [n for n in nums if n % 2 == 0]
print(even_numbers)


# ==============================
# 15. ENUMERATE
# ==============================
names = ["Phil", "Vicky"]

for i, name in enumerate(names, start=1):
    print(i, name)


# ==============================
# 16. ZIP
# ==============================
names = ["Phil", "Vicky"]
ages = [35, 34]

pairs = list(zip(names, ages))
print(pairs)


# ==============================
# 17. INFINITE LOOP (CONTROLLED)
# ==============================
count = 0

while True:
    print("Running...", count)
    count += 1

    if count == 5:
        break


# ==============================
# 18. USER INPUT LOOP
# ==============================
# (Simulated version instead of input)
inputs = ["hello", "test", "exit"]

count = 0
for text in inputs:
    count += 1
    if text == "exit":
        break

print("Inputs entered:", count)


# ==============================
# 19. PERFORMANCE LOOP
# ==============================
# Basic comparison idea (not timing, just structure)

# For loop
result = []
for i in range(10):
    result.append(i*i)

# List comprehension
result2 = [i*i for i in range(10)]

print(result, result2)


# ==============================
# 20. FINAL PROJECT – HTTP CHECKER
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