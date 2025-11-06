# Python Dictionaries Practice

This directory contains practice exercises for learning dictionaries in Python. These examples demonstrate how to work with key-value pairs to store and manipulate related data.

## Contents

1. [What are Dictionaries?](#what-are-dictionaries)
2. [Creating and Accessing Dictionaries](#creating-and-accessing-dictionaries)
3. [Dictionary Methods](#dictionary-methods)
4. [Iterating Through Dictionaries](#iterating-through-dictionaries)
5. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are Dictionaries?

```python
# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates
```

A **dictionary** is a collection of key-value pairs where:
- Each **key** is unique and maps to a **value**
- Keys are used to look up their associated values
- Dictionaries are ordered (as of Python 3.7+)
- Dictionaries are changeable (mutable)
- Keys cannot be duplicated (each key appears only once)

**Analogy:** Like a real dictionary where words (keys) have definitions (values).

**Use cases:**
- Storing related data (country → capital)
- Mapping IDs to information
- Counting occurrences
- Configuration settings

---

## Creating and Accessing Dictionaries

### Creating a Dictionary

```python
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
```

**Structure:**
- **Keys**: "USA", "India", "China", "Russia"
- **Values**: "Washington D.C.", "New Delhi", "Beijing", "Moscow"
- **Syntax**: `{key1: value1, key2: value2, ...}`

### Exploring Dictionary Methods

```python
print(dir(capitals))    # Shows all available methods
print(help(capitals))   # Shows detailed documentation
```

These functions help you discover what operations are available on dictionaries.

---

## Dictionary Methods

### Checking for Keys

```python
if capitals.get("Russia"):
    print("Capital exists")
else:
    print("Capital doesn't exists")
```

**`.get(key)`** method:
- Returns the value if key exists
- Returns `None` if key doesn't exist (doesn't raise error)
- Safer than using `capitals[key]` which raises error if key missing

### Adding and Updating Entries

```python
# Adding a new entry
capitals["Kenya"] = "Nairobi"

# Updating an existing entry
capitals.update({"USA": "USA City"})
```

**Two ways to add/update:**
- **Direct assignment**: `dictionary[key] = value`
  - Creates new entry if key doesn't exist
  - Updates value if key exists
- **`.update()` method**: `dictionary.update({key: value})`
  - Can update multiple entries at once
  - `capitals.update({"USA": "NYC", "Kenya": "Mombasa"})`

### Removing Entries

```python
# Remove specific key
capitals.pop("China")

# Remove last inserted item
capitals.popitem()
```

**Removal methods:**
- **`.pop(key)`**: Removes specific key-value pair, returns the value
- **`.popitem()`**: Removes and returns last inserted key-value pair as tuple
- **`.clear()`**: Removes all entries

### Getting Values

```python
print(capitals.get("USA"))      # Returns "Washington D.C."
print(capitals.get("Japan"))    # Returns None (key doesn't exist)
```

**`.get()` advantages:**
- Returns `None` instead of error for missing keys
- Can specify default: `capitals.get("Japan", "Not Found")`

### Getting Items, Keys, and Values

```python
print(list(capitals.items())[0])    # First key-value pair as tuple
print(list(capitals.keys())[0])     # First key
print(list(capitals.values())[0])   # First value
```

**Dictionary views:**
- **`.items()`**: Returns view of (key, value) tuples
- **`.keys()`**: Returns view of all keys
- **`.values()`**: Returns view of all values
- **Converting to list**: Use `list()` to convert views to lists for indexing

---

## Iterating Through Dictionaries

### Iterating Through Keys

```python
keys = capitals.keys()
for key in keys:
    print(key)
```

**Output:**
```
USA
India
China
Russia
```

**Alternative (direct iteration):**
```python
for key in capitals:
    print(key)
```

### Iterating Through Values

```python
values = capitals.values()
for value in values:
    print(value)
```

**Output:**
```
Washington D.C.
New Delhi
Beijing
Moscow
```

### Iterating Through Key-Value Pairs

```python
for key, value in capitals.items():
    print(f"{key}: {value}")
```

**Output:**
```
USA: Washington D.C.
India: New Delhi
China: Beijing
Russia: Moscow
```

**How it works:**
- `.items()` returns tuples of (key, value)
- Tuple unpacking assigns key and value in each iteration
- Most useful pattern for accessing both keys and values

### Clearing Dictionary

```python
capitals.clear()
print(capitals)  # {}
```

Removes all entries, leaving an empty dictionary.

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python dictionaries.py
   ```

---

## Key Concepts Learnt

### Understanding Dictionaries
- **Definition**: Collection of key-value pairs
- **Syntax**: Created with curly braces `{key: value}`
- **Properties**: Ordered, changeable, no duplicate keys
- **Access**: Values accessed by keys, not indices

### Creating Dictionaries
- **Literal syntax**: `{"key1": "value1", "key2": "value2"}`
- **Empty dictionary**: `{}` or `dict()`
- **Key types**: Must be immutable (strings, numbers, tuples)
- **Value types**: Can be any type (strings, numbers, lists, dictionaries, etc.)

### Accessing Values
- **Direct access**: `dictionary[key]` (raises error if key missing)
- **Safe access**: `dictionary.get(key)` (returns None if key missing)
- **Default values**: `dictionary.get(key, "default")`
- **Checking existence**: Using `.get()` in conditional statements

### Adding and Modifying
- **Add entry**: `dictionary[new_key] = value`
- **Update entry**: `dictionary[existing_key] = new_value`
- **Batch update**: `dictionary.update({key1: val1, key2: val2})`
- **No duplicate keys**: New value overwrites old value for same key

### Removing Entries
- **Remove specific**: `.pop(key)` returns value
- **Remove last**: `.popitem()` returns (key, value) tuple
- **Remove all**: `.clear()` empties dictionary
- **Delete with del**: `del dictionary[key]`

### Dictionary Views
- **`.keys()`**: View of all keys
- **`.values()`**: View of all values
- **`.items()`**: View of (key, value) tuples
- **Converting views**: Use `list()` to convert for indexing

### Iteration Patterns
- **Keys only**: `for key in dictionary:`
- **Values only**: `for value in dictionary.values():`
- **Key-value pairs**: `for key, value in dictionary.items():`
- **Tuple unpacking**: Automatically assigns key and value

### Exploration Tools
- **`dir()`**: Lists all methods and attributes
- **`help()`**: Shows detailed documentation
- **Learning tool**: Useful for discovering functionality

---

## Common Dictionary Operations

### Check if Key Exists

```python
# Method 1: Using in
if "USA" in capitals:
    print("USA found")

# Method 2: Using get()
if capitals.get("USA"):
    print("USA found")

# Method 3: Using keys()
if "USA" in capitals.keys():
    print("USA found")
```

### Get Value with Default

```python
# If key doesn't exist, return default value
capital = capitals.get("Japan", "Unknown")
print(capital)  # Unknown
```

### Count Items

```python
num_countries = len(capitals)
print(f"Number of countries: {num_countries}")
```

### Copy Dictionary

```python
# Shallow copy
capitals_copy = capitals.copy()

# Alternative
capitals_copy = dict(capitals)
```

### Merge Dictionaries

```python
dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}

# Method 1: Update
dict1.update(dict2)

# Method 2: Unpacking (Python 3.9+)
merged = {**dict1, **dict2}
```

---

## Practical Examples

### Example 1: Student Grades

```python
grades = {"Alice": 85,
          "Bob": 92,
          "Charlie": 78}

# Add new student
grades["David"] = 88

# Update grade
grades["Alice"] = 90

# Display all grades
for student, grade in grades.items():
    print(f"{student}: {grade}")
```

### Example 2: Word Counter

```python
text = "hello world hello"
word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # {'hello': 2, 'world': 1}
```

### Example 3: Phone Book

```python
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

# Search for contact
name = input("Enter name: ")
phone = contacts.get(name, "Contact not found")
print(f"{name}: {phone}")
```

### Example 4: Nested Dictionary

```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"}
}

# Access nested value
print(students["Alice"]["age"])  # 20

# Iterate nested dictionary
for name, info in students.items():
    print(f"{name}: Age {info['age']}, Grade {info['grade']}")
```

---

## Dictionary vs Other Collections

### Dictionary vs List

| Feature | Dictionary | List |
|---------|-----------|------|
| **Access** | By key | By index (0, 1, 2...) |
| **Order** | Ordered (Python 3.7+) | Ordered |
| **Duplicates** | Keys unique | Allowed |
| **Syntax** | `{key: value}` | `[item1, item2]` |
| **Use case** | Mapping relationships | Sequential data |

### Dictionary vs Tuple

| Feature | Dictionary | Tuple |
|---------|-----------|-------|
| **Mutable** | Yes | No |
| **Structure** | Key-value pairs | Sequential items |
| **Access** | By key | By index |
| **Syntax** | `{key: value}` | `(item1, item2)` |

### Dictionary vs Set

| Feature | Dictionary | Set |
|---------|-----------|-----|
| **Structure** | Key-value pairs | Unique items only |
| **Values** | Has values | No values (just items) |
| **Duplicates** | Keys unique | All items unique |
| **Syntax** | `{key: value}` | `{item1, item2}` |

---

## Common Patterns

### Pattern 1: Default Dictionary Behavior

```python
# Count occurrences
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```

### Pattern 2: Dictionary Comprehension

```python
# Create dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
```

### Pattern 3: Filtering Dictionary

```python
# Keep only items where value > 80
filtered = {k: v for k, v in grades.items() if v > 80}
```

### Pattern 4: Swapping Keys and Values

```python
# Swap keys and values
swapped = {v: k for k, v in dictionary.items()}
```

---

## Understanding Dictionary Order

Prior to Python 3.7, dictionaries were unordered. Since Python 3.7+, dictionaries maintain insertion order.

```python
capitals = {}
capitals["USA"] = "Washington D.C."
capitals["India"] = "New Delhi"
capitals["China"] = "Beijing"

# Order is guaranteed:
for key in capitals:
    print(key)
# Output: USA, India, China (in insertion order)
```