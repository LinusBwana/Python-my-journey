# Python Continue & Break Practice

This directory contains practice exercises for learning the `continue` and `break` statements in Python. These control flow statements allow you to modify loop behavior.

## Contents

1. [What are Continue & Break?](#what-are-continue--break)
2. [Continue Statement](#continue-statement)
3. [Break Statement](#break-statement)
4. [Practice Example](#practice-example)
5. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are Continue & Break?

```python
# continue - skips that specific iteration and continues the loop
# break - breaks out of the loop entirely
```

**Continue** and **break** are control flow statements that give you more control over loop execution:

- **`continue`**: Skips the remaining code in the current iteration and moves to the next iteration
- **`break`**: Exits the loop completely, regardless of the loop condition

---

## Continue Statement

### What Does `continue` Do?

When Python encounters a `continue` statement:
1. It skips all remaining code in the current iteration
2. Jumps back to the loop condition
3. Continues with the next iteration (if the condition is still true)

### Syntax

```python
for item in sequence:
    if condition:
        continue  # Skip to next iteration
    # This code is skipped when continue executes
```

### Example: Skip Even Numbers

```python
for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)  # Only prints odd numbers
```

**Output:**
```
1
3
5
7
9
```

**How it works:**
- When `x` is even (divisible by 2), `continue` is executed
- The `print(x)` is skipped for even numbers
- Loop moves to the next iteration
- Only odd numbers are printed

---

## Break Statement

### What Does `break` Do?

When Python encounters a `break` statement:
1. It immediately exits the entire loop
2. No more iterations are performed
3. Execution continues with the code after the loop

### Syntax

```python
for item in sequence:
    if condition:
        break  # Exit loop entirely
    # This code runs until break is encountered
# Code after loop continues here
```

### Example: Stop at First Match

```python
for x in range(1, 11):
    print(x)
    if x == 5:
        break
print("Loop ended")
```

**Output:**
```
1
2
3
4
5
Loop ended
```

**How it works:**
- Loop prints numbers starting from 1
- When `x` equals 5, `break` is executed
- Loop terminates immediately
- Execution continues with code after the loop

---

## Practice Example

This example uses `continue` to print only odd numbers from 1 to 20.

```python
for x in range(1, 21):
    if x % 2 == 0:
        continue
    else:
        print(x)
```

**Output:**
```
1
3
5
7
9
11
13
15
17
19
```

**Step-by-step breakdown:**
1. Loop iterates through numbers 1 to 20
2. For each number, check if it's even using modulo operator (`%`)
3. If `x % 2 == 0` (number is even), execute `continue`
4. `continue` skips the `print(x)` statement
5. If number is odd, the else block executes and prints the number
6. Result: Only odd numbers are printed

**Note:** The `else` block isn't strictly necessary here. This code works the same:
```python
for x in range(1, 21):
    if x % 2 == 0:
        continue
    print(x)
```

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the Python file:
   ```bash
   python "continue & break.py"
   ```

---

## Key Concepts Learnt

### Continue Statement
- **Purpose**: Skip current iteration and continue with next one
- **Use case**: When you want to skip certain items but keep looping
- **Effect**: Jumps back to loop condition, doesn't exit the loop
- **Common scenarios**: Filtering data, skipping invalid entries

### Break Statement
- **Purpose**: Exit loop completely
- **Use case**: When you want to stop looping early
- **Effect**: Terminates the loop immediately
- **Common scenarios**: Finding a match, stopping on error, user-initiated exit

### Control Flow Impact
- Both statements work in `for` and `while` loops
- Can be used with `if` statements for conditional control
- Affect only the innermost loop (in nested loops)
- Make code more efficient by avoiding unnecessary iterations

### Best Practices
- Use `continue` to skip unwanted iterations
- Use `break` to exit when a condition is met
- Keep logic clear and readable
- Consider if the same result can be achieved with better conditionals

---

## Common Use Cases

### Continue: Skip Invalid Data
```python
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(num)
# Output: 1, 3, 5
```

### Continue: Skip Specific Values
```python
for i in range(10):
    if i == 5:
        continue  # Skip when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4, 6, 7, 8, 9
```

### Break: Stop at First Match
```python
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    if name == "Charlie":
        print("Found!")
        break
# Output: Found!
# Stops searching after finding Charlie
```

### Break: Exit on User Command
```python
while True:
    command = input("Enter command (q to quit): ")
    if command == "q":
        break
    print(f"You entered: {command}")
```

### Break: Stop on Error Condition
```python
for x in range(1, 10):
    if x > 5:
        print("Limit reached!")
        break
    print(x)
# Output: 1, 2, 3, 4, 5, Limit reached!
```

---

## Continue vs Break

| Aspect | `continue` | `break` |
|--------|-----------|---------|
| **Action** | Skips current iteration | Exits entire loop |
| **Loop status** | Continues running | Terminates immediately |
| **Next step** | Goes to next iteration | Goes to code after loop |
| **Use when** | You want to skip some items | You want to stop looping |
| **Example scenario** | Skip even numbers | Stop when target found |

### Visual Comparison

**With `continue`:**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0, 1, 3, 4 (skips 2, continues loop)
```

**With `break`:**
```python
for i in range(5):
    if i == 2:
        break
    print(i)
# Output: 0, 1 (stops at 2, exits loop)
```

---

## When to Use Which?

### Use `continue` when:
- You want to skip certain iterations but keep looping
- You're filtering data within a loop
- You want to ignore invalid or unwanted values
- The loop should process all items except specific ones

### Use `break` when:
- You've found what you're looking for
- An error condition is met
- User wants to quit
- No need to continue checking remaining items
- You want to optimize by stopping early

---