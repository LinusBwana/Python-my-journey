# Python Collections: Lists, Sets, and Tuples

This directory contains practice exercises for learning Python collections. These examples demonstrate how to work with lists, sets, and tuples to store and manipulate multiple values.

## Contents

1. [What are Collections?](#what-are-collections)
2. [Lists](#lists)
3. [Sets](#sets)
4. [Tuples](#tuples)
5. [Comparison Table](#comparison-table)
6. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are Collections?

```python
# collection - single "variable" used to store multiple values
#               List = [] ordered and changeable. Duplicates OK
#               Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#               Tuple = () ordered and unchangeable. Duplicates OK. FASTER
```

A **collection** is a single variable that can store multiple values. Python has three main built-in collection types:

| Type | Symbol | Ordered | Changeable | Duplicates | Speed |
|------|--------|---------|------------|------------|-------|
| **List** | `[]` | Yes | Yes | Yes | Normal |
| **Set** | `{}` | No | Items immutable, but can add/remove | No | Normal |
| **Tuple** | `()` | Yes | No | Yes | Faster |

---

## Lists

**Lists** are ordered, changeable collections that allow duplicate values. They are the most versatile collection type.

### Creating and Accessing Lists

```python
fruits = ["apple", "banana", "coconut", "oranges", "water mellon", "pineapples", "guavas"]
```

### List Slicing

```python
print(fruits[2:7:2])    # ['coconut', 'water mellon', 'guavas']
print(fruits[::2])      # Every 2nd element from start to end
print(fruits[::-2])     # Every 2nd element in reverse
```

### Common List Operations

```python
# Get length
print(len(fruits))      # 7

# Check membership
print("oranges" in fruits)  # True

# Modify element
fruits[3] = "tomatoes"  # Changes "oranges" to "tomatoes"

# Add elements
fruits.append("carrot")         # Adds to end
fruits.insert(1, "cucumber")    # Inserts at index 1

# Remove elements
fruits.remove("coconut")        # Removes specific item

# Sort and reverse
fruits.sort()           # Sorts alphabetically
fruits.reverse()        # Reverses order

# Clear all
fruits.clear()          # Removes all elements

# Find and count
print(fruits.index("water mellon"))  # Gets index of item
print(fruits.count("guavas"))        # Counts occurrences
```

### Iterating Over Lists

```python
for fruit in fruits:
    if fruit == "oranges":
        continue
    print(fruit)
```

**Output:** Prints all fruits except "oranges"

---

## Sets

**Sets** are unordered collections with no duplicate values. Individual items are immutable, but you can add or remove items from the set.

### Creating Sets

```python
fruits = {"apple", "banana", "coconut", "oranges", "water mellon", "guavas"}
```

### Common Set Operations

```python
# Explore methods
print(dir(fruits))      # Shows all available methods
print(help(fruits))     # Shows documentation

# Get length
print(len(fruits))      # Number of items in set

# Check membership
print("oranges" in fruits)  # True

# Add elements
fruits.add("pineapples")    # Adds new item

# Remove elements
fruits.remove("guavas")     # Removes specific item
fruits.pop()                # Removes random item (sets are unordered)

# Display
print(fruits)               # Order may vary each time
```

### Iterating Over Sets

```python
for fruit in fruits:
    if fruit == "oranges":
        continue
    print(fruit)
```

**Note:** Order of iteration is not guaranteed with sets.

---

## Tuples

**Tuples** are ordered, unchangeable collections that allow duplicates. They are faster than lists because they're immutable.

### Creating Tuples

```python
fruits = ("apple", "banana", "coconut", "oranges", "water mellon", "guavas")
```

### Common Tuple Operations

```python
# Display
print(fruits)

# Find and count
print(fruits.index("water mellon"))  # Gets index of item
print(fruits.count("guavas"))        # Counts occurrences
```

### Iterating Over Tuples

```python
for fruit in fruits:
    if fruit == "oranges":
        continue
    print(fruit)
```

**Output:**
```
apple
banana
coconut
water mellon
guavas
```

**Note:** Cannot modify, add, or remove items from tuples after creation.

---

## Comparison Table

### Method Availability

| Method | List | Set | Tuple | Description |
|--------|------|-----|-------|-------------|
| `len()` | ✓ | ✓ | ✓ | Get number of items |
| `in` | ✓ | ✓ | ✓ | Check if item exists |
| `index()` | ✓ | ✗ | ✓ | Find item position |
| `count()` | ✓ | ✗ | ✓ | Count occurrences |
| `append()` | ✓ | ✗ | ✗ | Add item to end |
| `insert()` | ✓ | ✗ | ✗ | Add item at position |
| `remove()` | ✓ | ✓ | ✗ | Remove specific item |
| `pop()` | ✓ | ✓ | ✗ | Remove item |
| `sort()` | ✓ | ✗ | ✗ | Sort items |
| `reverse()` | ✓ | ✗ | ✗ | Reverse order |
| `clear()` | ✓ | ✓ | ✗ | Remove all items |
| `add()` | ✗ | ✓ | ✗ | Add item to set |
| Slicing `[:]` | ✓ | ✗ | ✓ | Get subset |
| Indexing `[i]` | ✓ | ✗ | ✓ | Access by position |
| Modification | ✓ | ✗ | ✗ | Change items |

### When to Use Each Type

**Use Lists when:**
- You need an ordered collection
- You need to modify items
- Duplicates are allowed/needed
- You need to access items by index
- You need sorting/reversing capabilities

**Use Sets when:**
- Order doesn't matter
- You need unique values only
- You need fast membership testing
- You need mathematical set operations (union, intersection, etc.)

**Use Tuples when:**
- You need an ordered collection
- Data should not change (immutable)
- You want better performance than lists
- You need to use collection as dictionary key
- You want to protect data from modification

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python lists_sets_and_tuples.py
   ```
3. Uncomment different sections to test various operations

---

## Key Concepts Learnt

### Understanding Collections
- **Definition**: Single variable storing multiple values
- **Three main types**: Lists, sets, and tuples
- **Choosing the right type**: Based on mutability, order, and duplicates needs

### List Operations
- **Creating lists**: Using square brackets `[]`
- **Indexing**: Accessing elements by position `fruits[0]`
- **Slicing**: Getting subsets `fruits[2:7:2]`
- **Modifying**: Changing values `fruits[3] = "new value"`
- **Adding items**: `append()` and `insert()`
- **Removing items**: `remove()`, `pop()`, `clear()`
- **Organizing**: `sort()` and `reverse()`
- **Searching**: `index()` and `count()`
- **Membership testing**: Using `in` keyword

### Set Operations
- **Creating sets**: Using curly braces `{}`
- **Uniqueness**: Automatically removes duplicates
- **Unordered**: No guaranteed order of elements
- **Adding items**: `add()` method
- **Removing items**: `remove()` and `pop()` methods
- **No indexing**: Cannot access by position
- **Fast membership testing**: Efficient `in` checks
- **Exploration**: Using `dir()` and `help()` to discover methods

### Tuple Operations
- **Creating tuples**: Using parentheses `()`
- **Immutability**: Cannot change after creation
- **Performance**: Faster than lists
- **Limited methods**: Only `index()` and `count()` available
- **Use cases**: When data shouldn't change
- **Still iterable**: Can loop through with for loops

### Common Patterns Across All Types
- **Length checking**: `len()` works on all collections
- **Membership testing**: `in` keyword works on all
- **Iteration**: All can be used in for loops
- **Empty collections**: `[]`, `{}`, `()` create empty collections

### Iteration with Control Flow
- Using for loops to iterate through collections
- Combining with `continue` to skip specific items
- Applying conditional logic while iterating

---

## Practical Examples

### List: Shopping Cart
```python
cart = ["milk", "bread", "eggs"]
cart.append("butter")
cart.remove("bread")
print(f"Cart has {len(cart)} items")
```

### Set: Unique Visitors
```python
visitors = {"Alice", "Bob", "Alice", "Charlie"}
print(visitors)  # {'Alice', 'Bob', 'Charlie'} - no duplicates
visitors.add("David")
print(f"Total unique visitors: {len(visitors)}")
```

### Tuple: Coordinates
```python
location = (40.7128, -74.0060)  # New York coordinates
latitude, longitude = location
print(f"Lat: {latitude}, Long: {longitude}")
# location[0] = 50  # ERROR: tuples are immutable
```

### Choosing Collection Type
```python
# List - menu items that can change
menu = ["pizza", "burger", "pasta"]
menu.append("salad")

# Set - unique usernames
usernames = {"john", "jane", "john"}  # Only 2 items stored

# Tuple - RGB color that shouldn't change
red = (255, 0, 0)
```