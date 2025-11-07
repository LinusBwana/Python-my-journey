# Python Random Numbers & Number Guessing Game

This directory contains practice exercises for learning random number generation and building a number guessing game. These examples demonstrate how to use the `random` module and string validation methods.

## Contents

1. [The Random Module](#the-random-module)
2. [Generating Random Numbers](#generating-random-numbers)
3. [Number Guessing Game](#number-guessing-game)
4. [String Validation Methods](#string-validation-methods)
5. [Key Concepts Learnt](#key-concepts-learnt)

---

## The Random Module

The `random` module provides functions for generating random numbers and making random choices.

```python
import random
```

**Common functions:**
- `random.randint(a, b)` - Random integer between a and b (inclusive)
- `random.random()` - Random float between 0.0 and 1.0
- `random.choice(sequence)` - Random element from a sequence
- `random.shuffle(list)` - Shuffles a list in place

---

## Generating Random Numbers

### Example 1: Random Numbers

```python
import random

low = 1
high = 100

# Random integer
number = random.randint(low, high)

# Random float
number = random.random()
print(f"{number:.2f}")
```

**Explanation:**
- **`random.randint(low, high)`**: Returns random integer between low and high (both inclusive)
  - Example: `random.randint(1, 100)` can return any number from 1 to 100
- **`random.random()`**: Returns random float between 0.0 and 1.0
  - Example: Could return 0.4572894, 0.9123456, etc.
- **`{number:.2f}`**: Formats float to 2 decimal places

### Example 2: Random Choice from Sequence

```python
options = ("rock", "paper", "scissors")
pick = random.choice(options)
print(pick)
```

**Explanation:**
- **`random.choice(sequence)`**: Randomly selects one element from the sequence
- Works with lists, tuples, and strings
- Each element has equal probability of being selected

**Output:** Could be "rock", "paper", or "scissors"

### Example 3: Shuffling a List

```python
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "JOKER"]
random.shuffle(cards)
print(cards)
```

**Explanation:**
- **`random.shuffle(list)`**: Randomly reorders elements in the list
- Modifies the original list (in-place operation)
- Useful for card games, randomizing questions, etc.

**Output:** Cards in random order, e.g., `['K', '3', 'JOKER', '7', 'A', ...]`

---

## Number Guessing Game

A practice project that uses random numbers and input validation to create an interactive guessing game.

### Complete Code

```python
import random

lower = 1
upper = 10
no_guesses = 0
number = random.randint(lower, upper)

print("----Python Number Guessing Game----")
while True:
    guess = input(f"Guess a number between {lower} and {upper}: ")
    if guess.isdigit():
        guess = int(guess)
        no_guesses += 1
        if guess == number:
            print(f"CORRECT GUESS. The answer is {guess}")
            print(f"The number of guesses is: {no_guesses}")
            break
        elif guess < number:
            print("Too Low! Try again.")
            print(f"The number of guesses is: {no_guesses}")
            continue
        elif guess > number:
            print("Too High! Try again.")
            print(f"The number of guesses is: {no_guesses}")
            continue
    else:
        if guess == "q":
            print(f"The number of guesses is: {no_guesses}.\nThe correct answer was {number}")
            print("Bye")
            break
        else:
            no_guesses += 1
            print("Guess should an integer:")
            print(f"The number of guesses is: {no_guesses}")
```

### How the Game Works

1. Program generates random number between 1 and 10
2. User guesses a number
3. Program validates input is a digit using `.isdigit()`
4. Provides feedback: too low, too high, or correct
5. Tracks number of guesses
6. User can quit by entering 'q'
7. Game ends when correct guess or user quits

### Example Run

```
----Python Number Guessing Game----
Guess a number between 1 and 10: 5
Too High! Try again.
The number of guesses is: 1
Guess a number between 1 and 10: 3
Too Low! Try again.
The number of guesses is: 2
Guess a number between 1 and 10: 4
CORRECT GUESS. The answer is 4
The number of guesses is: 3
```

### Code Breakdown

#### 1. Setup

```python
import random

lower = 1
upper = 10
no_guesses = 0
number = random.randint(lower, upper)
```

- **Generate random number**: Creates target number between 1 and 10
- **Initialize counter**: Tracks number of attempts
- **Define range**: Sets lower and upper bounds

#### 2. Main Game Loop

```python
print("----Python Number Guessing Game----")
while True:
    guess = input(f"Guess a number between {lower} and {upper}: ")
```

- **Infinite loop**: Continues until break condition
- **Dynamic prompt**: Shows valid range using f-string

#### 3. Input Validation

```python
if guess.isdigit():
    guess = int(guess)
    no_guesses += 1
```

- **`.isdigit()`**: Checks if input contains only digits
- **Convert to int**: Changes string to integer for comparison
- **Count attempt**: Increments guess counter

#### 4. Number Comparison

```python
if guess == number:
    print(f"CORRECT GUESS. The answer is {guess}")
    print(f"The number of guesses is: {no_guesses}")
    break
elif guess < number:
    print("Too Low! Try again.")
    print(f"The number of guesses is: {no_guesses}")
    continue
elif guess > number:
    print("Too High! Try again.")
    print(f"The number of guesses is: {no_guesses}")
    continue
```

- **Exact match**: Displays success message and exits
- **Too low**: Hints to guess higher
- **Too high**: Hints to guess lower
- **`continue`**: Returns to start of loop

#### 5. Handling Non-Digit Input

```python
else:
    if guess == "q":
        print(f"The number of guesses is: {no_guesses}.\nThe correct answer was {number}")
        print("Bye")
        break
    else:
        no_guesses += 1
        print("Guess should an integer:")
        print(f"The number of guesses is: {no_guesses}")
```

- **Quit option**: Allows user to exit with 'q'
- **Invalid input**: Counts as guess and shows error
- **Reveal answer**: Shows correct number when quitting

---

## String Validation Methods

Python provides built-in methods to validate string content. These are essential for input validation.

### Overview

| Method | Returns True If | Example |
|--------|----------------|---------|
| `.isdigit()` | All characters are digits (0-9) | `"123".isdigit()` → `True` |
| `.isalpha()` | All characters are letters (a-z, A-Z) | `"Hello".isalpha()` → `True` |
| `.isalnum()` | All characters are letters or digits | `"Hello123".isalnum()` → `True` |

### Detailed Examples

#### .isdigit()

Checks if all characters in the string are digits.

```python
"123".isdigit()      # True - all digits
"12.5".isdigit()     # False - contains decimal point
"12a".isdigit()      # False - contains letter
"-5".isdigit()       # False - contains minus sign
"".isdigit()         # False - empty string
```

**Use case:** Validating numeric input (as used in the guessing game)

```python
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    # Process number
else:
    print("Invalid input")
```

#### .isalpha()

Checks if all characters in the string are letters (no spaces, digits, or special characters).

```python
"Hello".isalpha()        # True - all letters
"Hello World".isalpha()  # False - contains space
"Hello123".isalpha()     # False - contains digits
"Hello!".isalpha()       # False - contains punctuation
"".isalpha()             # False - empty string
```

**Use case:** Validating name input

```python
name = input("Enter your name: ")
if name.isalpha():
    print(f"Welcome, {name}!")
else:
    print("Name should contain only letters")
```

#### .isalnum()

Checks if all characters are alphanumeric (letters or digits, no spaces or special characters).

```python
"Hello123".isalnum()     # True - letters and digits
"User2024".isalnum()     # True - letters and digits
"Hello World".isalnum()  # False - contains space
"Hello-123".isalnum()    # False - contains hyphen
"".isalnum()             # False - empty string
```

**Use case:** Validating usernames

```python
username = input("Enter username: ")
if username.isalnum():
    print("Valid username")
else:
    print("Username can only contain letters and numbers")
```

### Comparison Table

```python
text = "Hello"
text.isdigit()    # False (no digits)
text.isalpha()    # True (all letters)
text.isalnum()    # True (letters are alphanumeric)

text = "123"
text.isdigit()    # True (all digits)
text.isalpha()    # False (no letters)
text.isalnum()    # True (digits are alphanumeric)

text = "Hello123"
text.isdigit()    # False (has letters)
text.isalpha()    # False (has digits)
text.isalnum()    # True (all are letters or digits)

text = "Hello 123"
text.isdigit()    # False (has space and letters)
text.isalpha()    # False (has space and digits)
text.isalnum()    # False (has space)
```

---

## How to Run

1. Navigate to the project directory
2. Run either Python file:
   ```bash
   python generating_random_numbers.py
   python number_guessing_game.py
   ```

---

## Key Concepts Learnt

### Random Module Functions
- **Importing modules**: Using `import random`
- **`random.randint(a, b)`**: Generating random integers in a range
- **`random.random()`**: Generating random floats between 0 and 1
- **`random.choice(sequence)`**: Selecting random element from collection
- **`random.shuffle(list)`**: Randomizing order of list elements
- **In-place operations**: `shuffle()` modifies original list

### String Validation Methods
- **`.isdigit()`**: Validating numeric input without try-except
- **`.isalpha()`**: Checking for alphabetic characters only
- **`.isalnum()`**: Checking for alphanumeric characters
- **Use cases**: Input validation, data cleaning, format checking
- **Return values**: All return boolean (True or False)

### Input Validation Patterns
- **Type checking**: Validating before type conversion
- **Error prevention**: Avoiding ValueError with `.isdigit()`
- **User feedback**: Informing users of input requirements
- **Multiple conditions**: Checking different input scenarios

### Game Logic Implementation
- **State tracking**: Using variables to track game state (guesses, number)
- **Conditional branching**: Different actions based on comparisons
- **Loop control**: Using break and continue strategically
- **User hints**: Providing feedback (too high, too low)

### Program Flow Control
- **Infinite loops**: Using `while True` for ongoing interaction
- **Exit conditions**: Breaking loop when goal met or user quits
- **Continue statements**: Skipping to next iteration
- **Multiple exit points**: Different ways to end the game

### Counter Patterns
- **Initialization**: Starting counter at 0
- **Incrementing**: Adding 1 each iteration
- **Placement**: Where to increment (before or after validation)
- **Display**: Showing counter to user

---

## Practical Applications

### Random Number Applications

#### Dice Roller
```python
import random

def roll_dice(num_dice=1):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        print(f"Rolled: {roll}")
        total += roll
    return total

print(f"Total: {roll_dice(2)}")
```

#### Password Generator
```python
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
password = ""
for _ in range(12):
    password += random.choice(chars)
print(f"Password: {password}")
```

#### Lottery Number Generator
```python
import random

numbers = random.sample(range(1, 50), 6)
numbers.sort()
print(f"Lottery numbers: {numbers}")
```

### String Validation Applications

#### Username Validator
```python
def validate_username(username):
    if len(username) < 3:
        return False, "Username too short"
    if not username.isalnum():
        return False, "Only letters and numbers allowed"
    if username.isdigit():
        return False, "Username cannot be only numbers"
    return True, "Valid username"

username = input("Enter username: ")
valid, message = validate_username(username)
print(message)
```

#### Age Input Validator
```python
age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    if 0 < age < 120:
        print(f"Age: {age}")
    else:
        print("Invalid age range")
else:
    print("Age must be a number")
```

---

## Game Enhancement Ideas

### Enhancement 1: Difficulty Levels
```python
difficulty = input("Choose difficulty (easy/medium/hard): ")
if difficulty == "easy":
    lower, upper = 1, 10
elif difficulty == "medium":
    lower, upper = 1, 50
else:
    lower, upper = 1, 100
```

### Enhancement 2: Limited Attempts
```python
max_attempts = 5
if no_guesses >= max_attempts:
    print("Out of guesses! Game Over!")
    break
```

### Enhancement 3: Score System
```python
# Fewer guesses = higher score
score = max(0, 100 - (no_guesses * 10))
print(f"Your score: {score}")
```

### Enhancement 4: Play Again
```python
play_again = input("Play again? (y/n): ")
if play_again.lower() == "y":
    # Reset game
    no_guesses = 0
    number = random.randint(lower, upper)
else:
    break
```

### Enhancement 5: Hints System
```python
hints_left = 3
if user_wants_hint and hints_left > 0:
    if number % 2 == 0:
        print("Hint: The number is even")
    else:
        print("Hint: The number is odd")
    hints_left -= 1
```

---

## Common Random Module Functions

### Summary Table

| Function | Description | Example | Output |
|----------|-------------|---------|--------|
| `randint(a, b)` | Random integer a ≤ n ≤ b | `randint(1, 6)` | `4` |
| `random()` | Random float 0.0 ≤ n < 1.0 | `random()` | `0.7423` |
| `uniform(a, b)` | Random float a ≤ n ≤ b | `uniform(1.5, 5.5)` | `3.789` |
| `choice(seq)` | Random element from sequence | `choice(['a','b','c'])` | `'b'` |
| `choices(seq, k)` | k random elements with replacement | `choices([1,2,3], k=2)` | `[2, 2]` |
| `sample(seq, k)` | k random elements without replacement | `sample([1,2,3], k=2)` | `[1, 3]` |
| `shuffle(list)` | Shuffle list in place | `shuffle([1,2,3])` | `[3,1,2]` |

---