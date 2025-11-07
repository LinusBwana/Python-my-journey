# Python Functions & Return Statement

This directory contains practice exercises for learning functions and the return statement in Python. These examples demonstrate how to create reusable code blocks and send results back to the caller.

## Contents

1. [What are Functions?](#what-are-functions)
2. [The Return Statement](#the-return-statement)
3. [Practice Examples](#practice-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are Functions?

```python
# function = a block of reusable code
#            place () after the function name to invoke it
#            we use def to define a function
```

A **function** is a named block of code that performs a specific task. Functions help you:
- Avoid repeating code
- Organize code into logical pieces
- Make code easier to test and debug
- Create reusable components

**Basic syntax:**
```python
def function_name(parameters):
    # code to execute
    pass
```

**Key terms:**
- **Define**: Create a function using `def`
- **Parameters**: Variables in the function definition
- **Arguments**: Values passed when calling the function
- **Invoke/Call**: Execute the function using `function_name()`

---

## The Return Statement

```python
# return = statement used to end a function and send a result back to the caller
```

The **return statement**:
- Ends function execution immediately
- Sends a value back to where the function was called
- Allows function results to be stored in variables or used in expressions

**Without return:**
```python
def greet():
    print("Hello")
    # Function does something but returns None

greet()  # Prints "Hello"
result = greet()  # result is None
```

**With return:**
```python
def greet():
    return "Hello"
    # Function returns a value

message = greet()  # message is "Hello"
print(message)  # Prints "Hello"
```

---

## Practice Examples

### Example 1: Function with Parameters (No Return)

A function that prints birthday messages.

```python
def happy_birthday(name, age):
    print(f"Happy birthday {name}")
    print(f"You are {age} years old")
    print()

happy_birthday("Linus", 20)
happy_birthday("Annette", 30)
happy_birthday("bro", 29)
```

**Output:**
```
Happy birthday Linus
You are 20 years old

Happy birthday Annette
You are 30 years old

Happy birthday bro
You are 29 years old
```

**How it works:**
- **`def happy_birthday(name, age)`**: Defines function with two parameters
- **Parameters**: `name` and `age` act as placeholders
- **Arguments**: Values passed when calling (e.g., "Linus", 20)
- **No return**: Function performs action but doesn't return a value
- **Reusability**: Same function called multiple times with different values

**Function call breakdown:**
```python
happy_birthday("Linus", 20)
#              ↓        ↓
#            name=    age=
```

---

### Example 2: Functions with Return Statement

Mathematical functions that calculate and return results.

```python
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(25, 5))       # 30
print(subtract(25, 5))  # 20
print(multiply(25, 5))  # 125
print(divide(25, 5))    # 5.0
```

**How it works:**
- **Parameters**: `x` and `y` are input values
- **Calculation**: Perform operation and store in `z`
- **Return**: Send result back to caller
- **Usage**: Can be used in print statements, assignments, or expressions

**With return, you can:**
```python
result = add(10, 5)           # Store result
total = add(10, 5) + 20       # Use in expression
print(add(10, 5))             # Print directly
if add(10, 5) > 10:           # Use in conditions
    print("Greater than 10")
```

**Simplified version:**
```python
def add(x, y):
    return x + y  # Can return directly without intermediate variable
```

---

### Example 3: String Manipulation Function

A function that formats names and returns the result.

```python
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("linus", "bwana")
print(full_name)  # Linus Bwana
```

**Output:**
```
Linus Bwana
```

**How it works:**
- **Input**: Takes two parameters (first name, last name)
- **Processing**: 
  - Capitalizes first letter of each name
  - Combines with space between
- **Return**: Sends formatted full name back
- **Assignment**: Result stored in `full_name` variable

**Step-by-step execution:**
```python
create_name("linus", "bwana")
    ↓
first = "linus".capitalize()  # "Linus"
last = "bwana".capitalize()   # "Bwana"
    ↓
return "Linus" + " " + "Bwana"  # "Linus Bwana"
    ↓
full_name = "Linus Bwana"
```

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python functions_and_return.py
   ```

---

## Key Concepts Learnt

### Function Basics
- **Definition**: Using `def` keyword to create functions
- **Naming**: Following snake_case convention for function names
- **Parameters**: Variables that receive values when function is called
- **Arguments**: Actual values passed to function
- **Invocation**: Calling function with `function_name()`

### Function Parameters
- **Multiple parameters**: Functions can accept multiple inputs
- **Order matters**: Arguments passed in order of parameters
- **Parameter names**: Only visible inside function (local scope)
- **Flexibility**: Same function can be called with different values

### Return Statement
- **Purpose**: Send result back to caller
- **Ends function**: Code after return is not executed
- **Return value**: Can be any data type (number, string, list, etc.)
- **None**: Functions without return automatically return None
- **Single return**: Can only return one value (but can be tuple/list with multiple items)

### Functions Without Return
- **Side effects**: Perform actions (print, modify files, etc.)
- **Return None**: Implicitly return None
- **Use case**: When you need action, not a value
- **Example**: Printing, saving files, sending emails

### Functions With Return
- **Calculate values**: Perform computation and return result
- **Data transformation**: Process input and return processed output
- **Reusable results**: Value can be stored and used multiple times
- **Composable**: Return values can be used as arguments to other functions

### Variable Scope
- **Local variables**: Variables inside function only exist during function execution
- **Parameters**: Act as local variables
- **Return**: Way to get data out of function scope

---

## Understanding Return vs Print

### Print: Displays to Screen
```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Prints: Hello, Alice
result = greet("Alice")  # Prints: Hello, Alice, result = None
```

### Return: Sends Value Back
```python
def greet(name):
    return f"Hello, {name}"

greet("Alice")  # Nothing displayed
result = greet("Alice")  # result = "Hello, Alice"
print(result)  # Now prints: Hello, Alice
```

### When to Use Each

**Use print when:**
- Displaying information to user
- Debugging
- Creating output for human reading

**Use return when:**
- Function should calculate something
- Value will be used in further calculations
- Building reusable components
- Testing functions

---

## Common Function Patterns

### Pattern 1: Calculator Functions
```python
def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y

result = calculate(10, 5, "add")
```

### Pattern 2: Validation Functions
```python
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False

if is_valid_email("user@example.com"):
    print("Valid email")
```

### Pattern 3: Data Transformation
```python
def format_phone(phone):
    digits = phone.replace("-", "").replace(" ", "")
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

formatted = format_phone("123-456-7890")
```

### Pattern 4: Multiple Calculations
```python
def calculate_circle(radius):
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference  # Returns tuple

area, circ = calculate_circle(5)
```

---

## Function Best Practices

### Good Function Names
```python
# Good - describes what function does
def calculate_total_price(items):
    pass

def is_valid_password(password):
    pass

def get_user_name():
    pass

# Bad - unclear or too generic
def do_stuff():
    pass

def function1():
    pass
```

### Single Responsibility
```python
# Good - one clear purpose
def calculate_tax(amount):
    return amount * 0.08

# Bad - does too many things
def process_order(items):
    # calculates total
    # applies discount
    # calculates tax
    # sends email
    # updates database
    pass
```

### Clear Parameters
```python
# Good - clear what's expected
def create_user(username, email, age):
    pass

# Bad - unclear purpose
def create_user(x, y, z):
    pass
```

---

## Advanced Examples

### Example: Temperature Converter
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")
```

### Example: Grade Calculator
```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grade = calculate_grade(85)
print(f"Your grade is: {grade}")
```

### Example: String Utilities
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

text = "Hello World"
print(f"Vowels: {count_vowels(text)}")
print(f"Reversed: {reverse_text(text)}")
```

---

## Testing Functions

### Simple Tests
```python
def add(x, y):
    return x + y

# Test cases
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
print("All tests passed!")
```

### Test with Print
```python
def multiply(x, y):
    return x * y

# Test
result = multiply(4, 5)
expected = 20
if result == expected:
    print("Test passed")
else:
    print(f"Test failed: expected {expected}, got {result}")
```