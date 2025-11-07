# Python Variable Scope & Scope Resolution

This directory contains practice exercises for learning variable scope and scope resolution in Python. These examples demonstrate the LEGB rule and how Python looks up variable names.

## Contents

1. [What is Variable Scope?](#what-is-variable-scope)
2. [Scope Resolution - LEGB Rule](#scope-resolution---legb-rule)
3. [Local Scope](#local-scope)
4. [Enclosed Scope](#enclosed-scope)
5. [Global Scope](#global-scope)
6. [Built-in Scope](#built-in-scope)
7. [Key Concepts Learnt](#key-concepts-learnt)

---

## What is Variable Scope?

```python
# variable scope = where a variable is visible and accessible
```

**Variable scope** determines:
- Where a variable can be accessed
- How long a variable exists
- Which variable is used when names conflict

**Scope types in Python:**
1. **Local** - Inside a function
2. **Enclosed** - In enclosing functions (nested functions)
3. **Global** - At module level
4. **Built-in** - In Python's built-in namespace

---

## Scope Resolution - LEGB Rule

```python
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# Python scope resolution order - LEGB
```

**LEGB** is the order Python searches for variables:

1. **L**ocal - Current function
2. **E**nclosed - Enclosing function (if nested)
3. **G**lobal - Module level
4. **B**uilt-in - Python's built-in names

**How it works:**
- Python searches in this order: L → E → G → B
- Stops at first match
- Raises `NameError` if name not found in any scope

**Visual representation:**
```
Built-in Scope (Outermost)
    ↓
Global Scope
    ↓
Enclosed Scope (if nested)
    ↓
Local Scope (Innermost)
```

---

## Local Scope

```python
# Local Scope-------------------------------------------
def func1():
    a = 2  # a - is local in function 1. Function 1 cannot see b
    print(a)

def func2():
    b = 5  # b - is local in function 2. Function 2 cannot see a
    print(b)

func1()  # Output: 2
func2()  # Output: 5
```

**How it works:**
- **Local variables**: Created inside a function
- **Scope**: Only accessible within that function
- **Isolation**: `func1` cannot see `b`, `func2` cannot see `a`
- **Lifetime**: Exists only during function execution

**Attempting to access:**
```python
def func1():
    a = 2
    print(a)

func1()
print(a)  # NameError: name 'a' is not defined
```

**Key points:**
- Each function has its own local scope
- Variables are independent between functions
- Local variables "disappear" when function exits

---

## Enclosed Scope

```python
# Enclosed Scope-----------------------------------------
def func1():
    x = 2
    def func2():
        print(x)  # uses the x from the enclosed scope since there is no x in the local scope
    func2()

func1()  # Output: 2
```

**How it works:**
- **Nested function**: `func2` is inside `func1`
- **Enclosed variable**: `x` is in `func1`'s scope
- **Access**: `func2` can access `x` from enclosing function
- **Search order**: Looks in local first, then enclosed

**Scope hierarchy:**
```
func1 scope (x = 2)
    ↓
func2 scope (no local x, uses enclosed x)
```

**More complex example:**
```python
def outer():
    x = "outer"
    
    def middle():
        x = "middle"
        
        def inner():
            print(x)  # Uses "middle" from enclosed scope
        
        inner()
    
    middle()

outer()  # Output: middle
```

**With local variable:**
```python
def func1():
    x = 2
    
    def func2():
        x = 5  # Creates new local variable, doesn't modify func1's x
        print(x)  # Prints 5
    
    func2()
    print(x)  # Still prints 2

func1()
# Output:
# 5
# 2
```

---

## Global Scope

```python
# Global Scope-----------------------------------------
# Global meaning outside any function
def func1():
    print(x)

def func2():
    print(x)

x = 3
func1()  # Output: 3
func2()  # Output: 3
```

**How it works:**
- **Global variable**: `x` defined outside any function
- **Access**: Both functions can access `x`
- **Module-level**: Accessible throughout the file
- **Shared**: Same variable seen by all functions

**Modifying global variables:**
```python
x = 10

def modify():
    global x  # Declare we want to modify global x
    x = 20
    print(f"Inside function: {x}")

print(f"Before: {x}")  # 10
modify()                # Inside function: 20
print(f"After: {x}")    # 20
```

**Without global keyword:**
```python
x = 10

def modify():
    x = 20  # Creates new local variable
    print(f"Inside function: {x}")  # 20

print(f"Before: {x}")  # 10
modify()
print(f"After: {x}")   # Still 10 (global unchanged)
```

**Key points:**
- Global variables accessible in all functions
- Use `global` keyword to modify global variables
- Without `global`, assignment creates local variable
- Global variables exist for entire program lifetime

---

## Built-in Scope

```python
# Built-in Scope-----------------------------------------
from math import pi

def func1():
    print(pi)  # pi is built-in

func1()  # Output: 3.141592653589793
```

**How it works:**
- **Built-in names**: Provided by Python
- **Always available**: Don't need to define them
- **Examples**: `print()`, `len()`, `range()`, `int()`, `str()`
- **Constants**: Like `pi` from math module

**Common built-in names:**
```python
# Built-in functions
print(len([1, 2, 3]))      # len is built-in
print(max(1, 2, 3))        # max is built-in
print(sum([1, 2, 3]))      # sum is built-in

# Built-in types
x = int("5")               # int is built-in
y = str(123)               # str is built-in
z = list((1, 2, 3))        # list is built-in

# Built-in constants
print(True)                # True is built-in
print(False)               # False is built-in
print(None)                # None is built-in
```

**Shadowing built-ins (not recommended):**
```python
# Don't do this!
len = 5
print(len)  # 5 (now a variable)
# print(len([1, 2, 3]))  # TypeError: 'int' object is not callable

# Built-in is shadowed, can't use len() function anymore
```

**Key points:**
- Outermost scope in LEGB
- Contains Python's built-in functions and constants
- Always accessible unless shadowed
- Don't name variables after built-ins

---

## How to Run

1. Navigate to the project directory
2. Run the Python file:
   ```bash
   python variable_scope_and_scope_resolution.py
   ```

---

## Key Concepts Learnt

### Variable Scope

**Definition:**
- Where a variable is visible and accessible
- Determines variable lifetime
- Controls access to variables

**Scope types:**
1. **Local**: Inside function
2. **Enclosed**: In enclosing function
3. **Global**: Module level
4. **Built-in**: Python's built-in namespace

### LEGB Rule

**Search order:**
```
Local → Enclosed → Global → Built-in
```

**How Python finds variables:**
1. Check local scope first
2. If not found, check enclosed scope
3. If not found, check global scope
4. If not found, check built-in scope
5. If still not found, raise `NameError`

**Example:**
```python
x = "global"

def outer():
    x = "enclosed"
    
    def inner():
        x = "local"
        print(x)  # Finds in local scope, stops searching
    
    inner()

outer()  # Output: local
```

### Local Scope

**Characteristics:**
- Variables defined inside function
- Only accessible within that function
- Created when function called
- Destroyed when function returns
- Independent between functions

**Use cases:**
- Function parameters
- Variables inside functions
- Loop variables in functions

### Enclosed Scope

**Characteristics:**
- Variables in outer function of nested functions
- Accessible to inner functions
- Created when outer function called
- Survives across inner function calls

**Use cases:**
- Closures
- Factory functions
- Decorators
- Nested helper functions

### Global Scope

**Characteristics:**
- Variables defined at module level
- Accessible throughout module
- Exist for program lifetime
- Shared across all functions

**Modifying globals:**
- Use `global` keyword to modify
- Without `global`, creates local variable
- Best practice: avoid modifying globals

### Built-in Scope

**Characteristics:**
- Python's pre-defined names
- Always available
- Outermost scope
- Should not be shadowed

**Common built-ins:**
- Functions: `print`, `len`, `input`, `range`
- Types: `int`, `str`, `list`, `dict`
- Constants: `True`, `False`, `None`

---

## LEGB Examples

### Example 1: All Four Scopes

```python
# Built-in: len
# Global: x
x = "global"

def outer():
    # Enclosed: y
    y = "enclosed"
    
    def inner():
        # Local: z
        z = "local"
        print(f"Local: {z}")
        print(f"Enclosed: {y}")
        print(f"Global: {x}")
        print(f"Built-in: {len([1, 2, 3])}")
    
    inner()

outer()
```

**Output:**
```
Local: local
Enclosed: enclosed
Global: global
Built-in: 3
```

### Example 2: Variable Shadowing

```python
x = "global"

def func():
    x = "local"  # Shadows global x
    print(x)     # Uses local x

func()      # Output: local
print(x)    # Output: global (global unchanged)
```

### Example 3: Nested Shadowing

```python
x = "global"

def outer():
    x = "enclosed"
    
    def inner():
        x = "local"
        print(f"Inner sees: {x}")
    
    inner()
    print(f"Outer sees: {x}")

outer()
print(f"Global is: {x}")
```

**Output:**
```
Inner sees: local
Outer sees: enclosed
Global is: global
```

---

## Modifying Variables Across Scopes

### Using global Keyword

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)  # 2
```

### Using nonlocal Keyword

```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # Refers to count in outer()
        count += 1
    
    inner()
    inner()
    print(count)  # 2

outer()
```

**Difference:**
- **`global`**: Refers to module-level variable
- **`nonlocal`**: Refers to variable in enclosing function

### Without Keywords

```python
# Creates new local variable
def outer():
    x = 10
    
    def inner():
        x = 20  # New local variable in inner
        print(f"Inner: {x}")  # 20
    
    inner()
    print(f"Outer: {x}")  # Still 10

outer()
```

---

## Common Pitfalls

### Pitfall 1: Unintended Local Variable

```python
x = 10

def func():
    print(x)  # Intend to print global x
    x = 20    # But this makes x local throughout function

func()  # UnboundLocalError: local variable 'x' referenced before assignment
```

**Solution:**
```python
x = 10

def func():
    global x
    print(x)  # Now refers to global x
    x = 20

func()
```

### Pitfall 2: Loop Variables

```python
x = 5

def func():
    for x in range(3):  # x becomes local
        print(x)
    # x is still local here, not global

func()
print(x)  # Still 5 (global unchanged)
```

### Pitfall 3: Shadowing Built-ins

```python
# Don't do this
list = [1, 2, 3]
print(list)  # [1, 2, 3]
# list([4, 5, 6])  # TypeError: 'list' object is not callable

# Fix: use different name
my_list = [1, 2, 3]
```

---

## Practical Examples

### Example: Counter with Closure

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### Example: Configuration

```python
# Global configuration
DEBUG = True
MAX_RETRIES = 3

def log(message):
    if DEBUG:
        print(f"[DEBUG] {message}")

def retry_operation():
    for attempt in range(MAX_RETRIES):
        log(f"Attempt {attempt + 1}")
        # perform operation

log("Starting program")
retry_operation()
```

### Example: Temperature Converter

```python
from math import pi

FAHRENHEIT_OFFSET = 32
FAHRENHEIT_SCALE = 9/5

def celsius_to_fahrenheit(celsius):
    # Uses global constants
    return celsius * FAHRENHEIT_SCALE + FAHRENHEIT_OFFSET

def circle_area(radius):
    # Uses built-in pi
    return pi * radius ** 2

print(celsius_to_fahrenheit(25))
print(circle_area(5))
```

---

## Best Practices

### Do's

1. **Minimize global variables** - use function parameters instead
2. **Use descriptive names** - avoid shadowing built-ins
3. **Keep scope small** - define variables in smallest scope needed
4. **Use `global` sparingly** - prefer return values
5. **Document scope changes** - comment when using `global` or `nonlocal`

### Don'ts

1. **Don't shadow built-ins** - avoid names like `list`, `str`, `dict`
2. **Don't modify globals unnecessarily** - makes code harder to test
3. **Don't use same name in different scopes** - causes confusion
4. **Don't rely on mutable defaults** - can cause scope issues
5. **Don't create overly nested functions** - makes scoping complex

### Preferred Pattern

```python
# Good: Use parameters and return values
def process_data(data, config):
    result = data * config
    return result

# Avoid: Relying on globals
data = 10
config = 2

def process_data():
    global data
    data = data * config
    return data
```

---

## Scope Visualization

### Simple Function
```
Built-in (print, len, etc.)
    ↓
Global (module variables)
    ↓
Local (function variables)
```

### Nested Functions
```
Built-in (print, len, etc.)
    ↓
Global (module variables)
    ↓
Outer function (enclosed variables)
    ↓
Inner function (local variables)
```

### Multiple Nested Functions
```
Built-in
    ↓
Global
    ↓
Level 1 function (enclosed for Level 2)
    ↓
Level 2 function (enclosed for Level 3)
    ↓
Level 3 function (local)
```