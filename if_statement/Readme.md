# Python If Statements Practice

This repository contains practice exercises for learning if statements in Python. These examples demonstrate basic conditional logic, logical operators, and practical applications.

## Contents

1. [Basic If Statement](#basic-if-statement)
2. [Temperature Converter](#temperature-converter)
3. [Weight Converter](#weight-converter)
4. [Arithmetic Calculator](#arithmetic-calculator)
5. [Logical Operators](#logical-operators)

---

## Basic If Statement

A simple example demonstrating basic if-else logic with user input.

```python
response = str(input("Do you like food? (Y/N) ").upper())

if response == "Y":
    print("The order is on the way")
elif response == "N":
    print("Ohh, you are full")
else:
    print("Wrong input")
```

---

## Temperature Converter

Converts temperature between Celsius and Fahrenheit.

```python
temp = float(input("Enter the Temperature: "))
unit = input("Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    temp = round((temp * (9/5)) + 32, 1)
    unit = "°K."
    print(f"The temperature is {round(temp, 1)}{unit}")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    unit = "°C"
    print(f"The temperature is {round(temp, 1)}{unit}")
else:
    print(f"{unit} was not a valid input")
```

---

## Weight Converter

Converts weight between Kilograms and Pounds.

```python
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or P): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not a valid")
```

---

## Arithmetic Calculator

A basic calculator that performs arithmetic operations based on user input.

```python
num1 = float(input("The the 1st number: "))
num2 = float(input("The the 2nd number: "))
operator = input("Choose an operator (+ - * /): ")

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 - num2
    print(round(result, 2))
elif operator == "/":
    result = num1 - num2
    print(round(result, 2))
else:
    print(f"The operator {operator} is invalid")
```

---

## Logical Operators

Demonstrates the use of logical operators (`and`, `or`, `not`) to evaluate multiple conditions.

```python
# logical operators = Allows us to evaluate multiple conditions (or, not, and)

is_sunny = False
temp = 20

if temp >= 28 and is_sunny:
    print("It is HOT outside🔥")
    print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 😊")
    print("It is SUNNY ☀️")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside🔥")
    print("It is CLOUDY ☁️️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁️️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 😊")
    print("It is CLOUDY ☁️️")
```

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run any Python file:
   ```bash
   python filename.py
   ```

## Key Concepts Learned

- Basic if-elif-else statements
- User input handling with `input()`
- Type conversion with `float()` and `str()`
- String methods like `.upper()`
- Logical operators (`and`, `or`, `not`)
- F-strings for formatted output
- Rounding numbers with `round()`

---