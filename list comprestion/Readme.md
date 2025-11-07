# Python List Comprehension

This directory contains practice exercises for learning list comprehension in Python. These examples demonstrate how to create lists concisely using comprehension syntax.

## Contents

1. [What is List Comprehension?](#what-is-list-comprehension)
2. [Syntax](#syntax)
3. [Practice Examples](#practice-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What is List Comprehension?

```python
# list comprehension = a concise way to create lists in Python
#                      compact and easier way to read than traditional loops
#                      [expression for value in iterable if condition]
```

**List comprehension** provides a concise way to create lists. It's more readable and often faster than traditional for loops with append.

**Traditional approach:**
```python
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
```

**List comprehension:**
```python
doubles = [x * 2 for x in range(1, 11)]
```

---

## Syntax

### Basic Syntax
```python
[expression for value in iterable]
```

### With Condition
```python
[expression for value in iterable if condition]
```

**Components:**
- **expression**: What to do with each value
- **value**: Variable representing each item
- **iterable**: Collection to iterate through
- **condition** (optional): Filter items

---

## Practice Examples

### Traditional vs List Comprehension

**Traditional:**
```python
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**List comprehension:**
```python
doubles = [x * 2 for x in range(1, 11)]
print(doubles)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

### Example 1: Basic Operations

```python
# Triples
triples = [y * 3 for y in range(1, 11)]
print(triples)
# Output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Squares
squares = [y * y for y in range(1, 11)]
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

### Example 2: String Operations

```python
fruits = ["apple", "orange", "banana"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
# Output: ['APPLE', 'ORANGE', 'BANANA']
```

**With print (side effect):**
```python
fruits = [print(fruit.capitalize()) for fruit in ["apple", "orange", "banana"]]
# Prints: Apple Orange Banana (each on new line)

fruit_char = [print(fruit[0]) for fruit in ["apple", "orange", "banana"]]
# Prints: a o b (each on new line)
```

**Note:** Using `print()` in comprehension is valid but not typical - it's done for side effects, not to create a useful list.

---

### Example 3: Filtering with Conditions

```python
numbers = [1, -2, 3, -5, 12, -24, 14, 4, -7]

positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)
# Output: [1, 3, 12, 14, 4]

negative_nums = [num for num in numbers if num <= 0]
print(negative_nums)
# Output: [-2, -5, -24, -7]

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
# Output: [-2, 12, -24, 14, 4]

odd_nums = [print(num) for num in numbers if num % 2 == 1]
# Prints odd numbers: 1 3 -5 -7
```

---

### Example 4: Grade Filtering

```python
grades = [85, 76, 59, 78, 49, 30, 78, 63]
pass_grade = [print(grade, end=" ") for grade in grades if grade >= 75]
# Prints: 85 76 78 78
```

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python list_compression.py
   ```

---

## Key Concepts Learnt

### List Comprehension Benefits
- **Concise**: One line instead of multiple
- **Readable**: Clear intent once familiar
- **Faster**: Generally more efficient than loops
- **Pythonic**: Preferred Python style

### Basic Comprehension
```python
[expression for item in iterable]
```
- Creates new list
- Applies expression to each item
- Returns resulting list

### Comprehension with Filtering
```python
[expression for item in iterable if condition]
```
- Only includes items that meet condition
- Combines mapping and filtering
- More concise than filter() + map()

### Common Patterns

**Transformation:**
```python
[x * 2 for x in numbers]        # Double each
[s.upper() for s in strings]    # Uppercase each
[x ** 2 for x in range(10)]     # Square each
```

**Filtering:**
```python
[x for x in numbers if x > 0]           # Positive only
[x for x in numbers if x % 2 == 0]      # Even only
[s for s in strings if len(s) > 5]     # Long strings
```

**Transformation + Filtering:**
```python
[x * 2 for x in numbers if x > 0]       # Double positive numbers
[s.upper() for s in strings if 'a' in s] # Uppercase strings with 'a'
```

---

## Comparison: Traditional vs Comprehension

### Example 1: Basic Transformation
**Traditional:**
```python
result = []
for x in range(10):
    result.append(x * 2)
```

**Comprehension:**
```python
result = [x * 2 for x in range(10)]
```

### Example 2: With Condition
**Traditional:**
```python
result = []
for x in numbers:
    if x > 0:
        result.append(x)
```

**Comprehension:**
```python
result = [x for x in numbers if x > 0]
```

### Example 3: Transformation + Filter
**Traditional:**
```python
result = []
for x in numbers:
    if x > 0:
        result.append(x * 2)
```

**Comprehension:**
```python
result = [x * 2 for x in numbers if x > 0]
```

---

## Additional Examples

### Character Extraction
```python
word = "Python"
chars = [char for char in word]
# ['P', 'y', 't', 'h', 'o', 'n']
```

### Range Operations
```python
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### String Lengths
```python
words = ["hi", "hello", "hey", "howdy"]
lengths = [len(word) for word in words]
# [2, 5, 3, 5]
```

### Conditional Expression
```python
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']
```

---
