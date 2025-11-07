# Python Rock Paper Scissors Game

This directory contains a practice project for building a Rock Paper Scissors game. This example demonstrates how to use random choices, complex conditional logic, and score tracking to create an interactive game against the computer.

## Contents

1. [Program Overview](#program-overview)
2. [How the Game Works](#how-the-game-works)
3. [Code Breakdown](#code-breakdown)
4. [Game Logic Explained](#game-logic-explained)
5. [Key Concepts Learnt](#key-concepts-learnt)

---

## Program Overview

The **Rock Paper Scissors Game** allows users to:
- Play against the computer
- Make moves: rock, paper, or scissors
- Track scores throughout the session
- Quit anytime and see final results

**Features:**
- Random computer moves
- Input validation
- Score tracking (5 points per win)
- Case-insensitive input
- Final results summary

---

## How the Game Works

### Game Rules

- **Rock** beats Scissors
- **Scissors** beats Paper
- **Paper** beats Rock
- Same move = Draw

### Score System

- Win: +5 points
- Lose: Opponent gets +5 points
- Draw: No points awarded

### User Interaction Flow

1. Computer secretly picks a move
2. User enters their move (rock, paper, or scissors)
3. Program compares moves and determines winner
4. Scores are updated and displayed
5. Process repeats until user enters 'q'
6. Final scores and overall result are displayed

### Example Run

```
Pick a move: (rock, paper or scissors). Press q to quit game: rock
Your move:rock | computer move:scissors | Results:You win
Your score:5 | Computer score:0
Pick a move: (rock, paper or scissors). Press q to quit game: paper
Your move:paper | computer move:paper | Results:Draw
Your score:5 | Computer score:0
Pick a move: (rock, paper or scissors). Press q to quit game: scissors
Your move:scissors | computer move:rock | Results:You Lose
Your score:5 | Computer score:5
Pick a move: (rock, paper or scissors). Press q to quit game: q
Your score:5 | computer score:5 | Results:Draw
Bye
```

---

## Code Breakdown

### Complete Code

```python
import random

options = ("rock", "paper", "scissors")
results = ("You win", "You Lose", "Draw")
your_score = 0
computer_score = 0

while True:
    computer_move = random.choice(options)
    your_move = input("Pick a move: (rock, paper or scissors). Press q to quit game: ").lower()
    if your_move not in options:
        if your_move == "q":
            if your_score > computer_score:
                result = results[0]
            elif your_score < computer_score:
                result = results[1]
            else:
                result = results[2]
            print(f"Your score:{your_score} | computer score:{computer_score} | Results:{result}")
            print("Bye")
            break
        else:
            print("Incorrect Option")
            print(f"Your score:{your_score} | Computer score:{computer_score}")
            continue

    if your_move == computer_move:
        result = results[2]
    elif (your_move == "rock" and computer_move != "paper") or \
            (your_move == "paper" and computer_move != "scissors") or \
            (your_move == "scissors" and computer_move != "rock"):
        result = results[0]
    else:
        result = results[1]

    if result == results[0]:
        your_score += 5
    if result == results[1]:
        computer_score += 5

    print(f"Your move:{your_move} | computer move:{computer_move} | Results:{result}")
    print(f"Your score:{your_score} | Computer score:{computer_score}")
    continue
```

### Step-by-Step Explanation

#### 1. Setup and Initialization

```python
import random

options = ("rock", "paper", "scissors")
results = ("You win", "You Lose", "Draw")
your_score = 0
computer_score = 0
```

**Explanation:**
- **`options`**: Tuple containing valid moves
- **`results`**: Tuple containing possible outcomes
- **`your_score`**: Tracks player's points
- **`computer_score`**: Tracks computer's points
- **Why tuples?**: Valid moves and results shouldn't change

**Index mapping:**
```
results[0] = "You win"
results[1] = "You Lose"
results[2] = "Draw"
```

#### 2. Main Game Loop

```python
while True:
    computer_move = random.choice(options)
    your_move = input("Pick a move: (rock, paper or scissors). Press q to quit game: ").lower()
```

**Explanation:**
- **Infinite loop**: Continues until user quits
- **`random.choice(options)`**: Computer randomly picks from rock, paper, scissors
- **`.lower()`**: Converts input to lowercase for case-insensitive comparison

#### 3. Input Validation

```python
if your_move not in options:
    if your_move == "q":
        if your_score > computer_score:
            result = results[0]
        elif your_score < computer_score:
            result = results[1]
        else:
            result = results[2]
        print(f"Your score:{your_score} | computer score:{computer_score} | Results:{result}")
        print("Bye")
        break
    else:
        print("Incorrect Option")
        print(f"Your score:{your_score} | Computer score:{computer_score}")
        continue
```

**Explanation:**
- **First check**: Is input a valid move?
- **If not valid**:
  - **Check for 'q'**: User wants to quit
    - Compare final scores to determine overall winner
    - Display final results
    - Break out of game loop
  - **Any other invalid input**: 
    - Show error message
    - Display current scores
    - Continue to next iteration (ask for input again)

**Determining overall winner:**
```
your_score > computer_score  → "You win"
your_score < computer_score  → "You Lose"
your_score == computer_score → "Draw"
```

#### 4. Game Logic - Determining Round Winner

```python
if your_move == computer_move:
    result = results[2]
elif (your_move == "rock" and computer_move != "paper") or \
        (your_move == "paper" and computer_move != "scissors") or \
        (your_move == "scissors" and computer_move != "rock"):
    result = results[0]
else:
    result = results[1]
```

**Explanation:**

**Condition 1: Draw**
```python
if your_move == computer_move:
    result = results[2]  # "Draw"
```
Both players chose the same move.

**Condition 2: You Win**
```python
elif (your_move == "rock" and computer_move != "paper") or \
        (your_move == "paper" and computer_move != "scissors") or \
        (your_move == "scissors" and computer_move != "rock"):
    result = results[0]  # "You win"
```

Breaking down the winning conditions:
- **Rock wins**: `your_move == "rock" and computer_move != "paper"`
  - Computer must be scissors (rock beats scissors)
  - Computer can't be paper (paper beats rock)
  
- **Paper wins**: `your_move == "paper" and computer_move != "scissors"`
  - Computer must be rock (paper beats rock)
  - Computer can't be scissors (scissors beats paper)
  
- **Scissors wins**: `your_move == "scissors" and computer_move != "rock"`
  - Computer must be paper (scissors beats paper)
  - Computer can't be rock (rock beats scissors)

**Condition 3: You Lose**
```python
else:
    result = results[1]  # "You Lose"
```
If it's not a draw and you didn't win, you lost.

#### 5. Update Scores

```python
if result == results[0]:
    your_score += 5
if result == results[1]:
    computer_score += 5
```

**Explanation:**
- Winner gets 5 points
- Draw gives no points to either player
- Uses separate if statements (not elif) to check each condition

#### 6. Display Round Results

```python
print(f"Your move:{your_move} | computer move:{computer_move} | Results:{result}")
print(f"Your score:{your_score} | Computer score:{computer_score}")
continue
```

**Explanation:**
- Shows what both players chose
- Shows round result
- Shows updated scores
- `continue` returns to start of loop (not strictly necessary at end of loop)

---

## Game Logic Explained

### Understanding the Winning Condition

The game uses a clever approach to check wins:

```python
(your_move == "rock" and computer_move != "paper")
```

This translates to: "You played rock AND computer didn't play the move that beats rock"

**Why this works:**

For rock:
- Rock beats scissors ✓
- Rock loses to paper ✗
- Rock draws with rock (already handled)

So if you play rock and computer didn't play paper, you either:
- Win (computer played scissors)
- This condition returns True

### Complete Win Matrix

| Your Move | Computer Move | Result | Condition Met |
|-----------|---------------|--------|---------------|
| Rock | Rock | Draw | First condition |
| Rock | Paper | Lose | Else |
| Rock | Scissors | Win | Second condition |
| Paper | Rock | Win | Second condition |
| Paper | Paper | Draw | First condition |
| Paper | Scissors | Lose | Else |
| Scissors | Rock | Lose | Else |
| Scissors | Paper | Win | Second condition |
| Scissors | Scissors | Draw | First condition |

### Alternative Logic Approaches

#### Approach 1: Explicit Win Conditions
```python
if your_move == computer_move:
    result = "Draw"
elif (your_move == "rock" and computer_move == "scissors") or \
     (your_move == "paper" and computer_move == "rock") or \
     (your_move == "scissors" and computer_move == "paper"):
    result = "You win"
else:
    result = "You Lose"
```

#### Approach 2: Dictionary Mapping
```python
wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

if your_move == computer_move:
    result = "Draw"
elif wins[your_move] == computer_move:
    result = "You win"
else:
    result = "You Lose"
```

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python rock_paper_scissors.py
   ```
3. Enter your move when prompted
4. Press 'q' to quit and see final results

---

## Key Concepts Learnt

### Random Module Usage
- **`random.choice()`**: Selecting random element from sequence
- **Game AI**: Creating computer opponent
- **Unpredictability**: Making games more interesting

### Complex Conditional Logic
- **Multiple conditions**: Using `and` and `or` operators
- **Logical negation**: Using `!=` to check what something is not
- **Condition chaining**: Combining multiple checks with `or`
- **Order matters**: Checking draw first, then win, then assuming loss

### Input Validation
- **Membership testing**: Using `in` to check valid options
- **Case handling**: Using `.lower()` for case-insensitive input
- **Multiple outcomes**: Different handling for valid, invalid, and quit

### Score Tracking
- **Accumulation**: Adding points to scores
- **Conditional updates**: Only updating when certain conditions met
- **Final comparison**: Determining overall winner from scores

### Program Flow Control
- **Infinite loops**: Using `while True` for continuous play
- **Multiple exit points**: Breaking on quit command
- **Continue statement**: Restarting loop after error or at end

### String Formatting
- **F-strings with multiple variables**: Displaying complex information
- **Pipe separator**: Using `|` for visual organization
- **Dynamic output**: Showing changing scores and results

### Data Organization
- **Tuple for constants**: Storing valid options and results
- **Index access**: Using results tuple with indices
- **Immutability**: Protecting game rules from changes

---

## Understanding the Logic Flow

### Flowchart of Game Logic

```
Start
  ↓
Computer picks random move
  ↓
User enters move
  ↓
Is move valid? ──No──→ Is it 'q'? ──Yes──→ Show final results → Exit
  ↓                          ↓
 Yes                        No
  ↓                          ↓
Same moves? ──Yes──→ Draw   Show error → Continue loop
  ↓
 No
  ↓
Check winning conditions
  ↓
Win? ──Yes──→ You win
  ↓
 No
  ↓
You lose
  ↓
Update scores
  ↓
Display results
  ↓
Continue loop
```