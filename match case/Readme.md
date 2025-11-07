# Python Match-Case Statement

This directory contains practice exercises for learning match-case statements in Python. These examples demonstrate how to use match-case as a cleaner alternative to multiple elif statements.

## Contents

1. [What is Match-Case?](#what-is-match-case)
2. [Syntax](#syntax)
3. [Practice Examples](#practice-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What is Match-Case?

```python
# match-case statement (switch) - An alternative to using many elif statements
# Execute some code if a value matches a case
# Benefits - cleaner and the syntax is more readable
```

**Match-case** (introduced in Python 3.10) provides a cleaner way to handle multiple conditions compared to long if-elif chains.

**Instead of:**
```python
if day == 1:
    return "Sunday"
elif day == 2:
    return "Monday"
elif day == 3:
    return "Tuesday"
```

**Use:**
```python
match day:
    case 1:
        return "Sunday"
    case 2:
        return "Monday"
    case 3:
        return "Tuesday"
```

---

## Syntax

### Basic Structure
```python
match variable:
    case value1:
        # code
    case value2:
        # code
    case _:  # wildcard (default)
        # code if no match
```

### Multiple Values
```python
match variable:
    case value1 | value2 | value3:
        # code for any of these values
```

**Components:**
- **`match`**: Keyword to start match statement
- **`case`**: Defines each possible match
- **`_`**: Wildcard that matches anything (default case)
- **`|`**: OR operator to match multiple values

---

## Practice Examples

### Example 1: Day of Week (Numbers)

```python
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:  # wildcard - prints if all other cases fail
            return "Invalid day"

print(day_of_week(9))
# Output: Invalid day
```

---

### Example 2: Weekend Checker (Long Form)

```python
def is_weekend(day):
    match day:
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case "Sunday":
            return True
        case _:  # wildcard - prints if all other cases fail
            return "Invalid day"

print(is_weekend("Monday"))
# Output: False
```

---

### Example 3: Weekend Checker (Using OR)

```python
def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:  # wildcard - prints if all other cases fail
            return "Invalid day"

print(is_weekend("Pizza"))
# Output: Invalid day
```

**Benefits:**
- More concise than multiple cases
- Groups related values together
- Easier to read and maintain

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python match_case_statement.py
   ```

**Note:** Requires Python 3.10 or higher.

---

## Key Concepts Learnt

### Match-Case Advantages
- **Cleaner syntax**: More readable than long if-elif chains
- **Pattern matching**: Can match values directly
- **Wildcard support**: `_` handles unmatched cases
- **Multiple values**: Use `|` to match several values at once

### Basic Match-Case
- Tests a value against multiple cases
- Executes code for first matching case
- Stops after first match (no fallthrough)
- Wildcard `_` catches all unmatched cases

### OR Operator (|)
- Combines multiple values in single case
- Acts as logical OR
- Reduces code duplication
- Makes related cases clearer

### Wildcard (_)
- Matches anything not caught by other cases
- Similar to `else` in if-elif-else
- Should be last case
- Optional but recommended for error handling

---

## Comparison: if-elif vs match-case

### Using if-elif
```python
def get_grade(score):
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
```

### Using match-case
```python
def get_action(command):
    match command:
        case "start":
            return "Starting..."
        case "stop":
            return "Stopping..."
        case "pause":
            return "Pausing..."
        case "resume":
            return "Resuming..."
        case _:
            return "Unknown command"
```

**When to use match-case:**
- Matching exact values
- Multiple discrete options
- Clearer than many elif statements

**When to use if-elif:**
- Range comparisons (>=, <=, <, >)
- Complex conditions
- Python version < 3.10

---

## Additional Examples

### Menu Selection
```python
def process_menu(choice):
    match choice:
        case 1:
            return "View balance"
        case 2:
            return "Deposit"
        case 3:
            return "Withdraw"
        case 4:
            return "Exit"
        case _:
            return "Invalid option"
```

### HTTP Status
```python
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown Status"
```

### Traffic Light
```python
def traffic_action(light):
    match light:
        case "red":
            return "Stop"
        case "yellow":
            return "Slow down"
        case "green":
            return "Go"
        case _:
            return "Light malfunction"
```

---