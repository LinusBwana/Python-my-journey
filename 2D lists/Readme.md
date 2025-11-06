# Python 2D Collections Practice

This directory contains practice exercises for learning 2D collections in Python. These examples demonstrate how to work with lists of lists, lists of tuples, and nested data structures.

## Contents

1. [What are 2D Collections?](#what-are-2d-collections)
2. [2D Lists](#2d-lists)
3. [2D Tuples](#2d-tuples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are 2D Collections?

A **2D collection** (two-dimensional collection) is a collection that contains other collections as its elements. Think of it as a table or grid with rows and columns.

**Structure:**
- **Outer collection**: The main container (like rows in a table)
- **Inner collections**: The nested items (like columns in each row)

**Use cases:**
- Storing tables of data
- Representing grids or matrices
- Organizing related groups of data
- Creating game boards

---

## 2D Lists

### Creating 2D Collections

You can create 2D collections in multiple ways:

#### Method 1: List of Lists
```python
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
```

#### Method 2: List of Tuples
```python
groceries = [("apple", "orange", "banana", "coconut"),
             ("celery", "carrots", "potatoes"),
             ("chicken", "fish", "turkey")]
```

**Note:** The inner collections can be lists, tuples, or sets. The choice depends on whether you need the inner collections to be changeable.

### Accessing Elements in 2D Collections

```python
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# Modify an element
fruits[0] = "mango"

# Access entire collection
print(groceries)
# Output: [['mango', 'orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]

# Access first inner collection
print(groceries[0])
# Output: ['mango', 'orange', 'banana', 'coconut']

# Access specific element (row 2, column 1)
print(groceries[2][1])
# Output: fish
```

**Indexing syntax:**
- `groceries[i]` - Access entire inner collection at index i
- `groceries[i][j]` - Access element at row i, column j

### Iterating Through 2D Collections

```python
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
```

**Output:**
```
apple orange banana coconut 
celery carrots potatoes 
chicken fish turkey 
```

**How it works:**
1. **Outer loop**: Iterates through each inner collection (fruits, vegetables, meats)
2. **Inner loop**: Iterates through items in current collection
3. **`end=" "`**: Prints items on same line with space separator
4. **`print()`**: Moves to new line after each collection

---

## 2D Tuples

### Phone Keypad Example

A practical example using a 2D tuple to represent a phone keypad.

```python
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for i in row:
        print(i, end="   ")
    print()
```

**Output:**
```
1   2   3   
4   5   6   
7   8   9   
*   0   #   
```

**How it works:**
- **Outer tuple**: Contains 4 rows (immutable)
- **Inner tuples**: Each row contains 3 elements
- **Mixed types**: Numbers and strings can coexist
- **Nested iteration**: Outer loop for rows, inner loop for elements
- **Formatting**: `end="   "` adds spacing between numbers

**Visual representation:**
```
Row 0: (1, 2, 3)
Row 1: (4, 5, 6)
Row 2: (7, 8, 9)
Row 3: ("*", 0, "#")
```

**Accessing elements:**
```python
print(num_pad[0])      # (1, 2, 3) - First row
print(num_pad[1][1])   # 5 - Row 1, Column 1
print(num_pad[3][0])   # * - Row 3, Column 0
```

---

## How to Run

1. Navigate to the project directory
2. Run either Python file:
   ```bash
   python 2D_lists.py
   python 2D_Tuple_exercise.py
   ```

---

## Key Concepts Learnt

### Understanding 2D Collections
- **Definition**: A collection containing other collections
- **Structure**: Outer collection with inner collections
- **Analogy**: Like a table with rows and columns
- **Flexibility**: Inner collections can be lists, tuples, or sets

### Creating 2D Collections
- **Method 1**: Create separate collections, then combine them
- **Method 2**: Define all collections inline
- **Mixed types**: Outer and inner collections can be different types
- **Example**: List of tuples, tuple of lists, etc.

### Accessing Elements
- **Single index**: `collection[i]` accesses entire inner collection
- **Double index**: `collection[i][j]` accesses specific element
- **Row and column**: First index is row, second is column
- **Zero-based**: Both indices start at 0

### Modifying 2D Collections
- **If outer is list**: Can modify, add, or remove inner collections
- **If inner is list**: Can modify individual elements
- **If inner is tuple**: Cannot modify elements (immutable)
- **Reference changes**: Modifying original list affects 2D collection

**Example:**
```python
fruits = ["apple", "orange"]
groceries = [fruits, ["celery"]]
fruits[0] = "mango"  # Changes reflected in groceries
print(groceries)  # [['mango', 'orange'], ['celery']]
```

### Nested Iteration
- **Outer loop**: Processes each inner collection
- **Inner loop**: Processes each element in current collection
- **Pattern**: `for row in table: for item in row:`
- **Common use**: Printing grids, processing matrices

### Formatting Output
- **`end=" "`**: Print items on same line with spaces
- **`end="   "`**: Print with multiple spaces for alignment
- **`print()`**: Move to next line after inner loop
- **Creating grids**: Using nested loops with proper formatting

---

## Understanding Indexing in 2D Collections

### Visual Indexing Guide

For this 2D collection:
```python
groceries = [["apple", "orange", "banana"],
             ["celery", "carrots"],
             ["chicken", "fish", "turkey"]]
```

**Index map:**
```
groceries[0][0] = "apple"     groceries[0][1] = "orange"    groceries[0][2] = "banana"
groceries[1][0] = "celery"    groceries[1][1] = "carrots"
groceries[2][0] = "chicken"   groceries[2][1] = "fish"      groceries[2][2] = "turkey"
```

**Accessing patterns:**
```python
groceries[0]      # ['apple', 'orange', 'banana'] - entire first row
groceries[1]      # ['celery', 'carrots'] - entire second row
groceries[0][0]   # 'apple' - row 0, column 0
groceries[1][1]   # 'carrots' - row 1, column 1
groceries[2][2]   # 'turkey' - row 2, column 2
groceries[-1][-1] # 'turkey' - last row, last column
```

---

## Practical Examples

### Example 1: Student Grades
```python
grades = [["Alice", 85, 90, 88],
          ["Bob", 78, 82, 80],
          ["Charlie", 92, 88, 95]]

for student in grades:
    name = student[0]
    average = sum(student[1:]) / 3
    print(f"{name}: {average:.1f}")
```

**Output:**
```
Alice: 87.7
Bob: 80.0
Charlie: 91.7
```

### Example 2: Tic-Tac-Toe Board
```python
board = [["X", "O", "X"],
         ["O", "X", "O"],
         ["O", "X", "X"]]

for row in board:
    for cell in row:
        print(cell, end=" | ")
    print()
    print("-" * 11)
```

**Output:**
```
X | O | X | 
-----------
O | X | O | 
-----------
O | X | X | 
-----------
```

### Example 3: Seating Chart
```python
classroom = [("Alice", "Bob", "Charlie"),
             ("David", "Eve", "Frank"),
             ("Grace", "Henry", "Ivy")]

print("Row 1:", classroom[0])
print("Row 2:", classroom[1])
print("Row 3:", classroom[2])

# Find student
for row_num, row in enumerate(classroom):
    for col_num, student in enumerate(row):
        if student == "Eve":
            print(f"{student} sits at Row {row_num}, Seat {col_num}")
```

### Example 4: Multiplication Table
```python
table = []
for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    table.append(row)

for row in table:
    for num in row:
        print(f"{num:4}", end="")
    print()
```

**Output:**
```
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

---

## List vs Tuple for Inner Collections

### When to Use Lists Inside
```python
groceries = [["apple", "orange"],
             ["celery", "carrots"]]
```
- Inner collections need to change
- Adding/removing items from inner collections
- Modifying individual elements

### When to Use Tuples Inside
```python
groceries = [("apple", "orange"),
             ("celery", "carrots")]
```
- Inner collections should not change
- Data represents fixed records
- Better performance
- Protect data from accidental modification

### Example Comparison
```python
# List of lists - can modify
data = [["A", "B"], ["C", "D"]]
data[0][0] = "Z"  # Works fine
print(data)  # [['Z', 'B'], ['C', 'D']]

# List of tuples - cannot modify inner items
data = [("A", "B"), ("C", "D")]
data[0][0] = "Z"  # ERROR: tuples are immutable
```

---

## Common Patterns

### Pattern 1: Process All Elements
```python
for row in collection_2d:
    for item in row:
        # process item
```

### Pattern 2: Access with Indices
```python
for i in range(len(collection_2d)):
    for j in range(len(collection_2d[i])):
        print(collection_2d[i][j])
```

### Pattern 3: Enumerate Rows and Items
```python
for row_num, row in enumerate(collection_2d):
    for col_num, item in enumerate(row):
        print(f"[{row_num}][{col_num}] = {item}")
```

### Pattern 4: Build 2D Collection
```python
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * j)
    matrix.append(row)
```

---

**Happy Coding!**