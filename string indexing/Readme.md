# Python Indexing Practice

This repository contains practice exercises for learning indexing in Python. These examples demonstrate how to access and manipulate elements within sequences using the indexing operator.

## Contents

1. [What is Indexing?](#what-is-indexing)
2. [Indexing Syntax](#indexing-syntax)
3. [Practice Example](#practice-example)
4. [Indexing Methods Explained](#indexing-methods-explained)
5. [Key Concepts Learned](#key-concepts-learned)

---

## What is Indexing?

**Indexing** is a way of accessing individual elements or ranges of elements in a sequence (like strings, lists, or tuples) using square brackets `[]` and the indexing operator. In Python, indexing allows you to:

- Access a single character or element at a specific position
- Extract a portion of a sequence (slicing)
- Reverse a sequence
- Skip elements using a step value

Python uses **zero-based indexing**, meaning the first element is at index `0`, the second at index `1`, and so on. You can also use **negative indexing** to access elements from the end of the sequence, where `-1` refers to the last element.

---

## Indexing Syntax

The general syntax for indexing is:

```python
sequence[start:end:step]
```

- **start**: The starting index (inclusive)
- **end**: The ending index (exclusive)
- **step**: The interval between elements (default is 1)

---

## Practice Example

```python
# indexing = accessing the elements of a sequence using [] (indexing operator)
#            [start : end : stop]

credit_number = "1235-7652-3763-8724"

print(credit_number[4])
print(credit_number[:4])
print(credit_number[5:])
print(credit_number[5:9])
print(credit_number[-4])
print(credit_number[2::3])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse = credit_number[::-1]
print(reverse)
```

---

## Indexing Methods Explained

### Single Element Access

| Code | Output | Explanation |
|------|--------|-------------|
| `credit_number[4]` | `-` | Accesses the character at index 4 (the 5th character) |
| `credit_number[-4]` | `8` | Accesses the 4th character from the end |

### Slicing

| Code | Output | Explanation |
|------|--------|-------------|
| `credit_number[:4]` | `1235` | Extracts characters from the start up to (but not including) index 4 |
| `credit_number[5:]` | `7652-3763-8724` | Extracts characters from index 5 to the end |
| `credit_number[5:9]` | `7652` | Extracts characters from index 5 up to (but not including) index 9 |
| `credit_number[-4:]` | `8724` | Extracts the last 4 characters |

### Step Slicing

| Code | Output | Explanation |
|------|--------|-------------|
| `credit_number[2::3]` | `37338` | Starts at index 2 and takes every 3rd character |
| `credit_number[::-1]` | `4278-3673-2567-5321` | Reverses the entire string (step of -1) |

### Practical Application

**Masking Credit Card Number:**
```python
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
```
**Output:** `XXXX-XXXX-XXXX-8724`

This extracts the last 4 digits and formats them for secure display.

**Reversing a String:**
```python
reverse = credit_number[::-1]
print(reverse)
```
**Output:** `4278-3673-2567-5321`

Using a step of `-1` reverses the entire sequence.

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the Python file:
   ```bash
   python indexing.py
   ```

---

## Key Concepts Learnt

- **Zero-based indexing**: First element is at index `0`
- **Negative indexing**: Access elements from the end using negative numbers
- **Slicing syntax**: `[start:end:step]`
  - `start` is inclusive
  - `end` is exclusive
  - `step` determines the interval
- **Omitting parameters**:
  - Omit `start` to begin from the first element
  - Omit `end` to go to the last element
  - Omit `step` to use default step of 1
- **Reversing sequences**: Use `[::-1]` to reverse
- **Practical applications**: Masking sensitive data, extracting specific portions of strings

---

## Quick Reference

```python
string = "Hello World"

string[0]      # 'H' - first character
string[-1]     # 'd' - last character
string[:5]     # 'Hello' - first 5 characters
string[6:]     # 'World' - from index 6 to end
string[::2]    # 'HloWrd' - every 2nd character
string[::-1]   # 'dlroW olleH' - reversed
```

---