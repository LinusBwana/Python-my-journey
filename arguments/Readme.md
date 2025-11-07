# Python Function Arguments

This directory contains practice exercises for learning different types of function arguments in Python. These examples demonstrate positional arguments, default arguments, keyword arguments, *args, and **kwargs.

## Contents

1. [Types of Arguments](#types-of-arguments)
2. [Positional Arguments](#positional-arguments)
3. [Default Arguments](#default-arguments)
4. [Keyword Arguments](#keyword-arguments)
5. [Arbitrary Arguments (*args)](#arbitrary-arguments-args)
6. [Keyword Arbitrary Arguments (**kwargs)](#keyword-arbitrary-arguments-kwargs)
7. [Combining All Argument Types](#combining-all-argument-types)
8. [Key Concepts Learnt](#key-concepts-learnt)

---

## Types of Arguments

Python functions can accept different types of arguments. Understanding these types makes functions more flexible and powerful.

### Complete List of Argument Types

1. **Positional Arguments** - Arguments passed by position
2. **Default Arguments** - Arguments with default values
3. **Keyword Arguments** - Arguments passed with parameter names
4. **Arbitrary Arguments (*args)** - Variable number of positional arguments
5. **Keyword Arbitrary Arguments (**kwargs)** - Variable number of keyword arguments

### Order of Arguments

**CRITICAL:** When using all argument types together, they **must** follow this order:

```python
function(positional_args, *args, keyword_args, **kwargs)
```

**Example:**
```python
def my_function(pos1, pos2, *args, key1="default", **kwargs):
    pass

# Valid calls
my_function(1, 2)
my_function(1, 2, 3, 4, 5)
my_function(1, 2, 3, 4, key1="value")
my_function(1, 2, 3, 4, key1="value", extra="data")
```

---

## Positional Arguments

**Positional arguments** are the most basic type - arguments passed in order.

### Example

```python
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mr", "Linus", "Ogero")
# Output: Hello Mr Linus Ogero
```

**How it works:**
- Arguments matched by position
- Order matters: `hello("Hello", "Mr", "Linus", "Ogero")`
  - `greeting = "Hello"`
  - `title = "Mr"`
  - `first = "Linus"`
  - `last = "Ogero"`

**Requirements:**
- Must provide correct number of arguments
- Must be in correct order
- Cannot skip arguments

---

## Default Arguments

```python
# default arguments = a default value for certain parameters
# used when the argument is omitted
# makes the function more flexible, reduces # of arguments
```

**Default arguments** have predefined values that are used when the argument is omitted.

### Example 1: Price Calculator

```python
def net_price(list_price, discount=0, tax=0.05):
    print(list_price, discount, tax)
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))         # Uses default discount=0, tax=0.05
print(net_price(500, 0.1))    # Uses default tax=0.05
print(net_price(500, 0.1, 0)) # Overrides all defaults
```

**Output:**
```
500 0 0.05
525.0
500 0.1 0.05
472.5
500 0.1 0
450.0
```

**How it works:**
- `net_price(500)`: Uses `discount=0` and `tax=0.05` (defaults)
- `net_price(500, 0.1)`: Uses `tax=0.05` (default), provides `discount=0.1`
- `net_price(500, 0.1, 0)`: Overrides both defaults

### Example 2: Count Up Timer

```python
import time

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE")

count(30, 15)  # Counts from 15 to 30
count(10)      # Counts from 0 to 10 (uses default start=0)
```

**How it works:**
- `start=0` provides a default starting point
- Can be overridden by passing a value
- Makes function flexible for different use cases

**Benefits:**
- Fewer required arguments
- Backward compatibility
- Common values don't need to be specified

**Rules:**
- Default arguments must come after positional arguments
- Cannot have positional argument after default argument

```python
# Valid
def func(a, b, c=0, d=0):
    pass

# Invalid - will cause error
def func(a, b=0, c, d=0):
    pass
```

---

## Keyword Arguments

```python
# keyword arguments = an argument preceded by an identifier
# helps with readability
# order of arguments does not matter
```

**Keyword arguments** are passed using the parameter name, making order irrelevant.

### Example 1: Flexible Ordering

```python
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr", last="Ogero", first="Linus")
# Output: Hello Mr Linus Ogero
```

**How it works:**
- First argument is positional: `greeting="Hello"`
- Remaining arguments use keywords: order doesn't matter
- More readable, especially with many parameters

### Example 2: Built-in Keyword Arguments

```python
for x in range(1, 10):
    print(x, end=" ")  # end is a keyword argument
print()

print("1", "2", "3", "4", "5", sep="-")  # sep is a keyword argument
# Output: 1-2-3-4-5
```

**Common built-in keyword arguments:**
- `print()`: `end`, `sep`, `file`
- `open()`: `mode`, `encoding`
- `range()`: `start`, `stop`, `step`

### Example 3: Phone Number Formatter

```python
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country=254, area="711", first="618", last="688")
print(phone_number)
# Output: 254-711-618-688
```

**Benefits:**
- Self-documenting code
- Order independence
- Prevents errors from wrong order
- Easier to maintain

**Can mix positional and keyword:**
```python
hello("Hello", "Mr", last="Ogero", first="Linus")
# First two are positional, last two are keyword
```

**Rules:**
- Keyword arguments must come after positional arguments
- Cannot use same argument twice

```python
# Valid
func(1, 2, c=3, d=4)

# Invalid - positional after keyword
func(1, 2, c=3, 4)
```

---

## Arbitrary Arguments (*args)

```python
# arbitrary meaning varying amount of arguments
# *args = allows you to pass multiple non-key arguments
# *unpacking operator
```

***args** allows a function to accept any number of positional arguments.

### Example 1: Add Function

```python
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5, 6, 1))
# Output: 22
```

**How it works:**
- `*nums` collects all positional arguments into a tuple
- Can pass any number of arguments (0, 1, 2, 3, ...)
- Inside function, `nums` is a tuple

**Example calls:**
```python
add()              # nums = ()
add(1)             # nums = (1,)
add(1, 2)          # nums = (1, 2)
add(1, 2, 3, 4, 5) # nums = (1, 2, 3, 4, 5)
```

### Example 2: Display Name

```python
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Eng", "Linus", "Bwana", "EBK")
# Output: Eng Linus Bwana EBK
```

**How it works:**
- Accepts any number of name parts
- Flexible for different name formats
- `args` is a tuple, can iterate through it

**Key points:**
- `*args` creates a tuple of arguments
- Name `args` is convention (can use any name after *)
- Must come after regular positional arguments
- Can only have one `*args` in function definition

---

## Keyword Arbitrary Arguments (**kwargs)

```python
# **kwargs = allows you to pass multiple keyword-arguments
```

***kwargs** allows a function to accept any number of keyword arguments.

### Example: Print Address

```python
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:8}: {value}")

print_address(street="Clay City",
              city="Nairobi",
              state="Kasarani",
              zip="00618")
```

**Output:**
```
street  : Clay City
city    : Nairobi
state   : Kasarani
zip     : 00618
```

**How it works:**
- `**kwargs` collects all keyword arguments into a dictionary
- Can pass any number of keyword arguments
- Inside function, `kwargs` is a dictionary
- Key = parameter name, Value = argument value

**Example calls:**
```python
print_address()                          # kwargs = {}
print_address(city="NYC")               # kwargs = {"city": "NYC"}
print_address(city="NYC", zip="10001")  # kwargs = {"city": "NYC", "zip": "10001"}
```

**Key points:**
- `**kwargs` creates a dictionary of arguments
- Name `kwargs` is convention (can use any name after **)
- Keys are strings (parameter names)
- Must come after `*args` if both are used
- Can only have one `**kwargs` in function definition

---

## Combining All Argument Types

### Example: Shipping Label

```python
def shipping_label(*args, greeting="hi", **kwargs):
    print(greeting)
    
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "po_box" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('po_box')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('county')}")

shipping_label("Eng.", "Linus", "Bwana",
               greeting="Niaje",
               street="0618 Ruaraka.",
               po_box="PO BOX 264",
               city="Clay City",
               state="Kasarani",
               county="Nairobi")
```

**Output:**
```
Niaje
Eng. Linus Bwana 
0618 Ruaraka.
PO BOX 264
Clay City Kasarani, Nairobi
```

**How it works:**
1. **`*args`**: Collects "Eng.", "Linus", "Bwana" into tuple
2. **`greeting="hi"`**: Default argument (overridden by keyword argument)
3. **`**kwargs`**: Collects street, po_box, city, state, county into dictionary

**Order in function call:**
```python
shipping_label(
    # 1. Positional arguments (collected by *args)
    "Eng.", "Linus", "Bwana",
    
    # 2. Keyword argument (matches default parameter)
    greeting="Niaje",
    
    # 3. Keyword arguments (collected by **kwargs)
    street="0618 Ruaraka.",
    po_box="PO BOX 264",
    city="Clay City",
    state="Kasarani",
    county="Nairobi"
)
```

---

## How to Run

1. Navigate to the project directory
2. Run any Python file:
   ```bash
   python arguments_keyword_arguments.py
   python default_arguments.py
   python default_arguments_count_up_timer.py
   python arbitrary_arguments_args_kwargs_.py
   python args_kwargs_exercise.py
   ```

---

## Key Concepts Learnt

### Understanding Argument Types

**1. Positional Arguments**
- Basic argument type
- Order matters
- Must provide exact number required
- No default values

**2. Default Arguments**
- Have default values
- Optional to provide
- Make functions flexible
- Reduce number of required arguments

**3. Keyword Arguments**
- Include parameter name
- Order doesn't matter (among keyword args)
- Improve readability
- Prevent errors from wrong order

**4. Arbitrary Arguments (*args)**
- Accept varying number of positional arguments
- Creates tuple inside function
- Use `*` prefix
- Convention: name it `args`

**5. Keyword Arbitrary Arguments (**kwargs)**
- Accept varying number of keyword arguments
- Creates dictionary inside function
- Use `**` prefix
- Convention: name it `kwargs`

### Argument Order Rules

When combining argument types, follow this order:

```python
def function(
    positional,           # 1. Required positional arguments
    *args,                # 2. Arbitrary positional arguments
    default="value",      # 3. Default/keyword arguments
    **kwargs              # 4. Arbitrary keyword arguments
):
    pass
```

**Valid examples:**
```python
def func1(a, b):                           # Just positional
def func2(a, b, c=0):                      # Positional + default
def func3(a, *args):                        # Positional + *args
def func4(a, *args, b=0):                   # Positional + *args + default
def func5(a, *args, b=0, **kwargs):        # All types
def func6(a, b=0, **kwargs):               # Positional + default + **kwargs
```

**Invalid examples:**
```python
def func1(*args, a):           # Positional after *args
def func2(**kwargs, a):        # Any argument after **kwargs
def func3(a=0, b):             # Positional after default
def func4(**kwargs, *args):    # *args after **kwargs
```

### Using *args

**Characteristics:**
- Tuple inside function
- Can iterate through it
- Access by index: `args[0]`, `args[1]`
- Check length: `len(args)`
- Can be empty: `()`

**Common use cases:**
- Functions with variable inputs
- Mathematical operations (sum, average, etc.)
- Formatting multiple values
- Collecting multiple items

### Using **kwargs

**Characteristics:**
- Dictionary inside function
- Iterate with `.items()`, `.keys()`, `.values()`
- Access with `.get()` or `[]`
- Check keys with `in`
- Can be empty: `{}`

**Common use cases:**
- Optional configuration parameters
- Flexible function interfaces
- Passing data to other functions
- Building objects with variable attributes

### Unpacking Operator

The `*` and `**` operators can also unpack collections:

```python
# Unpacking list with *
numbers = [1, 2, 3, 4]
print(*numbers)  # Same as print(1, 2, 3, 4)

# Unpacking dictionary with **
data = {"name": "Alice", "age": 25}
def show_info(name, age):
    print(name, age)
show_info(**data)  # Same as show_info(name="Alice", age=25)
```

---

## Practical Examples

### Example: Flexible Calculator
```python
def calculate(operation, *numbers):
    if operation == "add":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == "average":
        return sum(numbers) / len(numbers)

print(calculate("add", 1, 2, 3, 4))         # 10
print(calculate("multiply", 2, 3, 4))       # 24
print(calculate("average", 10, 20, 30))     # 20.0
```

### Example: Logger Function
```python
def log_message(level, *messages, **metadata):
    print(f"[{level}]", end=" ")
    print(*messages)
    for key, value in metadata.items():
        print(f"  {key}: {value}")

log_message("INFO", "User logged in", 
            user="alice", 
            ip="192.168.1.1")
```

**Output:**
```
[INFO] User logged in
  user: alice
  ip: 192.168.1.1
```

### Example: Create User
```python
def create_user(username, email, *groups, is_admin=False, **extra_info):
    user = {
        "username": username,
        "email": email,
        "groups": groups,
        "is_admin": is_admin,
        "extra": extra_info
    }
    return user

user = create_user(
    "jdoe", 
    "jdoe@example.com",
    "developers", "testers",
    is_admin=True,
    department="IT",
    location="NYC"
)
print(user)
```

### Example: Build Query
```python
def build_query(table, *columns, **filters):
    if columns:
        cols = ", ".join(columns)
    else:
        cols = "*"
    
    query = f"SELECT {cols} FROM {table}"
    
    if filters:
        conditions = [f"{k}={v}" for k, v in filters.items()]
        query += " WHERE " + " AND ".join(conditions)
    
    return query

print(build_query("users"))
# SELECT * FROM users

print(build_query("users", "name", "email"))
# SELECT name, email FROM users

print(build_query("users", "name", "email", age=25, city="NYC"))
# SELECT name, email FROM users WHERE age=25 AND city=NYC
```

---

## Common Patterns

### Pattern 1: Wrapper Functions
```python
def my_print(*args, **kwargs):
    print("[LOG]", *args, **kwargs)

my_print("Hello", "World", sep="-")
# Output: [LOG] Hello-World
```

### Pattern 2: Extending Functions
```python
def super_sum(*args, start=0):
    total = start
    for num in args:
        total += num
    return total

print(super_sum(1, 2, 3))           # 6
print(super_sum(1, 2, 3, start=10)) # 16
```

### Pattern 3: Configuration Functions
```python
def configure_app(**settings):
    config = {
        "debug": False,
        "port": 8000,
        "host": "localhost"
    }
    config.update(settings)
    return config

app_config = configure_app(debug=True, port=5000)
```

### Pattern 4: Dynamic Object Creation
```python
def create_object(type_name, *values, **properties):
    obj = {
        "type": type_name,
        "values": values,
        "properties": properties
    }
    return obj

obj = create_object("Person", "Alice", 25, city="NYC", job="Engineer")
```

---

## Best Practices

### When to Use Each Type

**Positional:**
- Required, obvious arguments
- Small number of arguments (2-3)
- Arguments with clear order

**Default:**
- Optional parameters
- Common default values
- Configuration options

**Keyword:**
- Many parameters
- Optional parameters
- Improving readability

***args:**
- Variable number of similar items
- Unknown number of arguments
- List-like operations

****kwargs:**
- Optional configuration
- Flexible interfaces
- Passing to other functions

### Naming Conventions

```python
# Good - descriptive names
def process_data(*records, **options):
    pass

def send_email(*recipients, **settings):
    pass

# Standard - using conventions
def func(*args, **kwargs):
    pass
```

### Documentation

```python
def my_function(required, *args, optional="default", **kwargs):
    """
    Description of function.
    
    Args:
        required: Required positional argument
        *args: Variable positional arguments
        optional: Optional keyword argument (default: "default")
        **kwargs: Variable keyword arguments
    
    Returns:
        Description of return value
    """
    pass
```