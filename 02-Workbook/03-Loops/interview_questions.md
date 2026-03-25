# Python Loop Interview Answers

A reference guide covering common Python loop questions — useful for interview prep and revision.

---

## 1. Basic `for` loop

**What does a `for` loop do in Python?**

A `for` loop iterates over each item in an iterable (such as a list, string, or range) and executes a block of code for each item.

**How is a `for` loop different from a `while` loop?**

A `for` loop is used when iterating over a known sequence or collection.
- [ ] A `while` loop is used when the loop should continue based on a condition and the number of iterations is not known in advance.

---

## 2. `range()`

**What does `range(5)` return?**

It returns a range object representing the sequence: `0, 1, 2, 3, 4`.

**How would you print numbers from 1 to 10?**

```python
for i in range(1, 11):
    print(i)
```

---

## 3. `while` loop

**When would you use a `while` loop instead of a `for` loop?**

When the number of iterations is unknown and depends on a condition, such as waiting for user input or retrying an operation until success.

**What can happen if you forget to update the loop variable?**

The loop may become infinite, causing the program to hang or consume resources.

---

## 4. Loop with `else`

**What does `else` do in a loop?**

The `else` block runs when the loop completes normally without hitting a `break`.

**When does the `else` block not run?**

When the loop exits early using `break`.

---

## 5. Loop through a string

**Why can a string be used in a loop?**

Because strings are iterable collections of characters.

**How would you count vowels in a word?**

```python
word = "python"
count = 0

for char in word:
    if char.lower() in "aeiou":
        count += 1

print(count)
```

---

## 6. `break`

**What does `break` do?**

It immediately exits the loop.

**Give a practical example of when you would use it.**

Stopping a search once a match is found in logs or data.

---

## 7. `continue`

**What does `continue` do?**

It skips the current iteration and moves to the next.

**How is it different from `break`?**

`continue` skips one iteration, while `break` exits the loop entirely.

---

## 8. Nested loops

**What is a nested loop?**

A loop inside another loop.

**What kind of problems usually need nested loops?**

Working with grids, comparing datasets, or generating combinations.

---

## 9. `pass`

**What does `pass` do?**

It is a placeholder that does nothing.

**Why might a developer use it?**

To define structure before implementing logic or avoid syntax errors.

---

## 10. Filtering in loops

**How do you print only values matching a condition?**

Use an `if` statement inside the loop.

**How would you print only even numbers from a list?**

```python
numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    if n % 2 == 0:
        print(n)
```

---

## 11. Counting pattern

**How do you count matching items in a loop?**

Use a counter variable and increment it when a condition is met.

**How would you count non-200 HTTP status codes?**

```python
statuses = [200, 500, 404, 200]

errors = 0
for s in statuses:
    if s != 200:
        errors += 1

print(errors)
```

---

## 12. Dictionary loops

**How do you loop through both keys and values in a dictionary?**

```python
for key, value in my_dict.items():
    print(key, value)
```

**How do you print only keys?**

```python
for key in my_dict.keys():
    print(key)
```

---

## 13. API loop

**Why is looping through URLs useful in operations work?**

It allows you to check multiple services, monitor endpoints, and validate system health.

**How should you handle request failures?**

Use `try/except` blocks, timeouts, and handle different status codes appropriately.

---

## 14. List comprehension

**What is a list comprehension?**

A concise way to create lists using a single line of code.

**When should you use a normal loop instead?**

When the logic is complex or readability would suffer.

---

## 15. `enumerate()`

**Why use `enumerate()`?**

To access both the index and value while looping.

**How do you start the counter from 1?**

```python
for i, value in enumerate(items, start=1):
    print(i, value)
```

---

## 16. `zip()`

**What does `zip()` do?**

It combines multiple iterables into pairs.

**What happens if the lists are different lengths?**

It stops at the shortest list.

---

## 17. Infinite loop

**What is an infinite loop?**

A loop that never ends because its condition is always true.

**How do you safely control one?**

Use a `break` condition or counter.

---

## 18. Input loop

**How can you repeatedly ask for user input until they type `exit`?**

```python
while True:
    text = input("Type exit to quit: ")
    if text == "exit":
        break
```

**What is the risk of badly designed input loops?**

They can trap users or create infinite loops.

---

## 19. Performance

**Why can large loops become slow?**

Because each iteration consumes time and resources.

**When is list comprehension faster?**

When performing simple transformations, as it is optimised and more concise.

---

## 20. HTTP status checker

**How would you loop through URLs and report status codes?**

```python
import requests

urls = ["https://api.github.com"]

for url in urls:
    r = requests.get(url)
    print(url, r.status_code)
```

**How would you improve a basic checker for production use?**

- Add timeouts
- Add retries
- Log results
- Handle exceptions
- Output results to a file or monitoring system
