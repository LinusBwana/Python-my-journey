# String Methods

String methods are built-in functions in Python that allow you to manipulate and analyze string data. They provide powerful ways to search, modify, validate, and transform text without writing complex code from scratch.

### String Methods Practice Example

```python
name = input("Enter your full name: ")
phone_number = input("Enter your phone number #: ")

result = len(name)
result = name.find(" ")
result = name.rfind("n")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()
result = phone_number.count("1")
result = phone_number.replace("-", "")
```

### String Methods Explained

| Method | Purpose | Example |
|--------|---------|---------|
| `len()` | Returns the length (number of characters) of a string | `len("Hello")` returns `5` |
| `find()` | Returns the index of the first occurrence of a substring. Returns `-1` if not found | `"Hello World".find(" ")` returns `5` |
| `rfind()` | Returns the index of the last occurrence of a substring (searches from right to left) | `"banana".rfind("a")` returns `5` |
| `capitalize()` | Converts the first character to uppercase and the rest to lowercase | `"hello".capitalize()` returns `"Hello"` |
| `upper()` | Converts all characters in the string to uppercase | `"hello".upper()` returns `"HELLO"` |
| `lower()` | Converts all characters in the string to lowercase | `"HELLO".lower()` returns `"hello"` |
| `isdigit()` | Returns `True` if all characters are digits, otherwise `False` | `"123".isdigit()` returns `True` |
| `isalpha()` | Returns `True` if all characters are alphabetic, otherwise `False` | `"Hello".isalpha()` returns `True` |
| `count()` | Counts the number of occurrences of a substring | `"hello".count("l")` returns `2` |
| `replace()` | Replaces all occurrences of a substring with another substring | `"hello".replace("l", "r")` returns `"herro"` |

---

## User Input Validation

A practical example combining if statements and string methods to validate user input.

```python
user_name = input("Enter the user name: ")

if len(user_name) > 12:
    print("User name can not be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("User name can not have spaces")
elif not user_name.isalpha():
    print("User name can not have digits")
else:
    print(f"Welcome {user_name}")
```

**How it works:**
1. Checks if username is longer than 12 characters using `len()`
2. Checks for spaces using `find()` - if it returns anything other than `-1`, a space exists
3. Checks if username contains only letters using `isalpha()`
4. If all validations pass, welcomes the user

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run any Python file:
   ```bash
   python filename.py
   ```

---

## Key Concepts Learned

### If Statements & Logic
- Basic if-elif-else statements
- User input handling with `input()`
- Type conversion with `float()` and `str()`
- Logical operators (`and`, `or`, `not`)
- Comparison operators (`==`, `>`, `<`, `>=`, `<=`)
- F-strings for formatted output
- Rounding numbers with `round()`

### String Methods
- `len()` - Measuring string length
- `find()` and `rfind()` - Searching for substrings
- `capitalize()`, `upper()`, `lower()` - Changing case
- `isdigit()` and `isalpha()` - Validating string content
- `count()` - Counting substring occurrences
- `replace()` - Substituting text
- Combining string methods with conditional logic for input validation

---