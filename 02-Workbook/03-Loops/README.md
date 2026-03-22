# 03 — Loops

Covering Python loops — how they work, when to use each type, and practical examples.

---

## Files

| File | Description |
|------|-------------|
| `loops.py` | Core loop concepts and examples |
| `loops2.py` | Extended loop practice |
| `tutorials1.py` | Step by step loop tutorials |
| `tutorial-with-Qs.py` | Tutorials with questions to answer |
| `main.py` | Main script |
| `checklist.md` | Topics checklist |
| `interview_questions.md` | Loop interview Q&A |

---

## Key concepts covered

- `for` loops and `range()`
- `while` loops
- `break`, `continue`, `pass`
- Nested loops
- Loop with `else`
- `enumerate()` and `zip()`
- List comprehension
- Looping through strings, lists, and dictionaries

## Notes

### For loop vs While loop

| | `for` loop | `while` loop |
|---|---|---|
| **Use when** | You know how many iterations | You don't know how many iterations |
| **Iterates over** | A sequence (list, string, range) | A condition |
| **Stops when** | The sequence is exhausted | The condition becomes False |
| **Risk** | Low — bounded by the sequence | Higher — can become infinite |

**`for` loop** — use when iterating over a known collection:
```python
for i in range(5):
    print(i)
```

**`while` loop** — use when repeating until a condition is met:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
