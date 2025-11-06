# Python Shopping Cart Program

This directory contains a practice project for building a shopping cart application. This example demonstrates how to use lists, loops, input validation, and exception handling to create a functional shopping cart.

## Contents

1. [Program Overview](#program-overview)
2. [How the Program Works](#how-the-program-works)
3. [Code Breakdown](#code-breakdown)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## Program Overview

The **Shopping Cart Program** allows users to:
- Add food items with their prices
- Validate that prices are numeric
- Display all items with their prices
- Calculate the total cost

**Features:**
- Input validation with error handling
- Price formatting in Kenyan Shillings (Ksh)
- Clean, formatted output
- User-friendly interface

---

## How the Program Works

### User Interaction Flow

1. User is prompted to enter a food item (or 'q' to quit)
2. If user enters a food item, they're asked for the price
3. Program validates that price is numeric
4. If invalid, user is prompted again until valid price is entered
5. Food and price are added to the cart
6. Process repeats until user enters 'q'
7. Program displays all items with prices and total cost

### Example Run

```
Enter a food to buy (q to quit): Pizza
Enter the price of Pizza. (Should be numeric): Ksh 850
Enter a food to buy (q to quit): Soda
Enter the price of Soda. (Should be numeric): Ksh abc
Invalid price. Please enter a number.
Enter the price of Soda. (Should be numeric): Ksh 120
Enter a food to buy (q to quit): Fries
Enter the price of Fries. (Should be numeric): Ksh 250
Enter a food to buy (q to quit): q
-------YOUR CART-------
Pizza           850.0
Soda            120.0
Fries           250.0
Your total is: Ksh 1220.00
```

---

## Code Breakdown

### Complete Code

```python
# shopping cart program

from operator import index

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        while True:
            price = input(f"Enter the price of {food}. (Should be numeric): Ksh ")
            try:
                price = float(price)
                foods.append(food)
                prices.append(price)
                break
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue


print("-------YOUR CART-------")

for price in prices:
    total += price

for food in foods:
    for price in prices:
        if foods.index(food) == prices.index(price):
            print(f"{food:15} {price}")
print(f"Your total is: Ksh {total:.2f}")
```

### Step-by-Step Explanation

#### 1. Initialization

```python
from operator import index

foods = []
prices = []
total = 0
```

- **`foods`**: Empty list to store food item names
- **`prices`**: Empty list to store corresponding prices
- **`total`**: Variable to accumulate the total cost
- **Note**: The `from operator import index` is imported but not used in this code

#### 2. Main Input Loop

```python
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
```

- **Infinite loop**: Continues until user enters 'q'
- **`.lower()`**: Converts input to lowercase for case-insensitive quit command
- **`break`**: Exits the main loop when user is done shopping

#### 3. Nested Price Validation Loop

```python
else:
    while True:
        price = input(f"Enter the price of {food}. (Should be numeric): Ksh ")
        try:
            price = float(price)
            foods.append(food)
            prices.append(price)
            break
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue
```

**How it works:**
- **Inner while loop**: Keeps asking for price until valid input
- **`try-except`**: Catches non-numeric input
- **`float(price)`**: Attempts to convert input to decimal number
- **If successful**: Adds food and price to respective lists, breaks inner loop
- **If fails**: Catches `ValueError`, displays error message, continues asking

#### 4. Calculate Total

```python
for price in prices:
    total += price
```

- Loops through all prices
- Adds each price to the total
- Simple accumulation pattern

#### 5. Display Cart

```python
for food in foods:
    for price in prices:
        if foods.index(food) == prices.index(price):
            print(f"{food:15} {price}")
```

**How it works:**
- **Outer loop**: Iterates through foods
- **Inner loop**: Iterates through prices
- **Matching**: Uses `.index()` to match food with corresponding price
- **`{food:15}`**: Formats food name to 15 characters width for alignment
- **Result**: Displays each item with its price in a formatted way

#### 6. Display Total

```python
print(f"Your total is: Ksh {total:.2f}")
```

- **`{total:.2f}`**: Formats total to 2 decimal places
- Displays the final total cost

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python shopping_cart.py
   ```
3. Follow the prompts to add items to your cart
4. Enter 'q' when done to see your cart and total

---

## Key Concepts Learnt

### Working with Parallel Lists
- **Definition**: Two or more lists where items at the same index are related
- **Example**: `foods[0]` corresponds to `prices[0]`
- **Accessing**: Using `.index()` to find matching positions
- **Benefit**: Keeps related data synchronized

### Exception Handling (try-except)
- **Purpose**: Handles errors gracefully without crashing the program
- **`try` block**: Code that might cause an error
- **`except ValueError`**: Catches specific error when conversion fails
- **`continue`**: Restarts the loop after error
- **Use case**: Input validation for numeric data

### Nested While Loops
- **Outer loop**: Main program flow (adding items)
- **Inner loop**: Validation loop (ensuring valid price)
- **Breaking inner loop**: Exits validation when input is valid
- **Breaking outer loop**: Exits entire program when user quits

### Input Validation Patterns
- **Case-insensitive input**: Using `.lower()` for user commands
- **Type conversion**: Converting string input to float
- **Retry logic**: Keep asking until valid input received
- **User feedback**: Informing user why input was rejected

### List Operations
- **`.append()`**: Adding items to lists
- **`.index()`**: Finding position of item in list
- **Iteration**: Looping through lists with for loops
- **Accumulation**: Building up total by iterating through numbers

### String Formatting
- **F-strings**: Using `f"{variable}"` for dynamic strings
- **Width specification**: `{food:15}` for alignment
- **Decimal formatting**: `{total:.2f}` for currency display
- **Combining text and variables**: Creating formatted output

### Program Flow Control
- **Infinite loops**: Using `while True` for continuous operation
- **Breaking loops**: Exiting loops with `break`
- **Continuing loops**: Skipping to next iteration with `continue`
- **Conditional branching**: Using if-else for different actions

---

## Understanding the Matching Logic

### How Foods and Prices are Matched

```python
for food in foods:
    for price in prices:
        if foods.index(food) == prices.index(price):
            print(f"{food:15} {price}")
```

**Example with data:**
```python
foods = ["Pizza", "Soda", "Fries"]
prices = [850.0, 120.0, 250.0]
```

**Execution:**
1. Outer loop: `food = "Pizza"` (index 0)
   - Inner loop checks all prices
   - When `price = 850.0` (index 0): `0 == 0` → True → Print "Pizza 850.0"

2. Outer loop: `food = "Soda"` (index 1)
   - Inner loop checks all prices
   - When `price = 120.0` (index 1): `1 == 1` → True → Print "Soda 120.0"

3. Outer loop: `food = "Fries"` (index 2)
   - Inner loop checks all prices
   - When `price = 250.0` (index 2): `2 == 2` → True → Print "Fries 250.0"
