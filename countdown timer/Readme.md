# Python Countdown Timer

This directory contains practice exercises for building countdown timers in Python. These examples demonstrate how to use for loops with the `time` module to create functional timers.

## Contents

1. [Introduction](#introduction)
2. [Required Module](#required-module)
3. [Practice Examples](#practice-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## Introduction

A **countdown timer** is a program that counts down from a specified time to zero. This project demonstrates:
- Working with the `time` module
- Creating different countdown formats
- Converting seconds to hours:minutes:seconds format
- Using for loops for time-based operations

---

## Required Module

### The `time` Module

The `time` module provides various time-related functions. In this project, we use:

```python
import time
```

**Key function:**
- `time.sleep(seconds)` - Pauses program execution for the specified number of seconds

---

## Practice Examples

### Example 1: Count Up Timer

Counts from 0 to the specified time.

```python
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)
print("Time is up!")
```

**Output (if user enters 5):**
```
0
1
2
3
4
Time is up!
```

**How it works:**
- `range(0, my_time)` generates numbers from 0 to my_time-1
- Each number is printed
- `time.sleep(1)` pauses for 1 second between prints
- Creates a count-up effect

---

### Example 2: Countdown Using `reversed()`

Counts down using the `reversed()` function.

```python
import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)
print("Time is up!")
```

**Output (if user enters 5):**
```
4
3
2
1
0
Time is up!
```

**How it works:**
- `reversed(range(0, my_time))` reverses the sequence
- Counts down from my_time-1 to 0
- Note: Doesn't include my_time itself, starts at my_time-1

---

### Example 3: Countdown Using Negative Step

Counts down using a negative step value in `range()`.

```python
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)
print("Time is up!")
```

**Output (if user enters 5):**
```
5
4
3
2
1
Time is up!
```

**How it works:**
- `range(my_time, 0, -1)` starts at my_time, ends before 0, decrements by 1
- Counts down from my_time to 1 (stops before 0)
- More intuitive than using `reversed()`
- This is the most common and readable approach

---

### Example 4: Formatted Countdown Timer (HH:MM:SS)

A professional-looking timer that displays time in hours:minutes:seconds format.

```python
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time is up!")
```

**Output (if user enters 3665):**
```
01:01:05
01:01:04
01:01:03
01:01:02
01:01:01
01:01:00
01:00:59
...
00:00:03
00:00:02
00:00:01
Time is up!
```

**How it works:**

1. **Calculate seconds:** `seconds = x % 60`
   - Modulo 60 gives remaining seconds after removing complete minutes
   - Example: 125 seconds → 125 % 60 = 5 seconds

2. **Calculate minutes:** `minutes = int(x / 60) % 60`
   - Divide by 60 to get total minutes
   - Modulo 60 to get remaining minutes after removing complete hours
   - Example: 125 seconds → 125/60 = 2.08 → int(2) → 2 % 60 = 2 minutes

3. **Calculate hours:** `hours = int(x / 3600)`
   - Divide by 3600 (60×60) to get total hours
   - Example: 3665 seconds → 3665/3600 = 1.01 → int(1) = 1 hour

4. **Format output:** `f"{hours:02}:{minutes:02}:{seconds:02}"`
   - `:02` means format as 2 digits with leading zero if needed
   - Example: 5 becomes "05", 12 stays "12"

**Time Conversion Table:**

| Total Seconds | Hours | Minutes | Seconds | Display |
|---------------|-------|---------|---------|---------|
| 3665 | 1 | 1 | 5 | 01:01:05 |
| 3600 | 1 | 0 | 0 | 01:00:00 |
| 125 | 0 | 2 | 5 | 00:02:05 |
| 59 | 0 | 0 | 59 | 00:00:59 |
| 1 | 0 | 0 | 1 | 00:00:01 |

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the Python file:
   ```bash
   python countdown_timer.py
   ```
4. Enter the desired time in seconds when prompted
5. Watch the countdown!

---

## Key Concepts Learnt

### Working with the `time` Module
- **Importing modules**: `import time`
- **`time.sleep()`**: Pauses execution for specified seconds
- **Real-time operations**: Creating delays for visual effects

### Countdown Techniques
- **Count up**: Using `range(0, my_time)`
- **Count down with `reversed()`**: Using `reversed(range(0, my_time))`
- **Count down with negative step**: Using `range(my_time, 0, -1)`
- **Most readable approach**: Negative step is clearest for countdowns

### Time Calculations
- **Modulo operator (`%`)**: Getting remainders for time units
- **Division**: Converting between time units
- **Seconds to minutes**: Divide by 60
- **Seconds to hours**: Divide by 3600
- **Extracting components**: Using modulo to get remaining time units

### String Formatting for Time
- **Format specifiers**: `:02` for two-digit padding
- **Leading zeros**: Ensuring consistent display format
- **Professional display**: Creating HH:MM:SS format
- **F-strings with calculations**: Combining math and formatting

### Mathematical Operations for Time
```python
# Breaking down 3665 seconds:
seconds = 3665 % 60        # 5 (remaining seconds)
minutes = (3665 // 60) % 60  # 1 (remaining minutes)
hours = 3665 // 3600       # 1 (total hours)
# Result: 01:01:05
```

---

## Common Use Cases & Extensions

### Basic Stopwatch
```python
import time

for x in range(0, 60):
    print(f"Elapsed: {x} seconds")
    time.sleep(1)
```

### Pomodoro Timer (25 minutes)
```python
import time

pomodoro_time = 25 * 60  # 25 minutes in seconds

for x in range(pomodoro_time, 0, -1):
    minutes = x // 60
    seconds = x % 60
    print(f"Work time: {minutes:02}:{seconds:02}")
    time.sleep(1)
print("Take a break!")
```

### Multiple Alarms
```python
import time

alarms = [10, 20, 30]  # seconds

for total in alarms:
    for x in range(total, 0, -1):
        print(f"Next alarm in: {x}s")
        time.sleep(1)
    print("ALARM!")
```

### Timer with Messages
```python
import time

my_time = int(input("Enter workout time (seconds): "))

for x in range(my_time, 0, -1):
    if x > 10:
        print(f"{x} - Keep going!")
    elif x > 5:
        print(f"{x} - Almost there!")
    else:
        print(f"{x} - Final push!")
    time.sleep(1)
print("Workout complete!")
```

---

## Understanding Time Conversion

### Why These Calculations Work

**For 3665 seconds (1 hour, 1 minute, 5 seconds):**

```python
# Step 1: Extract seconds
3665 % 60 = 5
# Because: 3665 = 61 minutes × 60 + 5 seconds

# Step 2: Extract minutes
3665 / 60 = 61.08...  → int(61) = 61 minutes total
61 % 60 = 1
# Because: 61 = 1 hour × 60 + 1 minute

# Step 3: Extract hours
3665 / 3600 = 1.01...  → int(1) = 1 hour
```

### Quick Reference

| Operation | Purpose | Example |
|-----------|---------|---------|
| `x % 60` | Get remaining seconds | `125 % 60 = 5` |
| `x // 60` | Get total minutes | `125 // 60 = 2` |
| `(x // 60) % 60` | Get remaining minutes | `3665: (61) % 60 = 1` |
| `x // 3600` | Get total hours | `3665 // 3600 = 1` |

---