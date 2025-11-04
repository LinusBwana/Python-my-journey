# Python For Loops Practice

This reposdirectoryitory contains practice exercises for learning for loops in Python. These examples demonstrate how to execute code a fixed number of times by iterating over sequences.

## Contents

1. [What are For Loops?](#what-are-for-loops)
2. [For Loop Syntax](#for-loop-syntax)
3. [Practice Examples](#practice-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are For Loops?

```python
# for loops execute a block of code a fixed number of times
# You can iterate over a range, string, sequence etc
```

A **for loop** is used for iterating over a sequence (such as a list, tuple, string, or range). Unlike while loops that run until a condition is false, for loops run for a predetermined number of times based on the length of the sequence.

For loops are useful for:
- Executing code a specific number of times
- Iterating through collections (lists, strings, tuples)
- Processing each element in a sequence
- Creating countdowns or countups

---

## For Loop Syntax

```python
for variable in sequence:
    # code to execute for each item
```

**Key components:**
- `variable` - Holds the current item from the sequence
- `sequence` - The collection to iterate over (range, string, list, etc.)
- `range()` - Generates a sequence of numbers

---

## Practice Examples

### Example 1: Basic Range Loop

Prints numbers from 1 to 10.

```python
for x in range(1, 11):
    print(x)
print("HAPPY NEW YEAR")
```

**Output:**
```
1
2
3
4
5
6
7
8
9
10
HAPPY NEW YEAR
```

**How it works:** 
- `range(1, 11)` generates numbers from 1 to 10 (end value is exclusive)
- The loop executes 10 times, printing each number
- After the loop completes, it prints "HAPPY NEW YEAR"

---

### Example 2: Reversed Range Loop

Counts down from 10 to 1.

```python
for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR")
```

**Output:**
```
10
9
8
7
6
5
4
3
2
1
HAPPY NEW YEAR
```

**How it works:** 
- `reversed()` function reverses the sequence from `range(1, 11)`
- Creates a countdown effect from 10 to 1
- Useful for countdowns or processing items in reverse order

---

### Example 3: Range with Step

Prints only odd numbers from 1 to 9.

```python
for x in range(1, 11, 2):
    print(x)
print("HAPPY NEW YEAR")
```

**Output:**
```
1
3
5
7
9
HAPPY NEW YEAR
```

**How it works:** 
- `range(1, 11, 2)` generates numbers starting at 1, ending before 11, with a step of 2
- The third parameter (2) is the **step** value - it skips every other number
- Results in only odd numbers being printed

---

### Example 4: Iterating Over a String

Prints each character of a credit card number.

```python
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
```

**Output:**
```
1
2
3
4
-
5
6
7
8
-
9
0
1
2
-
3
4
5
6
```

**How it works:** 
- Strings are sequences in Python, so you can iterate over them
- The loop visits each character in the string, including the dashes
- Each character is printed on a new line

---

## Understanding `range()` Function

The `range()` function is commonly used with for loops to generate sequences of numbers.

### Syntax Options

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1, incrementing by step
```

### Examples

| Code | Output | Explanation |
|------|--------|-------------|
| `range(5)` | `0, 1, 2, 3, 4` | Starts at 0, ends before 5 |
| `range(2, 6)` | `2, 3, 4, 5` | Starts at 2, ends before 6 |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` | Starts at 0, ends before 10, step of 2 |
| `range(10, 0, -1)` | `10, 9, 8, ..., 1` | Counts down from 10 to 1 |

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the Python file:
   ```bash
   python for_loops.py
   ```

---

## Key Concepts Learnt

### For Loop Fundamentals
- **Basic syntax**: `for variable in sequence:`
- **Fixed iterations**: Loops run for a predetermined number of times
- **Automatic iteration**: No need to manually increment counters
- **Cleaner than while loops**: When you know exactly how many times to loop

### Working with `range()`
- **Single parameter**: `range(n)` generates 0 to n-1
- **Two parameters**: `range(start, stop)` generates start to stop-1
- **Three parameters**: `range(start, stop, step)` with custom increment
- **Exclusive end**: The stop value is never included in the sequence

### Iterating Over Sequences
- **Strings**: Can iterate over each character
- **Lists**: Can iterate over each element (coming in future lessons)
- **Tuples**: Can iterate over each item (coming in future lessons)
- **Any iterable**: For loops work with any iterable object in Python

### Advanced Techniques
- **`reversed()`**: Reverses any sequence
- **Step values**: Positive steps count up, negative steps count down
- **Nested loops**: Can place loops inside other loops (for advanced use)

---

## Common For Loop Patterns

### Basic Counter
```python
for i in range(10):
    print(i)  # Prints 0 to 9
```

### Countdown Timer
```python
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```

### Even Numbers Only
```python
for i in range(0, 20, 2):
    print(i)  # Prints 0, 2, 4, ..., 18
```

### String Character Processing
```python
message = "Hello"
for char in message:
    print(char.upper())  # Prints each letter in uppercase
```

### Sum of Numbers
```python
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")  # Sum of 1 to 100
```

---

## For Loop vs While Loop

### Use For Loop When:
- You know exactly how many iterations you need
- You're iterating over a collection (string, list, etc.)
- You want cleaner, more readable code for counting

```python
# For loop - cleaner
for i in range(10):
    print(i)
```

### Use While Loop When:
- You don't know how many iterations you'll need
- You're waiting for a condition to change
- You need input validation

```python
# While loop - better for unknown iterations
password = ""
while password != "secret":
    password = input("Enter password: ")
```

---