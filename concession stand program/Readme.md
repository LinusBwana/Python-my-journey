# Python Concession Stand Program

This directory contains a practice project for building a concession stand ordering system. This example demonstrates how to use dictionaries, lists, loops, and input validation to create a functional food ordering application.

## Contents

1. [Program Overview](#program-overview)
2. [How the Program Works](#how-the-program-works)
3. [Code Breakdown](#code-breakdown)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## Program Overview

The **Concession Stand Program** allows users to:
- View a menu of food items with prices
- Select items to add to their cart
- Validate that selected items are available
- Calculate the total cost
- Display the order summary

**Features:**
- Interactive menu display
- Case-insensitive input
- Input validation
- Running total calculation
- Empty cart handling
- Price formatting in Kenyan Shillings (Ksh)

---

## How the Program Works

### User Interaction Flow

1. Program displays the menu with items and prices
2. User selects items by name (or 'q' to quit)
3. Program validates if item exists in menu
4. Valid items are added to cart
5. Invalid items prompt an error message
6. User continues ordering until entering 'q'
7. Program displays order summary with total cost
8. If cart is empty, program displays goodbye message

### Example Run

```
-----------MENU-----------
pizza     : Ksh3.00
nachos    : Ksh4.50
popcorn   : Ksh6.00
fries     : Ksh2.50
chips     : Ksh1.00
pretzel   : Ksh3.50
soda      : Ksh3.00
lemonade  : Ksh4.25
--------------------------
Select and item (q to quit): pizza
Select and item (q to quit): soda
Select and item (q to quit): burger
Not Available. Check the menu
Select and item (q to quit): fries
Select and item (q to quit): q
--------YOUR ORDER--------
pizza
soda
fries
Total amount: 8.50
--------------------------
```

---

## Code Breakdown

### Complete Code

```python
# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25,}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: Ksh{value:.2f}")
print("--------------------------")

while True:
    food = input("Select and item (q to quit): ").lower()

    if food == "q":
        break

    if food not in menu.keys():
        if food == "q":
            break
        else:
            print("Not Available. Check the menu")
            continue
    else:
        menu.get(food)
        cart.append(food)


if cart:
    print("--------YOUR ORDER--------")

    for food in cart:
        total += menu.get(food)
        print(food)

    print(f"Total amount: {total:.2f}")
    print("--------------------------")
else:
    print("--------------------------")
    print("You didn't order anything. Goodbye!")
    print("--------------------------")
```

### Step-by-Step Explanation

#### 1. Menu Setup

```python
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25,}
```

**Dictionary structure:**
- **Keys**: Food item names (strings)
- **Values**: Prices (floats)
- **Why dictionary?**: Fast lookup of prices by item name
- **Advantage**: Easy to add/remove items or update prices

#### 2. Initialize Variables

```python
cart = []
total = 0
```

- **`cart`**: Empty list to store ordered items (item names only)
- **`total`**: Accumulator for calculating total cost

#### 3. Display Menu

```python
print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: Ksh{value:.2f}")
print("--------------------------")
```

**How it works:**
- **Header**: Prints menu title
- **Loop**: Iterates through dictionary items
- **Formatting**: 
  - `{key:10}` - Left-aligns item name in 10-character width
  - `{value:.2f}` - Formats price to 2 decimal places
- **Footer**: Prints separator line

**Output format:**
```
pizza     : Ksh3.00
nachos    : Ksh4.50
```

#### 4. Order Input Loop

```python
while True:
    food = input("Select and item (q to quit): ").lower()

    if food == "q":
        break
```

**Main loop:**
- **Infinite loop**: Continues until user quits
- **`.lower()`**: Converts input to lowercase for case-insensitive comparison
- **Quit check**: Exits loop if user enters 'q'

#### 5. Input Validation

```python
if food not in menu.keys():
    if food == "q":
        break
    else:
        print("Not Available. Check the menu")
        continue
else:
    menu.get(food)
    cart.append(food)
```

**Validation logic:**
1. **Check if item exists**: `food not in menu.keys()`
2. **If item doesn't exist**:
   - Check if it's 'q' (quit command) → break
   - Otherwise → display error and continue loop
3. **If item exists**:
   - Get price from menu (not used, but demonstrates `.get()`)
   - Add item to cart

**Note:** The second `if food == "q"` check is redundant since the first check catches it, but provides extra safety.

#### 6. Display Order Summary

```python
if cart:
    print("--------YOUR ORDER--------")
    for food in cart:
        price = menu.get(food)
        total += price
        print(f"{food:10} Ksh{price:.2f}")

    print(f"Total amount: {total:.2f}")
    print("--------------------------")
```

**If cart has items:**
1. **Print header**: "YOUR ORDER"
2. **Loop through cart**:
   - Get price from menu using `.get(food)` and store in variable
   - Add price to total accumulator
   - Print item name and price in formatted columns
     - `{food:10}` - Left-aligns item name in 10-character width
     - `{price:.2f}` - Formats price to 2 decimal places
3. **Display total**: Formatted to 2 decimal places
4. **Print footer**: Separator line

**Output format:**
```
--------YOUR ORDER--------
pizza      Ksh3.00
soda       Ksh3.00
fries      Ksh2.50
Total amount: 8.50
--------------------------
```

#### 7. Handle Empty Cart

```python
else:
    print("--------------------------")
    print("You didn't order anything. Goodbye!")
    print("--------------------------")
```

**If cart is empty:**
- Display friendly goodbye message
- Prevents showing empty order

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python concession_stand_program.py
   ```
3. Browse the menu and enter item names
4. Enter 'q' when finished to see your order

---

## Key Concepts Learnt

### Working with Dictionaries
- **Menu storage**: Using dictionary for item-price mapping
- **Key lookup**: Checking if item exists with `in menu.keys()`
- **Value retrieval**: Getting prices with `.get(food)`
- **Iteration**: Using `.items()` to display menu
- **Fast access**: O(1) lookup time for prices

### List for Cart Management
- **Dynamic storage**: List grows as items are added
- **Appending**: Adding items with `.append()`
- **Allows duplicates**: User can order same item multiple times
- **Order preservation**: Items shown in order added

### Input Validation
- **Case handling**: Using `.lower()` for case-insensitive input
- **Membership testing**: Using `in` to check if item exists
- **Error feedback**: Informing user of invalid selections
- **Loop continuation**: Using `continue` to restart loop after error

### Program Flow Control
- **Infinite loop**: Using `while True` for continuous operation
- **Breaking loop**: Exiting with `break` when user quits
- **Conditional execution**: Using `if cart:` to handle empty cart
- **Continue statement**: Skipping to next iteration on error

### String Formatting
- **Width specification**: `{key:10}` for aligned output
- **Decimal precision**: `{value:.2f}` for currency
- **F-strings**: Dynamic string creation
- **Visual formatting**: Using separators for clarity

### Accumulation Pattern
- **Total calculation**: Running sum of prices
- **Loop accumulation**: Adding to total in each iteration
- **Formula**: `total += menu.get(food)`

### Boolean Context
- **Truthy/Falsy**: Empty list is falsy, non-empty is truthy
- **Conditional check**: `if cart:` checks if list has items
- **Simplifies logic**: No need for `if len(cart) > 0:`

---

## Understanding the Validation Flow

### Validation Decision Tree

```
User enters food item
        ↓
    .lower() applied
        ↓
    Is it "q"? ───YES──→ Break loop (quit)
        ↓ NO
    Is it in menu? ───NO──→ Show error, continue loop
        ↓ YES
    Add to cart
        ↓
    Ask for next item
```

### Why Two 'q' Checks?

```python
if food == "q":
    break

if food not in menu.keys():
    if food == "q":  # Redundant but safe
        break
```

**Explanation:**
- First check catches 'q' immediately
- Second check is redundant but provides safety net
- Could be simplified to just the first check

**Simplified version:**
```python
if food == "q":
    break
elif food not in menu.keys():
    print("Not Available. Check the menu")
    continue
else:
    cart.append(food)
```

## Dictionary vs List for Cart

### Why Not Store Prices in Cart?

**Current approach:**
```python
cart = ["pizza", "soda"]  # Store names only
price = menu.get(food)    # Look up price when needed
```

**Advantages of this approach:**
1. **Single source of truth**: Prices only in menu
2. **Easy updates**: Change price in menu, automatically reflected
3. **Memory efficient**: Store names only (smaller)
4. **Flexibility**: Can change menu prices mid-program

**When to store prices in cart:**
- Price might change during session
- Need to preserve price at time of order
- Working with promotional prices

---

## Understanding `.get()` vs Direct Access

### Using `.get()`

```python
price = menu.get("pizza")  # Returns 3.00
price = menu.get("burger")  # Returns None (no error)
```

### Using Direct Access

```python
price = menu["pizza"]   # Returns 3.00
price = menu["burger"]  # Raises KeyError
```

### Why `.get()` is Safer

- Returns `None` instead of crashing
- Can specify default: `menu.get("burger", 0.00)`
- Better for uncertain keys
- Used in this program for safety

---

## Data Flow Visualization

```
MENU (Dictionary)
┌─────────────────┐
│ pizza: 3.00     │
│ nachos: 4.50    │  ──┐
│ popcorn: 6.00   │    │
│ fries: 2.50     │    │ User selects "pizza"
│ chips: 1.00     │    │
│ pretzel: 3.50   │    │
│ soda: 3.00      │    │
│ lemonade: 4.25  │    │
└─────────────────┘    │
                       │
                       ↓
                  CART (List)
                  ┌─────────┐
                  │ pizza   │ ← Stores item name only
                  └─────────┘
                       │
                       ↓
              Display Order
              ┌──────────────────┐
              │ pizza            │
              │ Total: 3.00      │
              └──────────────────┘
                       ↑
                       │
            menu.get("pizza") → 3.00
```