# Python Quiz Game

This directory contains a practice project for building a quiz game application. This example demonstrates how to use tuples, loops, input validation, and list manipulation to create an interactive quiz experience.

## Contents

1. [Program Overview](#program-overview)
2. [How the Program Works](#how-the-program-works)
3. [Code Breakdown](#code-breakdown)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## Program Overview

The **Quiz Game** allows users to:
- Answer multiple-choice questions
- Receive immediate feedback on each answer
- See the correct answer when wrong
- View their final score as a percentage

**Features:**
- 5 trivia questions with 4 options each
- Input validation to ensure valid choices
- Score tracking and calculation
- Results summary showing answers vs guesses

---

## How the Program Works

### Game Flow

1. User is presented with a question and 4 options (A, B, C, D)
2. User enters their answer
3. Program validates the input is A, B, C, or D
4. If correct, score increases and moves to next question
5. If incorrect, shows correct answer and moves to next question
6. After all questions, displays results summary with percentage score

### Example Run

```
-------------------
How many elements are in the periodic table?: 
A. 116
B. 117
C. 118
D. 119
Choose (A, B, C, D): c
CORRECT
-------------------
Which animal lays the largest eggs?: 
A. Whale
B. Crocodile
C. Elephant
D. Ostrich
Choose (A, B, C, D): a
INCORRECT
The correct answer is: D
-------------------
...
-------------------------
         RESULTS         
-------------------------
Answers: C D A A B 
Guesses: C A A A B 
Your score is: 60%
```

---

## Code Breakdown

### Complete Code

```python
# Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    while True:
        guess = input("Choose (A, B, C, D): ").upper()
        if guess in answers:
            guesses.append(guess)
            if guess == answers[question_num]:
                score += 1
                print("CORRECT")
            else:
                print("INCORRECT")
                print(f"The correct answer is: {answers[question_num]}")
            question_num += 1
            break
        else:
            print("Wrong input", end=". ")

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score / len(questions)) * 100)
print(f"Your score is: {score}%")
```

### Step-by-Step Explanation

#### 1. Data Structure Setup

```python
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
```

**Data structure explanation:**
- **`questions`**: Tuple containing 5 question strings
- **`options`**: 2D tuple - each inner tuple contains 4 answer choices for corresponding question
- **`answers`**: Tuple containing correct answers (letters only)
- **Why tuples?**: Questions and answers should not change during the game

**Parallel structure:**
```
questions[0] → options[0] → answers[0]
questions[1] → options[1] → answers[1]
...
```

#### 2. Initialize Variables

```python
guesses = []
score = 0
question_num = 0
```

- **`guesses`**: Empty list to store user's answers
- **`score`**: Counter for correct answers
- **`question_num`**: Index tracker for current question

#### 3. Main Game Loop

```python
for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
```

**How it works:**
- **Outer loop**: Iterates through each question
- **Separator**: Prints line for visual clarity
- **Question display**: Prints current question
- **Inner loop**: Prints all options for current question using `question_num` as index

#### 4. Input Validation and Answer Checking

```python
while True:
    guess = input("Choose (A, B, C, D): ").upper()
    if guess in answers:
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT")
        else:
            print("INCORRECT")
            print(f"The correct answer is: {answers[question_num]}")
        question_num += 1
        break
    else:
        print("Wrong input", end=". ")
```

**Step-by-step:**
1. **`.upper()`**: Converts input to uppercase for case-insensitive comparison
2. **`if guess in answers`**: Validates input is A, B, C, or D
3. **Valid input**:
   - Append to guesses list
   - Check if matches correct answer
   - Increment score if correct
   - Display feedback
   - Increment question number
   - Break validation loop
4. **Invalid input**:
   - Display error message
   - Continue validation loop (ask again)

**Note about validation:** `if guess in answers` checks if the guess exists anywhere in the answers tuple. Since answers only contain A, B, C, and D, this effectively validates the input.

#### 5. Display Results

```python
print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
```

**How it works:**
- **Header**: Prints formatted results section
- **Answers row**: Displays all correct answers on one line
- **Guesses row**: Displays all user guesses on one line
- **`end=" "`**: Keeps items on same line with space separator
- **`print()`**: Moves to next line after each row

#### 6. Calculate and Display Score

```python
score = int((score / len(questions)) * 100)
print(f"Your score is: {score}%")
```

**Calculation:**
1. `score / len(questions)` - Divide correct answers by total questions (gives decimal)
2. `* 100` - Convert to percentage
3. `int()` - Convert to integer (removes decimals)

**Example:**
- 3 correct out of 5: `(3 / 5) * 100 = 60%`
- 5 correct out of 5: `(5 / 5) * 100 = 100%`

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python quiz_game.py
   ```
3. Answer each question by entering A, B, C, or D
4. View your final score at the end

---

## Key Concepts Learnt

### Working with Tuples
- **Immutability**: Using tuples for data that shouldn't change
- **Performance**: Tuples are faster than lists
- **Use case**: Perfect for storing quiz questions and answers
- **Accessing**: Using index to access specific elements

### 2D Data Structures
- **2D tuple**: Tuple containing other tuples (options)
- **Parallel structures**: Multiple collections with related data at same indices
- **Indexing**: Using `options[question_num]` to get options for current question
- **Nested iteration**: Looping through outer tuple, then inner tuples

### Input Validation
- **Case handling**: Using `.upper()` for case-insensitive input
- **Membership testing**: Using `in` to check if input is valid
- **Loop until valid**: Using `while True` with `break` when input is valid
- **User feedback**: Informing user of invalid input

### Score Tracking
- **Counter pattern**: Incrementing score for correct answers
- **List accumulation**: Appending guesses to track user answers
- **Percentage calculation**: Converting score to percentage
- **Type conversion**: Using `int()` to remove decimals

### Loop Control
- **For loop**: Iterating through questions
- **While loop**: Validating input until correct
- **Break statement**: Exiting validation loop when input is valid
- **Question tracking**: Using counter to track current question index

### Output Formatting
- **Separators**: Using dashes for visual clarity
- **`end` parameter**: Controlling print output (newline vs same line)
- **F-strings**: Formatting dynamic output
- **Alignment**: Creating organized results display

### List Operations
- **Appending**: Adding guesses to list with `.append()`
- **Iteration**: Looping through guesses for display
- **Length**: Using `len()` for calculations

---

## Understanding the Validation Logic

### Why `if guess in answers` Works

```python
answers = ("C", "D", "A", "A", "B")
guess = input("Choose (A, B, C, D): ").upper()
if guess in answers:
    # Valid input
```

**Explanation:**
- The `answers` tuple contains only valid letters (A, B, C, D)
- `in` checks if guess exists anywhere in the tuple
- Any letter A-D will be found since they're all answers to some question
- Letters outside A-D won't be found

**Example:**
```python
"A" in answers  # True (A is answer to questions 3 and 4)
"B" in answers  # True (B is answer to question 5)
"C" in answers  # True (C is answer to question 1)
"D" in answers  # True (D is answer to question 2)
"E" in answers  # False (E is not a valid option)
"Z" in answers  # False (Z is not a valid option)
```

## Data Structure Breakdown

### Understanding Parallel Collections

**Visual representation:**
```
Index:      0           1           2           3           4
          ┌─────────┬─────────┬─────────┬─────────┬─────────┐
questions │ "How..."│"Which..."│"What..."│"How..."│"Which..."│
          ├─────────┼─────────┼─────────┼─────────┼─────────┤
options   │(A,B,C,D)│(A,B,C,D)│(A,B,C,D)│(A,B,C,D)│(A,B,C,D)│
          ├─────────┼─────────┼─────────┼─────────┼─────────┤
answers   │   "C"   │   "D"   │   "A"   │   "A"   │   "B"   │
          └─────────┴─────────┴─────────┴─────────┴─────────┘
```

**Accessing related data:**
```python
question_num = 0
print(questions[question_num])    # First question
print(options[question_num])      # Options for first question
print(answers[question_num])      # Answer to first question
```

### Why Use 2D Tuple for Options?

```python
options = (("A. 116", "B. 117", "C. 118", "D. 119"),  # Question 0
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),  # Question 1
           ...)
```

**Benefits:**
1. **Organization**: Each question's options grouped together
2. **Easy access**: `options[question_num]` gets all options for current question
3. **Immutability**: Options can't be accidentally changed
4. **Iteration**: Can easily loop through options to display them

---