# Python Format Specifiers Practice

This directory contains practice exercises for learning format specifiers in Python. These examples demonstrate how to control the appearance and formatting of values in f-strings.

## Contents

1. [What are Format Specifiers?](#what-are-format-specifiers)
2. [Format Specifier Syntax](#format-specifier-syntax)
3. [Practice Example](#practice-example)
4. [Format Specifiers Explained](#format-specifiers-explained)
5. [Key Concepts Learnt](#key-concepts-learnt)

---

## Defination For Format Specifiers

**Format specifiers** are special codes used within f-strings to control how values are displayed. They allow you to:

- Round numbers to specific decimal places
- Allocate a specific amount of space for values
- Align text (left, right, or center)
- Add padding with zeros or spaces
- Include signs for positive/negative numbers
- Add comma separators for thousands

The syntax is `{value:flags}`, where flags determine how the value should be formatted.

---

## Format Specifier Syntax

```python
{value:flags}
```

**Common flags:**
- `.(number)f` - Round to that many decimal places (fixed point)
- `:(number)` - Allocate that many spaces
- `:03` - Allocate and zero pad that many spaces
- `:<` - Left justify
- `:>` - Right justify
- `:^` - Center justify
- `:+` - Use a plus sign to indicate positive value
- `:=` - Place a sign to leftmost position
- `: ` - Insert a space before positive numbers
- `:,` - Comma separator

---

## Practice Example

```python
# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 13366.563336
price2 = -73355.25266
price3 = 3242.33536

print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")

print(f"Price 1 is ${price1:12}")
print(f"Price 2 is ${price2:12}")
print(f"Price 3 is ${price3:12}")

print(f"Price 1 is ${price1:012}")
print(f"Price 2 is ${price2:012}")
print(f"Price 3 is ${price3:012}")

print(f"Price 1 is ${price1:<012}")
print(f"Price 2 is ${price2:<012}")
print(f"Price 3 is ${price3:>012}")

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
```

---

## Format Specifiers Explained

### Decimal Places (`.f`)

Rounds numbers to a specific number of decimal places.

| Code | Output | Explanation |
|------|--------|-------------|
| `f"{price1:.1f}"` | `13366.6` | Rounds to 1 decimal place |
| `f"{price2:.1f}"` | `-73355.3` | Rounds to 1 decimal place |
| `f"{price3:.1f}"` | `3242.3` | Rounds to 1 decimal place |

**Example:**
```python
print(f"Price 1 is ${price1:.1f}")  # Price 1 is $13366.6
```

---

### Width Allocation (`:number`)

Allocates a specific number of spaces for the value (right-aligned by default).

| Code | Output | Explanation |
|------|--------|-------------|
| `f"{price1:12}"` | `  13366.563336` | Allocates 12 spaces, right-aligned |
| `f"{price2:12}"` | ` -73355.25266` | Allocates 12 spaces, right-aligned |
| `f"{price3:12}"` | `   3242.33536` | Allocates 12 spaces, right-aligned |

**Example:**
```python
print(f"Price 1 is ${price1:12}")  # Price 1 is $  13366.563336
```

---

### Zero Padding (`:0number`)

Allocates spaces and fills empty spaces with zeros.

| Code | Output | Explanation |
|------|--------|-------------|
| `f"{price1:012}"` | `013366.563336` | 12 spaces with zero padding |
| `f"{price2:012}"` | `-73355.25266` | 12 spaces with zero padding |
| `f"{price3:012}"` | `003242.33536` | 12 spaces with zero padding |

**Example:**
```python
print(f"Price 1 is ${price1:012}")  # Price 1 is $013366.563336
```

---

### Text Alignment

Controls how the value is aligned within the allocated space.

| Flag | Alignment | Example Code | Example Output |
|------|-----------|--------------|----------------|
| `:<` | Left | `f"{price1:<012}"` | `13366.563336` (left-aligned) |
| `:>` | Right | `f"{price3:>012}"` | `003242.33536` (right-aligned) |
| `:^` | Center | `f"{price1:^20}"` | `   13366.563336    ` |

**Example:**
```python
print(f"Price 1 is ${price1:<012}")  # Left-aligned
print(f"Price 3 is ${price3:>012}")  # Right-aligned
```

---

### Sign and Comma Separators (`:+,`)

Displays the sign for both positive and negative numbers and adds comma separators.

| Code | Output | Explanation |
|------|--------|-------------|
| `f"{price1:+,.2f}"` | `+13,366.56` | Plus sign, comma separator, 2 decimals |
| `f"{price2:+,.2f}"` | `-73,355.25` | Plus/minus sign, comma separator, 2 decimals |
| `f"{price3:+,.2f}"` | `+3,242.34` | Plus sign, comma separator, 2 decimals |

**Example:**
```python
print(f"Price 1 is ${price1:+,.2f}")  # Price 1 is $+13,366.56
print(f"Price 2 is ${price2:+,.2f}")  # Price 2 is $-73,355.25
print(f"Price 3 is ${price3:+,.2f}")  # Price 3 is $+3,242.34
```

---

## Common Format Specifier Combinations

### Currency Formatting
```python
price = 1234.567
print(f"${price:,.2f}")  # $1,234.57
```

### Percentage Formatting
```python
percentage = 0.8567
print(f"{percentage:.1%}")  # 85.7%
```

### Padding with Alignment
```python
name = "Python"
print(f"|{name:>10}|")  # |    Python|
print(f"|{name:<10}|")  # |Python    |
print(f"|{name:^10}|")  # |  Python  |
```

### Scientific Notation
```python
large_num = 1234567890
print(f"{large_num:.2e}")  # 1.23e+09
```

---

## How to Run

1. Clone this repository
2. Navigate to the project directory
3. Run the Python file:
   ```bash
   python format_specifiers.py
   ```

---

## Key Concepts Learnt

- **Format specifier syntax**: `{value:flags}`
- **Decimal precision**: Using `.nf` to control decimal places
- **Width allocation**: Using `:number` to reserve space
- **Zero padding**: Using `:0number` to pad with zeros
- **Text alignment**: 
  - `:<` for left alignment
  - `:>` for right alignment
  - `:^` for center alignment
- **Sign display**: Using `:+` to show positive/negative signs
- **Comma separators**: Using `:,` for thousands separators
- **Combining flags**: Mixing multiple format specifiers like `:+,.2f`
- **Practical applications**: Currency formatting, data alignment, report generation

---

## Quick Reference

```python
value = 1234.56789

f"{value:.2f}"      # 1234.57 (2 decimal places)
f"{value:10.2f}"    # "   1234.57" (width 10, 2 decimals)
f"{value:010.2f}"   # "0001234.57" (zero-padded)
f"{value:<10.2f}"   # "1234.57   " (left-aligned)
f"{value:>10.2f}"   # "   1234.57" (right-aligned)
f"{value:^10.2f}"   # " 1234.57  " (center-aligned)
f"{value:+.2f}"     # "+1234.57" (show sign)
f"{value:,.2f}"     # "1,234.57" (comma separator)
f"{value:+,.2f}"    # "+1,234.57" (sign + comma)
```

---