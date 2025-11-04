# Python While Loops Practice

This directory contains practice exercises for learning while loops in Python. These examples demonstrate how to execute code repeatedly while a condition remains true.

## Contents

1. [What are While Loops?](#what-are-while-loops)
2. [While Loop Syntax](#while-loop-syntax)
3. [Practice Examples](#practice-examples)
4. [Compound Interest Calculator](#compound-interest-calculator)
5. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are While Loops?

A **while loop** is a control flow statement that repeatedly executes a block of code as long as a specified condition evaluates to `True`. Unlike for loops that iterate a specific number of times, while loops continue until their condition becomes `False`.

While loops are useful for:
- Input validation
- Creating menus that run until the user quits
- Processing data until a specific condition is met
- Implementing retry logic

---

## While Loop Syntax

```python
while condition:
    # code to execute
    # condition should eventually become False
```

**Important concepts:**
- `continue` - Skips the rest of the current iteration and goes back to the condition check
- `break` - Exits the loop immediately

---

## Practice Examples

### Example 1: Name Validation

Ensures the user enters a non-empty name.

```python
name = input("Enter your name: ")
while name == "":
    name = input("Enter a valid name: ")
print(f"Hello {name}")
```

**How it works:** The loop continues asking for a name until the user provides a non-empty string.

---

### Example 2: Age Validation

Validates that the age is not negative.

```python
age = int(input("Enter your age: "))
while age < 0:
    age = int(input("Age can't be negative. Input age again: "))
print(f"You are {age} years old")
```

**How it works:** The loop repeats until the user enters a valid non-negative age.

---

### Example 3: Favorite Foods List

Collects favorite foods until the user types 'q' to quit.

```python
food = input("Enter the food you like (q to quit): ")
while not food == "q":
    food = input(f"You like {food}. Enter the food you like (q to quit): ")
print("Bye")
```

**How it works:** The loop continues collecting food preferences until the user enters 'q', using the `not` operator to check the condition.

---

### Example 4: Number Range Validation

Ensures the user enters a number within a specific range.

```python
num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")
```

**How it works:** The loop continues until the user enters a number between 1 and 10 (inclusive), using the `or` operator to check both boundaries.

---

## Compound Interest Calculator

A practical application combining while loops, input validation, and mathematical calculations.

```python
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))
    error = []

    if principle < 0:
        error.append("Principle can't be less than zero")

    if rate < 0:
        error.append("Interest rate can't be less than zero") 

    if time < 0:
        error.append("Time can't be less than zero")
    
    if error:
        for e in error:
            print("-", e)
        print("Try again")
        continue
    else:
        total = principle * pow((1 + (rate / 100)), time)
        print(f"Balance after {time} year/s: ${total:.2f}")
        break
```

### How the Calculator Works

1. **Infinite Loop**: Uses `while True` to create a loop that runs indefinitely until explicitly broken
2. **Input Collection**: Prompts user for principle amount, interest rate, and time
3. **Error Tracking**: Creates an empty list to store validation errors
4. **Validation Checks**: 
   - Checks if principle is negative
   - Checks if rate is negative
   - Checks if time is negative
   - Adds error messages to the list if any validation fails
5. **Error Handling**:
   - If errors exist, displays all error messages and uses `continue` to restart the loop
   - If no errors, calculates compound interest and uses `break` to exit the loop
6. **Calculation**: Uses the compound interest formula: `A = P(1 + r/100)^t`
7. **Output**: Displays the final balance formatted to 2 decimal places

**Example Output:**
```
Enter the principle amount: 1000
Enter the interest rate: 5
Enter the time in years: 3
Balance after 3.0 year/s: $1157.63
```

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run any Python file:
   ```bash
   python while_loops.py
   python compound_interest_calculator.py
   ```

---

## Key Concepts Learnt

### While Loop Fundamentals
- **Basic syntax**: `while condition:`
- **Loop continuation**: Code executes as long as condition is `True`
- **Loop termination**: Loop stops when condition becomes `False`
- **Infinite loops**: Using `while True` for loops that need explicit break conditions

### Control Flow Statements
- **`break`**: Exits the loop immediately
- **`continue`**: Skips remaining code in current iteration and returns to condition check
- **Combining with if-else**: Using conditionals inside loops for complex logic

### Input Validation Patterns
- Empty string validation
- Numeric range validation
- Negative number validation
- Multiple validation checks with error collection

### Logical Operators in While Loops
- Using `not` to reverse conditions
- Using `or` to check multiple conditions
- Using `and` for compound conditions

### Practical Applications
- User input validation
- Building interactive programs
- Error handling and retry logic
- Mathematical calculations with validation
- Creating menu-driven applications

---

## Common While Loop Patterns

### Input Validation Pattern
```python
value = input("Enter value: ")
while not is_valid(value):
    value = input("Invalid. Try again: ")
```

### Infinite Loop with Break
```python
while True:
    user_input = input("Enter command (q to quit): ")
    if user_input == "q":
        break
    # process input
```

### Counter Pattern
```python
count = 0
while count < 10:
    print(count)
    count += 1
```

### Sentinel Value Pattern
```python
value = input("Enter value (or 'done'): ")
while value != "done":
    process(value)
    value = input("Enter value (or 'done'): ")
```


## Understanding `!=` vs `not`

### `!=` (Not Equal Operator)
- **Type**: Comparison operator
- **Purpose**: Compares two values to check if they are **not equal**
- **Returns**: Boolean (`True` or `False`)
- **Use case**: When comparing two specific values

**Examples:**
```python
# Comparing strings
value = "hello"
while value != "done":  # Continue while value is not equal to "done"
    print(value)

# Comparing numbers
age = 15
while age != 18:  # Continue while age is not equal to 18
    age += 1
```

### `not` (Logical Operator)
- **Type**: Logical operator
- **Purpose**: Reverses/negates a boolean value
- **Returns**: Boolean (`True` becomes `False`, `False` becomes `True`)
- **Use case**: When you want to reverse a condition or check if something is False

**Examples:**
```python
# Reversing a boolean
is_valid = False
while not is_valid:  # Same as: while is_valid == False
    print("Invalid")

# Reversing an expression
name = ""
while not name:  # Same as: while name == ""
    name = input("Enter name: ")

# Reversing a comparison
food = "pizza"
while not food == "quit":  # Same as: while food != "quit"
    print(food)
```

### Key Differences

| Aspect | `!=` | `not` |
|--------|------|-------|
| **Purpose** | Compares two values | Reverses a boolean |
| **Usage** | `a != b` | `not condition` |
| **Example** | `x != 5` checks if x is not 5 | `not x` reverses the truthiness of x |
| **Best for** | Direct value comparisons | Reversing boolean expressions |

### When to Use Which?

**Use `!=` when:**
```python
# Comparing specific values
while answer != "yes":
    answer = input("Try again: ")

# More readable and direct
while user_input != "q":
    process(user_input)
```

**Use `not` when:**
```python
# Checking for empty strings
while not name:  # More pythonic than: while name == ""
    name = input("Enter name: ")

# Reversing boolean variables
while not is_complete:
    do_work()

# Checking if something is not in a collection
while not item in my_list:
    search_elsewhere()
```

**Both work the same:**
```python
# These are equivalent:
while food != "quit":
while not food == "quit":

```