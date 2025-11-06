# Python Nested Loops Practice

This directory contains practice exercises for learning nested loops in Python. These examples demonstrate how to use loops within other loops to create patterns and grids.

## Contents

1. [What are Nested Loops?](#what-are-nested-loops)
2. [Nested Loop Syntax](#nested-loop-syntax)
3. [Practice Examples](#practice-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are Nested Loops?

```python
# nested loop = a loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:
```

A **nested loop** is a loop placed inside another loop. The structure consists of:
- **Outer loop**: The main loop that controls how many times the inner loop runs
- **Inner loop**: The loop that executes completely for each iteration of the outer loop

For each iteration of the outer loop, the inner loop completes all of its iterations.

---

## Nested Loop Syntax

```python
for outer_variable in outer_sequence:
    # Outer loop code
    for inner_variable in inner_sequence:
        # Inner loop code
    # More outer loop code
```

**Execution pattern:**
1. Outer loop starts first iteration
2. Inner loop runs all its iterations
3. Outer loop moves to next iteration
4. Inner loop runs all its iterations again
5. Process repeats until outer loop finishes

---

## Practice Examples

### Example 1: Number Pattern

Prints rows of numbers from 1 to 9.

```python
for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()
```

**Output:**
```
123456789
123456789
123456789
```

**How it works:**
- **Outer loop** (`x in range(3)`): Runs 3 times (creates 3 rows)
- **Inner loop** (`y in range(1, 10)`): Runs 9 times per outer iteration (prints numbers 1-9)
- **`end=""`**: Keeps numbers on the same line without spaces
- **`print()`**: After inner loop completes, moves to next line

**Step-by-step execution:**
```
Outer iteration 1: Print 1,2,3,4,5,6,7,8,9, then newline
Outer iteration 2: Print 1,2,3,4,5,6,7,8,9, then newline
Outer iteration 3: Print 1,2,3,4,5,6,7,8,9, then newline
```

---

### Example 2: Custom Grid Pattern

Creates a customizable grid using user input for dimensions and symbol.

```python
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()
```

**Example Output (rows=4, columns=6, symbol='*'):**
```
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
```

**Example Output (rows=3, columns=8, symbol='#'):**
```
# # # # # # # # 
# # # # # # # # 
# # # # # # # # 
```

**How it works:**
- Takes three inputs: number of rows, columns, and symbol to use
- **Outer loop** (`x in range(rows)`): Controls number of rows
- **Inner loop** (`y in range(columns)`): Prints symbols for each column
- **`end=" "`**: Adds space between symbols on same line
- **`print()`**: Moves to new line after each row is complete

**Execution flow (for 3 rows, 4 columns):**
```
Row 1: Print symbol 4 times with spaces, then newline
Row 2: Print symbol 4 times with spaces, then newline
Row 3: Print symbol 4 times with spaces, then newline
```

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python nested_loop.py
   ```
3. For Example 2, enter the requested values when prompted

---

## Key Concepts Learnt

### Nested Loop Fundamentals
- **Definition**: A loop inside another loop
- **Structure**: Outer loop contains inner loop
- **Execution order**: Inner loop completes fully for each outer loop iteration
- **Use cases**: Creating grids, patterns, matrices, tables

### Loop Control and Output
- **`end=""` parameter**: Controls what prints after each print statement
  - `end=""` - No space or newline (prints continuously)
  - `end=" "` - Adds space between items
  - `end="\n"` - Adds newline (default behavior)
- **`print()` with no arguments**: Prints a newline character
- **Combining both**: Using `end` in inner loop, plain `print()` after inner loop

### Understanding `end` Parameter

The `end` parameter in `print()` determines what character(s) are printed after the main content:

```python
# Default behavior (end="\n")
print("Hello")
print("World")
# Output:
# Hello
# World

# Using end="" (no space or newline)
print("Hello", end="")
print("World")
# Output: HelloWorld

# Using end=" " (space)
print("Hello", end=" ")
print("World")
# Output: Hello World
```

### Pattern Creation
- **Rows**: Controlled by outer loop iterations
- **Columns**: Controlled by inner loop iterations
- **Symbols**: Can be any character or string
- **Spacing**: Managed with `end` parameter

### Iteration Counting
For nested loops with `range(m)` outer and `range(n)` inner:
- **Outer loop runs**: `m` times
- **Inner loop runs**: `n` times per outer iteration
- **Total inner iterations**: `m × n` times

**Example:**
```python
for x in range(3):      # Runs 3 times
    for y in range(4):  # Runs 4 times per outer iteration
        print("*")      # Executes 3 × 4 = 12 times total
```

---

## Common Nested Loop Patterns

### Multiplication Table
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()
```

### Right Triangle Pattern
```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
```

### Inverted Triangle Pattern
```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# Output:
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
```

### Number Grid
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()
# Output:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
```

### Checkerboard Pattern
```python
for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()
# Output:
# ■ □ ■ □
# □ ■ □ ■
# ■ □ ■ □
# □ ■ □ ■
```

---

## Understanding Execution Order

### Visualization of Nested Loop Execution

For this code:
```python
for x in range(2):
    for y in range(3):
        print(f"x={x}, y={y}")
    print("Inner loop complete")
```

**Execution sequence:**
```
x=0, y=0
x=0, y=1
x=0, y=2
Inner loop complete
x=1, y=0
x=1, y=1
x=1, y=2
Inner loop complete
```

**Key observation:** The inner loop variable (`y`) changes faster than the outer loop variable (`x`).

---

## Nested Loop vs Single Loop

### When to Use Nested Loops
- Creating 2D patterns (grids, matrices)
- Processing multi-dimensional data
- Comparing each item with every other item
- Creating tables or structured output

### When to Use Single Loop
- Processing a single list or sequence
- Simple counting or iteration
- One-dimensional operations

**Example comparison:**

Single loop (1D):
```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4 (5 iterations)
```

Nested loop (2D):
```python
for i in range(5):
    for j in range(5):
        print(i, j)
# Output: 25 combinations (5 × 5 iterations)
```

---

**Happy Coding!**