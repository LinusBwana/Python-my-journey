# Python Iterables

This directory contains practice exercises for learning iterables in Python. These examples demonstrate what iterables are and how to loop through different types of collections.

## Contents

1. [What are Iterables?](#what-are-iterables)
2. [Types of Iterables](#types-of-iterables)
3. [Practice Examples](#practice-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are Iterables?

```python
# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated
# over in a loop
```

An **iterable** is any Python object that can be looped over using a for loop. It returns its elements one at a time, making it possible to process each item sequentially.

**Common iterables in Python:**
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- Files
- Ranges

**Key characteristic:** Can be used in a for loop.

---

## Types of Iterables

### Summary Table

| Type | Syntax | Iterable? | Ordered? | Mutable? | Example |
|------|--------|-----------|----------|----------|---------|
| String | `""` | Yes | Yes | No | `"Hello"` |
| List | `[]` | Yes | Yes | Yes | `[1, 2, 3]` |
| Tuple | `()` | Yes | Yes | No | `(1, 2, 3)` |
| Set | `{}` | Yes | No | Yes | `{1, 2, 3}` |
| Dictionary | `{}` | Yes | Yes (Python 3.7+) | Yes | `{"a": 1}` |
| Range | `range()` | Yes | Yes | No | `range(5)` |

**Note:** Sets are iterables but the order of iteration is not guaranteed (though in Python 3.7+ they maintain insertion order in CPython implementation).

---

## Practice Examples

### Example 1: Iterating Through a String (Commented)

```python
name = "Linus Bwana"
for character in name:
    print(character, end=" ")
```

**Output:**
```
L i n u s   B w a n a 
```

**How it works:**
- **Strings are iterables**: Each character can be accessed one at a time
- **For loop**: Iterates through each character
- **`end=" "`**: Prints characters on same line with space separator
- **Space character**: The space in "Linus Bwana" is also printed

---

### Example 2: Iterating Through a Dictionary

```python
my_dictionary = {"A": 1, "b": 2, "c": 3}

for key, value in my_dictionary.items():
    print(f"{key} : {value}")
```

**Output:**
```
A : 1
b : 2
c : 3
```

**How it works:**
- **Dictionary is iterable**: Can loop through its key-value pairs
- **`.items()`**: Returns pairs of keys and values
- **Tuple unpacking**: `key, value` receives each pair
- **Each iteration**: Gets one key-value pair from the dictionary

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python iterables.py
   ```

---

## Key Concepts Learnt

### Understanding Iterables
- **Definition**: Objects that can return elements one at a time
- **For loops**: Primary way to iterate through iterables
- **Sequential access**: Elements accessed in order (for ordered iterables)
- **One at a time**: Each iteration gives you one element

### Common Iterables
- **Strings**: Iterate through characters
- **Lists**: Iterate through elements
- **Tuples**: Iterate through elements
- **Sets**: Iterate through unique elements (unordered)
- **Dictionaries**: Iterate through keys, values, or pairs

### Dictionary Iteration
- **`.items()`**: Returns key-value pairs
- **`.keys()`**: Returns just keys
- **`.values()`**: Returns just values
- **Tuple unpacking**: Separating pairs into individual variables
- **Default**: Iterating dictionary without method gives keys only

### Iteration Syntax
- **Basic loop**: `for item in iterable:`
- **With index**: Using `enumerate()`
- **Multiple variables**: Unpacking tuples in loop
- **Nested loops**: Iterating through nested iterables

---

## Detailed Iteration Examples

### Iterating Through Different Types

#### String Iteration
```python
text = "Python"
for char in text:
    print(char)
# Output: P y t h o n (each on new line)
```

#### List Iteration
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# Output: 1 2 3 4 5 (each on new line)
```

#### Tuple Iteration
```python
colors = ("red", "green", "blue")
for color in colors:
    print(color)
# Output: red green blue (each on new line)
```

#### Set Iteration
```python
unique_numbers = {3, 1, 4, 1, 5, 9, 2, 6}
for num in unique_numbers:
    print(num)
# Output: Numbers in arbitrary order, duplicates removed
```

#### Range Iteration
```python
for i in range(5):
    print(i)
# Output: 0 1 2 3 4 (each on new line)
```

---

## Dictionary Iteration Methods

### Method 1: Iterate Over Keys (Default)
```python
my_dict = {"name": "Alice", "age": 25, "city": "NYC"}

for key in my_dict:
    print(key)
# Output: name age city
```

### Method 2: Iterate Over Keys (Explicit)
```python
for key in my_dict.keys():
    print(key)
# Output: name age city
```

### Method 3: Iterate Over Values
```python
for value in my_dict.values():
    print(value)
# Output: Alice 25 NYC
```

### Method 4: Iterate Over Key-Value Pairs
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: NYC
```

### Method 5: Using Keys to Get Values
```python
for key in my_dict:
    value = my_dict[key]
    print(f"{key} = {value}")
# Output:
# name = Alice
# age = 25
# city = NYC
```

---

## Advanced Iteration Techniques

### Using enumerate() for Index Access
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

**With custom start:**
```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry
```

### Using zip() to Iterate Multiple Iterables
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

### Iterating in Reverse
```python
numbers = [1, 2, 3, 4, 5]

for num in reversed(numbers):
    print(num)
# Output: 5 4 3 2 1
```

### Iterating with Conditions
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

---

## Understanding Tuple Unpacking in Loops

### What is Tuple Unpacking?

When you iterate over an iterable that contains tuples (or tuple-like objects), you can "unpack" them directly in the for loop.

**Example:**
```python
pairs = [(1, "one"), (2, "two"), (3, "three")]

# Without unpacking
for pair in pairs:
    print(pair[0], pair[1])

# With unpacking
for number, word in pairs:
    print(number, word)
```

### Dictionary .items() Returns Tuples
```python
my_dict = {"A": 1, "B": 2}

# .items() returns: dict_items([('A', 1), ('B', 2)])
# Each item is a tuple: ('A', 1)

for key, value in my_dict.items():
    # 'A', 1 gets unpacked into key and value
    print(key, value)
```

**Alternative without unpacking:**
```python
for item in my_dict.items():
    # item is a tuple
    print(item[0], item[1])  # Less readable
```

---

## Checking if Something is Iterable

### Using try-except
```python
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(is_iterable([1, 2, 3]))      # True
print(is_iterable("hello"))        # True
print(is_iterable(42))             # False
```

### Using collections.abc
```python
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance("hello", Iterable))    # True
print(isinstance(42, Iterable))         # False
```

---

## Common Iteration Patterns

### Pattern 1: Process Each Element
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    squared = num ** 2
    print(f"{num} squared is {squared}")
```

### Pattern 2: Accumulate Values
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Total: {total}")
```

### Pattern 3: Build New Collection
```python
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(doubled)  # [2, 4, 6, 8, 10]
```

### Pattern 4: Search for Element
```python
names = ["Alice", "Bob", "Charlie"]
search_name = "Bob"
found = False
for name in names:
    if name == search_name:
        found = True
        break
print(f"Found: {found}")
```

### Pattern 5: Filter Elements
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)  # [2, 4, 6, 8, 10]
```

---

## Iterables vs Iterators

### Iterable
- Object that can be looped over
- Has `__iter__()` method
- Returns an iterator

### Iterator
- Object that represents stream of data
- Has `__iter__()` and `__next__()` methods
- Keeps track of current position

**Example:**
```python
numbers = [1, 2, 3]  # List is an iterable

# Get an iterator from the iterable
iterator = iter(numbers)

# Use next() to get elements one at a time
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration error
```

**For loops handle this automatically:**
```python
for num in numbers:  # for loop creates iterator internally
    print(num)
```

---

## Performance Considerations

### Iterating Large Collections
```python
# Efficient - only loads one element at a time
for i in range(1000000):
    # process i
    pass

# Inefficient - creates entire list in memory
for i in [x for x in range(1000000)]:
    # process i
    pass
```

### Dictionary Iteration
```python
my_dict = {"a": 1, "b": 2, "c": 3}

# Efficient - iterate once
for key, value in my_dict.items():
    print(key, value)

# Inefficient - looks up each value
for key in my_dict:
    value = my_dict[key]
    print(key, value)
```

---

## Practical Examples

### Example: Count Character Frequency
```python
text = "hello world"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(f"'{char}': {count}")
```

### Example: Calculate Average
```python
grades = [85, 90, 78, 92, 88]
total = 0
count = 0

for grade in grades:
    total += grade
    count += 1

average = total / count
print(f"Average: {average}")
```

### Example: Find Maximum
```python
numbers = [45, 23, 67, 12, 89, 34]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum: {maximum}")
```

### Example: Reverse String
```python
text = "Python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)  # nohtyP
```