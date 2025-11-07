# Python Banking Program Exercise

This directory contains a practice project for building a banking program. This example demonstrates how to create an interactive menu-driven application using functions, loops, and validation.

## Contents

1. [Program Overview](#program-overview)
2. [How the Program Works](#how-the-program-works)
3. [Code Breakdown](#code-breakdown)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## Program Overview

The **Banking Program** allows users to:
- Check their account balance
- Deposit money
- Withdraw money
- Exit the program

**Features:**
- Menu-driven interface
- Input validation
- Balance tracking
- Error handling
- Professional formatting

---

## How the Program Works

### User Interaction Flow

1. Display welcome message and menu
2. User selects an option (1-4)
3. Perform selected operation:
   - Show balance
   - Deposit money (with validation)
   - Withdraw money (with validation)
   - Exit program
4. Repeat until user chooses to exit
5. Display goodbye message

### Example Run

```
******************************
Welcome To ABSA Bank
1. Show balance
2. Deposit
3. Withdraw
4. Exit
******************************
Enter your choice (1-4): 2
Enter amount to deposit in Ksh: 5000
******************************
Welcome To ABSA Bank
1. Show balance
2. Deposit
3. Withdraw
4. Exit
******************************
Enter your choice (1-4): 1
******************************
Your balance is Ksh.5000.00
******************************
******************************
Welcome To ABSA Bank
1. Show balance
2. Deposit
3. Withdraw
4. Exit
******************************
Enter your choice (1-4): 3
Enter amount to withdraw in Ksh: 2000
******************************
Welcome To ABSA Bank
1. Show balance
2. Deposit
3. Withdraw
4. Exit
******************************
Enter your choice (1-4): 1
******************************
Your balance is Ksh.3000.00
******************************
******************************
Welcome To ABSA Bank
1. Show balance
2. Deposit
3. Withdraw
4. Exit
******************************
Enter your choice (1-4): 4
******************************
Thank You Have A Nice Day
******************************
```

---

## Code Breakdown

### Complete Code

```python
def show_balance(balance):
    print("******************************")
    print(f"Your balance is Ksh.{balance:.2f}")
    print("******************************")

def deposit():
    amount = float(input("Enter amount to deposit in Ksh: "))

    if amount < 0:
        print("******************************")
        print("That is an invalid amount")
        print("******************************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw in Ksh: "))

    if amount > balance:
        print("******************************")
        print("Insufficient amount")
        print("******************************")
        return 0
    elif amount < 0:
        print("******************************")
        print("Amount must be greater than 0 ")
        print("******************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("******************************")
        print("Welcome To ABSA Bank")

        print("1. Show balance\n2. Deposit\n3. Withdraw\n4. Exit")
        print("******************************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("******************************")
            print("You have entered an invalid choice")
            print("******************************")

    print("******************************")
    print("Thank You Have A Nice Day")
    print("******************************")
    
if __name__ == "__main__":
    main()
```

### Step-by-Step Explanation

#### 1. Show Balance Function

```python
def show_balance(balance):
    print("******************************")
    print(f"Your balance is Ksh.{balance:.2f}")
    print("******************************")
```

**How it works:**
- **Parameter**: Takes current balance
- **Formatting**: Uses `:.2f` to display 2 decimal places
- **Currency**: Displays amount in Kenyan Shillings (Ksh)
- **Visual**: Border for professional appearance

#### 2. Deposit Function

```python
def deposit():
    amount = float(input("Enter amount to deposit in Ksh: "))

    if amount < 0:
        print("******************************")
        print("That is an invalid amount")
        print("******************************")
        return 0
    else:
        return amount
```

**How it works:**
- **Input**: Prompts user for deposit amount
- **Validation**: Checks if amount is negative
- **Invalid amount**: Returns 0 if negative (no deposit)
- **Valid amount**: Returns entered amount to add to balance
- **Return value**: Used to update balance in main function

**Validation logic:**
```
amount < 0  → Return 0 (invalid)
amount >= 0 → Return amount (valid)
```

#### 3. Withdraw Function

```python
def withdraw(balance):
    amount = float(input("Enter amount to withdraw in Ksh: "))

    if amount > balance:
        print("******************************")
        print("Insufficient amount")
        print("******************************")
        return 0
    elif amount < 0:
        print("******************************")
        print("Amount must be greater than 0 ")
        print("******************************")
        return 0
    else:
        return amount
```

**How it works:**
- **Parameter**: Takes current balance for validation
- **Input**: Prompts user for withdrawal amount
- **Validation 1**: Checks if amount exceeds balance
- **Validation 2**: Checks if amount is negative
- **Invalid**: Returns 0 (no withdrawal)
- **Valid**: Returns amount to subtract from balance

**Validation logic:**
```
amount > balance  → Return 0 (insufficient funds)
amount < 0        → Return 0 (invalid)
Otherwise         → Return amount (valid)
```

#### 4. Main Function

```python
def main():
    balance = 0
    is_running = True

    while is_running:
        print("******************************")
        print("Welcome To ABSA Bank")
        print("1. Show balance\n2. Deposit\n3. Withdraw\n4. Exit")
        print("******************************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("******************************")
            print("You have entered an invalid choice")
            print("******************************")

    print("******************************")
    print("Thank You Have A Nice Day")
    print("******************************")
```

**How it works:**

1. **Initialization**:
   - `balance = 0`: Start with empty account
   - `is_running = True`: Control variable for loop

2. **Main Loop**:
   - Continues while `is_running` is `True`
   - Displays menu each iteration
   - Processes user choice

3. **Menu Options**:
   - **Option 1**: Call `show_balance(balance)` to display balance
   - **Option 2**: Call `deposit()`, add returned amount to balance
   - **Option 3**: Call `withdraw(balance)`, subtract returned amount
   - **Option 4**: Set `is_running = False` to exit loop
   - **Invalid**: Display error message

4. **Exit**:
   - Loop ends when `is_running` becomes `False`
   - Display goodbye message

**Balance updates:**
```python
balance += deposit()      # Add deposit to balance
balance -= withdraw(balance)  # Subtract withdrawal from balance
```

#### 5. Entry Point

```python
if __name__ == "__main__":
    main()
```

**How it works:**
- Only runs `main()` if script is executed directly
- Allows functions to be imported without running program
- Standard Python practice

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python banking_program_exercise.py
   ```
3. Follow the on-screen menu to interact with the program
4. Choose option 4 to exit

---

## Key Concepts Learnt

### Function Design

**1. Single Responsibility**
- Each function has one clear purpose
- `show_balance()`: Display balance only
- `deposit()`: Handle deposits only
- `withdraw()`: Handle withdrawals only
- `main()`: Coordinate program flow

**2. Function Parameters**
- `show_balance(balance)`: Needs balance to display
- `withdraw(balance)`: Needs balance for validation
- `deposit()`: No parameters needed (gets input internally)

**3. Return Values**
- `show_balance()`: No return (just displays)
- `deposit()`: Returns amount to add (or 0 if invalid)
- `withdraw()`: Returns amount to subtract (or 0 if invalid)
- Using return values to update balance

### Input Validation

**Deposit validation:**
- Negative amounts rejected
- Returns 0 instead of invalid amount
- User informed of error

**Withdraw validation:**
- Checks against available balance
- Prevents negative withdrawals
- Multiple validation conditions
- Returns 0 for any invalid input

### Control Flow

**1. Loop Control**
- Using `while is_running:` for main loop
- Boolean flag to control execution
- Setting `is_running = False` to exit
- Alternative: Could use `break` statement

**2. Menu-Driven Interface**
- Displaying options to user
- Processing user choice with if-elif-else
- Handling invalid choices
- Repeating until exit

### State Management

**Tracking balance:**
- Initialize at 0
- Update through additions and subtractions
- Pass to functions as needed
- Maintain throughout program execution

**Program state:**
- `is_running` controls program execution
- Balance persists across menu selections
- State updated based on user actions

### User Experience

**Professional formatting:**
- Consistent border design (`******************************`)
- Clear messages
- Structured menu
- Feedback for all actions

**Error handling:**
- Invalid amounts
- Insufficient funds
- Invalid menu choices
- User-friendly error messages

### Program Structure

**Modular design:**
- Separate functions for each operation
- Main function coordinates everything
- Easy to test individual functions
- Easy to add new features

**Entry point pattern:**
- Using `if __name__ == "__main__":`
- Allows import without execution
- Standard Python practice

---

## Program Flow Diagram

```
Start
  ↓
Initialize (balance=0, is_running=True)
  ↓
┌─────────────────────────────┐
│ While is_running is True    │
│  ↓                          │
│ Display Menu                │
│  ↓                          │
│ Get User Choice             │
│  ↓                          │
│ Process Choice:             │
│  • 1: Show Balance          │
│  • 2: Deposit → Update Balance
│  • 3: Withdraw → Update Balance
│  • 4: Set is_running=False │
│  • Invalid: Show Error      │
│  ↓                          │
└─────────────────────────────┘
  ↓
Display Goodbye Message
  ↓
End
```

---

## Validation Flow

### Deposit Validation
```
User enters amount
  ↓
Is amount < 0?
  ├─ Yes → Show error, return 0
  └─ No  → Return amount
```

### Withdraw Validation
```
User enters amount
  ↓
Is amount > balance?
  ├─ Yes → Show "Insufficient", return 0
  └─ No  → Continue
       ↓
  Is amount < 0?
    ├─ Yes → Show error, return 0
    └─ No  → Return amount
```
---

## Testing the Program

### Test Case 1: Deposit
```
Input: Option 2, amount 1000
Expected: Balance becomes 1000
```

### Test Case 2: Withdraw (Valid)
```
Input: Deposit 1000, then Option 3, amount 500
Expected: Balance becomes 500
```

### Test Case 3: Withdraw (Insufficient)
```
Input: Balance 500, Option 3, amount 1000
Expected: Error message, balance stays 500
```

### Test Case 4: Negative Deposit
```
Input: Option 2, amount -100
Expected: Error message, balance unchanged
```

### Test Case 5: Negative Withdraw
```
Input: Option 3, amount -100
Expected: Error message, balance unchanged
```

### Test Case 6: Invalid Menu Choice
```
Input: Option 5 (or any invalid)
Expected: Error message, menu redisplays
```

---

## Best Practices Demonstrated

### 1. Input Validation
- Check for negative amounts
- Check for insufficient funds
- Return sensible defaults (0) on invalid input

### 2. Function Organization
- Small, focused functions
- Clear function names
- Appropriate use of parameters and returns

### 3. User Feedback
- Clear prompts
- Informative error messages
- Professional formatting
- Confirmation of actions

### 4. Code Maintainability
- Functions easy to test independently
- Clear variable names
- Consistent formatting
- Comments where needed

### 5. Error Prevention
- Validation before operations
- Safe default returns
- Graceful error handling

---