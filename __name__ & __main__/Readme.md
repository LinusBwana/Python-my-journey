# Python __name__ and __main__

This directory contains practice exercises for learning the `__name__` and `__main__` special variables in Python. These examples demonstrate how to create modular, reusable scripts and how to import functions between modules.

## Contents

1. [What are __name__ and __main__?](#what-are-__name__-and-__main__)
2. [Why Use __name__ == '__main__'?](#why-use-__name__--__main__)
3. [Script Examples](#script-examples)
4. [Key Concepts Learnt](#key-concepts-learnt)

---

## What are __name__ and __main__?

```python
# __name__ & __main__: (This script can be imported or run standalone)
# functions and classes in this module can be reused without the main block of code executing
```

### Understanding __name__

**`__name__`** is a special built-in variable in Python that:
- Gets automatically set for every module
- Contains the name of the module
- Has different values depending on how the script is executed

**Two possible values:**
1. **`"__main__"`** - When script is run directly
2. **Module name** - When script is imported

**Example:**
```python
# my_script.py
print(__name__)

# If you run: python my_script.py
# Output: __main__

# If you import: import my_script
# Output: my_script
```

### The if __name__ == '__main__': Pattern

```python
def main():
    """Entry point for the script."""
    # Your program code here
    pass

if __name__ == '__main__':
    main()
```

**What this does:**
- Code inside the `if` block only runs when script is executed directly
- Code is **skipped** when script is imported as a module
- Allows functions to be reused without side effects

---

## Why Use __name__ == '__main__'?

### Good Practices

```python
# Good practice: - code is modular
#                  helps in readability
#                  leaves no global variables
#                  avoids unintended execution
# e.g library - import a library for functionality
#               when running a library directly, display the help page
```

**Benefits:**

1. **Modularity**: Code can be used as script or imported module
2. **Readability**: Clear separation between definitions and execution
3. **No global variables**: Code runs in function scope
4. **Avoids unintended execution**: Import doesn't run code automatically
5. **Reusability**: Functions can be imported without running the program

### Example Scenario

**Without `if __name__ == '__main__':`**
```python
# utils.py
def add(x, y):
    return x + y

print("Calculating...")
result = add(5, 3)
print(result)

# In another file:
import utils  # This will print "Calculating..." and "8"
```

**With `if __name__ == '__main__':`**
```python
# utils.py
def add(x, y):
    return x + y

if __name__ == '__main__':
    print("Calculating...")
    result = add(5, 3)
    print(result)

# In another file:
import utils  # Nothing is printed, only function is imported
utils.add(10, 5)  # Can use the function
```

---

## Script Examples

### Example: Basic Template

```python
def main():
    """Entry point for the script."""
    # Your program code here
    pass

if __name__ == '__main__':
    main()
```

**How it works:**
- Define a `main()` function containing program logic
- Use `if __name__ == '__main__':` guard to call `main()`
- When run directly: `main()` executes
- When imported: Only function definition is loaded

---

### Example: Script1 and Script2 (Cross-Import)

#### script1.py
```python
from script2 import *

def favourite_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("This is script1")
    favourite_food("Pizza")
    favourite_drink("lemonade")
    print("Bye")

if __name__ == '__main__':
    main()
```

#### script2.py
```python
from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script2")
    favourite_food("Chips")
    favourite_drink("coffee")
    print("Bye")

if __name__ == '__main__':
    main()
```

### How Cross-Import Works

**Running script1.py:**
```
This is script1
Your favourite food is Pizza
Your favourite drink is lemonade
Bye
```

**Running script2.py:**
```
This is script2
Your favourite food is Chips
Your favourite drink is coffee
Bye
```

**What happens:**

1. **When running script1.py:**
   - script1's `__name__` is `"__main__"`
   - Imports all from script2
   - script2's `__name__` is `"script2"` (not `"__main__"`)
   - script2's `main()` **doesn't execute** (guarded by `if __name__ == '__main__':`)
   - Only `favourite_drink()` function is imported
   - script1's `main()` executes

2. **When running script2.py:**
   - script2's `__name__` is `"__main__"`
   - Imports all from script1
   - script1's `__name__` is `"script1"` (not `"__main__"`)
   - script1's `main()` **doesn't execute** (guarded by `if __name__ == '__main__':`)
   - Only `favourite_food()` function is imported
   - script2's `main()` executes

**Key point:** The `if __name__ == '__main__':` guard prevents each script's main logic from running when imported, avoiding circular execution and duplicate output.

---

## How to Run

1. Navigate to the project directory
2. Run either script:
   ```bash
   python script1.py
   python script2.py
   ```
3. Observe that only the selected script's main function runs
4. Functions from the other script are available but its main doesn't execute

---

## Key Concepts Learnt

### Understanding __name__

- **Special variable**: Automatically set by Python
- **Two values**: `"__main__"` when run directly, module name when imported
- **Every module has it**: Available in all Python files
- **Used for control flow**: Determines if code should execute

### The Main Guard Pattern

**Structure:**
```python
if __name__ == '__main__':
    # Code here only runs when script is executed directly
    main()
```

**Purpose:**
- Separates module definition from execution
- Allows code to be imported without side effects
- Standard Python practice for scripts

### Module Import Behavior

**Without guard:**
```python
# module.py
print("This runs on import!")

def my_function():
    pass

# In another file:
import module  # Prints "This runs on import!"
```

**With guard:**
```python
# module.py
def my_function():
    pass

if __name__ == '__main__':
    print("This only runs when executed directly!")

# In another file:
import module  # Nothing is printed
```

### Code Organization Benefits

**1. Modularity**
- Functions can be reused in other scripts
- Clear separation of concerns
- Easier to test individual functions

**2. Readability**
- Clear entry point with `main()` function
- Easy to understand execution flow
- Standard pattern recognized by Python developers

**3. No Global Variables**
- Variables defined in `main()` are local
- Avoids namespace pollution
- Reduces naming conflicts

**4. Avoids Unintended Execution**
- Import doesn't trigger program execution
- Can test functions without running entire program
- Library code won't execute when imported

### Cross-Module Imports

**Pattern:**
- Multiple modules can import from each other
- Each module's `main()` is protected by `if __name__ == '__main__':`
- Only the directly executed script runs its `main()`
- Functions are shared without executing main logic

**Example structure:**
```python
# module_a.py
from module_b import helper_function

def main_function():
    helper_function()

if __name__ == '__main__':
    main_function()

# module_b.py
from module_a import main_function

def helper_function():
    print("Helper")

if __name__ == '__main__':
    helper_function()
    main_function()
```

---

## Practical Examples

### Example 1: Math Utilities

```python
# math_utils.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def main():
    """Demo of math utilities"""
    print("Math Utilities Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")

if __name__ == '__main__':
    main()

# In another file:
from math_utils import add, multiply
result = add(10, multiply(2, 5))
```

### Example 2: Configuration

```python
# config.py
DATABASE = "mydb"
HOST = "localhost"
PORT = 5432

def print_config():
    print(f"Database: {DATABASE}")
    print(f"Host: {HOST}")
    print(f"Port: {PORT}")

if __name__ == '__main__':
    # Show config when run directly
    print("Current Configuration:")
    print_config()

# In another file:
import config
print(config.DATABASE)  # Access configuration
```

### Example 3: Testing

```python
# calculator.py
def calculate(operation, x, y):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y

def main():
    # Test the calculator
    print("Testing calculator...")
    print(calculate("add", 5, 3))
    print(calculate("subtract", 10, 4))

if __name__ == '__main__':
    main()

# In test file:
from calculator import calculate
assert calculate("add", 2, 3) == 5
assert calculate("subtract", 10, 5) == 5
```

### Example 4: Library with Help

```python
# mylib.py
"""
A simple utility library
"""

def process_data(data):
    """Process and return data"""
    return data.upper()

def show_help():
    """Display library help"""
    print(__doc__)
    print("\nAvailable functions:")
    print("- process_data(data): Process input data")
    print("\nExample usage:")
    print("  from mylib import process_data")
    print("  result = process_data('hello')")

if __name__ == '__main__':
    # When run directly, show help
    show_help()

# When imported:
from mylib import process_data
result = process_data("hello")
```

---

## Common Patterns

### Pattern 1: CLI Script
```python
def parse_arguments():
    # Parse command line arguments
    pass

def main():
    args = parse_arguments()
    # Process based on arguments
    
if __name__ == '__main__':
    main()
```

### Pattern 2: Module with Examples
```python
def my_function():
    # Function implementation
    pass

if __name__ == '__main__':
    # Show examples when run directly
    print("Example usage:")
    my_function()
```

### Pattern 3: Test Runner
```python
def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("All tests passed!")

if __name__ == '__main__':
    test_add()
```

### Pattern 4: Configuration Display
```python
CONFIG = {
    "debug": True,
    "port": 8000
}

if __name__ == '__main__':
    print("Configuration:")
    for key, value in CONFIG.items():
        print(f"{key}: {value}")
```

---

## Understanding __name__ Values

### Direct Execution
```python
# my_script.py
print(f"__name__ is: {__name__}")

if __name__ == '__main__':
    print("Running as main program")
else:
    print("Being imported as module")
```

**Running: `python my_script.py`**
```
__name__ is: __main__
Running as main program
```

### Import as Module
```python
# another_script.py
import my_script
```

**Running: `python another_script.py`**
```
__name__ is: my_script
Being imported as module
```

---

## Best Practices

### Do's

1. **Always use the pattern** for scripts that might be imported
2. **Define a main() function** as the entry point
3. **Keep global scope clean** - put code in functions
4. **Use for organization** - separate definitions from execution
5. **Document the main() function** with docstring

### Don'ts

1. **Don't put complex logic** in global scope
2. **Don't rely on side effects** when importing
3. **Don't skip the guard** if script might be imported
4. **Don't use overly complex** main functions - delegate to other functions

### Template

```python
#!/usr/bin/env python3
"""
Module description here
"""

def function1():
    """Function 1 description"""
    pass

def function2():
    """Function 2 description"""
    pass

def main():
    """Main program entry point"""
    function1()
    function2()

if __name__ == '__main__':
    main()
```