# Python Object-Oriented Programming (OOP)

This directory contains comprehensive practice exercises for learning Object-Oriented Programming in Python. The concepts are organized in a logical learning order from basic to advanced.

## Contents

1. [Introduction to OOP](#introduction-to-oop)
2. [Classes and Objects](#classes-and-objects)
3. [Class Variables](#class-variables)
4. [Static Methods](#static-methods)
5. [Class Methods](#class-methods)
6. [Magic Methods](#magic-methods)
7. [Inheritance](#inheritance)
8. [The super() Function](#the-super-function)
9. [Multiple and Multilevel Inheritance](#multiple-and-multilevel-inheritance)
10. [Polymorphism](#polymorphism)
11. [Key Concepts Learnt](#key-concepts-learnt)

---

## Introduction to OOP

### What is Object-Oriented Programming?

```python
# object = a bundle of related attributes (variables) and methods (functions). An instance of a class
#          attributes describe what the object has. Are variables that an object has
#          methods are functions that belong to an object. They define what an object can do.
#          e.g phone, cup, book
#          You need a "class" to create many objects

# class = A blueprint used to design the structure and layout of an object
```

**Key terminology:**
- **Object**: An instance of a class with specific data
- **Class**: A blueprint for creating objects
- **Attributes**: Variables that describe what an object has
- **Methods**: Functions that define what an object can do

**Real-world analogy:**
- **Class**: Car blueprint
- **Objects**: Specific cars (Mazda, BMW, Crown)
- **Attributes**: Model, year, color, for_sale
- **Methods**: drive(), stop(), describe()

---

## Classes and Objects

### Creating a Class

**oop_car.py:**
```python
class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.colour} {self.model}")

    def stop(self):
        print(f"You stop the {self.colour} {self.model}")

    def describe(self):
        return f"{self.year} {self.colour} {self.model}"
```

### Creating and Using Objects

**object_oriented_programming.py:**
```python
from oop_car import Car

car1 = Car("Mazda", "2024", "Red", False)
car2 = Car("BMW", "2022", "Black", False)
car3 = Car("Crown", "2020", "Blue", True)

# Accessing attributes
print(car1.model)   # Mazda
print(car1.year)    # 2024
print(car1.colour)  # Red
print(car1.for_sale) # False

# Calling methods
car1.drive()        # You drive the Red Mazda
car1.stop()         # You stop the Red Mazda
print(car2.describe())  # 2022 Black BMW
```

### Key Components

**1. The `__init__` Method (Constructor)**
- Automatically called when object is created
- Initializes object attributes
- `self` represents the instance being created

**2. Instance Attributes**
- Unique to each object
- Defined in `__init__` using `self`
- Accessed using dot notation: `object.attribute`

**3. Instance Methods**
- Functions that belong to objects
- First parameter is always `self`
- Can access and modify object attributes

---

## Class Variables

```python
# class variables = shared among all instances of a class (objects)
#                   Defined outside the constructor but instance variables (objects) are defined inside the constructor
#                   Allow you to share data among all objects created from that class
```

### Example: Student Class

```python
class Student:
    class_year = 2024      # Class variable - shared by all objects
    num_students = 0       # Class variable - tracks total students

    def __init__(self, name, age):
        self.name = name   # Instance variable - unique to each object
        self.age = age     # Instance variable - unique to each object
        Student.num_students += 1  # Update class variable

student1 = Student("Linus", 29)
student2 = Student("Philip", 30)
student3 = Student("Dan", 25)
student4 = Student("Sandra", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students}")
# Output: My graduating class of 2024 has 4

print(f"{student1.name} is {student1.age} years old")
# Output: Linus is 29 years old

# Access class variables through class name (best practice)
print(Student.class_year)      # 2024
print(Student.num_students)    # 4
```

### Class vs Instance Variables

| Aspect | Class Variables | Instance Variables |
|--------|----------------|-------------------|
| **Definition** | Outside `__init__` | Inside `__init__` with `self` |
| **Scope** | Shared by all objects | Unique to each object |
| **Access** | `ClassName.variable` | `object.variable` |
| **Use case** | Data common to all instances | Data specific to each instance |

**Best practice:** Access class variables using the class name (`Student.class_year`) rather than through objects for clarity.

---

## Static Methods

```python
# static methods - a method that belongs to a class rather than any object from that class (instance)
#                  usually used for general utility functions
# instance methods - best for operations on instances of the class (objects)
# static methods - best for utility functions that do not need access to class data
```

### Example: Employee Validation

```python
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method - operates on object data
    def get_info(self):
        return f"{self.name} = {self.position}"

    # Static method - utility function
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Linus", "Cashier")

# Call instance method on object
print(employee1.get_info())  # Eugene = Manager
print(employee2.get_info())  # Linus = Cashier

# Call static method on class (no object needed)
print(Employee.is_valid_position("Cook"))     # True
print(Employee.is_valid_position("Doctor"))   # False
```

### When to Use Static Methods

- Utility functions that don't need object data
- Validation functions
- Helper functions related to the class
- Functions that don't modify class or instance state

**Key difference:**
- **Instance method**: Requires object → `employee1.get_info()`
- **Static method**: Called on class → `Employee.is_valid_position()`

---

## Class Methods

```python
# class methods = allow operations related to the class itself
# Take (cls) as the first parameter, which represents the class itself
```

### Comparison of Method Types

```python
# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to the class data
# Class methods = Best for class-level data or require access to the class itself
```

### Example: Student Statistics

```python
class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # Class method - operates on class data
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    # Class method - uses class data
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {(cls.total_gpa / cls.count):.2f}"

student1 = Student("Linus", 4.8)
student2 = Student("Sandra", 4.1)
student3 = Student("Cate", 3.8)

# Call class methods on class
print(Student.get_count())         # Total # of students: 3
print(Student.get_average_gpa())   # Average gpa: 4.23
```

### Method Types Summary

| Method Type | Decorator | First Parameter | Access To | Use Case |
|------------|-----------|-----------------|-----------|----------|
| Instance | None | `self` | Instance data | Object operations |
| Static | `@staticmethod` | None | Nothing | Utility functions |
| Class | `@classmethod` | `cls` | Class data | Class-level operations |

---

## Magic Methods

```python
# magic methods - Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behaviour of objects
```

### Common Magic Methods

```python
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # String representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Equality comparison
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # Less than comparison
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # Addition
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # Contains (in operator)
    def __contains__(self, keyword):
        return keyword in self.title.lower() or keyword in self.author

    # Item access (indexing)
    def __getitem__(self, key):
        if key == 'Title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key {key} was not found"

book1 = Book("Utengano", "J. R. R", 310)
book2 = Book("The Sun Goes Down", "Wa Thiongo", 650)
book3 = Book("The River Between", "Wala bin Wala", 150)
book4 = Book("Utengano", "J. R. R", 980)

# Using magic methods
print(book3)                    # The River Between by Wala bin Wala (__str__)
print(book1 == book4)           # True (__eq__)
print(book1 < book4)            # True (__lt__)
print(book1 + book4)            # 1290 pages (__add__)
print("river" in book3)         # True (__contains__)
print(book1['Title'])           # Utengano (__getitem__)
print(book3['author'])          # Wala bin Wala
```

### Magic Methods Reference

| Method | Operator/Function | Purpose |
|--------|------------------|---------|
| `__init__` | Constructor | Initialize object |
| `__str__` | `str()`, `print()` | String representation |
| `__repr__` | `repr()` | Official representation |
| `__eq__` | `==` | Equality comparison |
| `__ne__` | `!=` | Not equal comparison |
| `__lt__` | `<` | Less than |
| `__le__` | `<=` | Less than or equal |
| `__gt__` | `>` | Greater than |
| `__ge__` | `>=` | Greater than or equal |
| `__add__` | `+` | Addition |
| `__sub__` | `-` | Subtraction |
| `__mul__` | `*` | Multiplication |
| `__truediv__` | `/` | Division |
| `__len__` | `len()` | Length |
| `__contains__` | `in` | Membership test |
| `__getitem__` | `[]` | Index access |

---

## Inheritance

```python
# inheritance - Allows you to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)
```

### Example: Animal Hierarchy

```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEAK")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# Inherited attributes
print(dog.name)       # Scooby
print(dog.is_alive)   # True

# Inherited methods
dog.eat()            # Scooby is eating
cat.sleep()          # Garfield is sleeping
mouse.sleep()        # Mickey is sleeping

# Child-specific methods
dog.speak()          # WOOF
cat.speak()          # MEOW
mouse.speak()        # SQUEAK
```

### Inheritance Benefits

1. **Code reusability**: Don't repeat common code
2. **Extensibility**: Add new features to existing classes
3. **Hierarchy**: Organize related classes
4. **Maintenance**: Update parent class affects all children

---

## The super() Function

```python
# super() - Function used in a child class (subclass) to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods
```

### Example: Shape Hierarchy

```python
class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)  # Call parent constructor
        self.radius = radius

    def describe(self):
        super().describe()  # Call parent method
        print(f"It is circle of area of {3.14 * int(self.radius) ** 2:.1f}cm^2")

class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is square of area {int(self.width) ** 2:.1f}cm^2")

class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is triangle of area {0.5 * int(self.width) * int(self.height):.1f}cm^2")

circle = Circle(colour="Red", is_filled=False, radius="4")
square = Square(colour="Black", is_filled=True, width="5")
triangle = Triangle(colour="Blue", is_filled=True, width="7", height="8")

circle.describe()
# Output:
# It is Red and not filled
# It is circle of area of 50.2cm^2

square.describe()
# Output:
# It is Black and filled
# It is square of area 25.0cm^2
```

### Two Ways to Call Parent Methods

```python
# Method 1: Using super()
super().__init__(colour, is_filled)

# Method 2: Using parent class name
Shape.__init__(self, colour, is_filled)
```

**Recommended:** Use `super()` as it's more maintainable and works better with multiple inheritance.

---

## Multiple and Multilevel Inheritance

### Multiple Inheritance

```python
# multiple inheritance = inherit from more than one parent class
#                        C(A, B)
```

### Multilevel Inheritance

```python
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
```

### Example: Animal Hierarchy

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")

# Multilevel: Prey inherits from Animal
class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

# Multilevel: Predator inherits from Animal
class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

# Multilevel: Rabbit inherits from Prey (which inherits from Animal)
class Rabbit(Prey):
    pass

# Multilevel: Hawk inherits from Predator (which inherits from Animal)
class Hawk(Predator):
    pass

# Multiple: Fish inherits from both Prey and Predator
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Kasuku")
fish = Fish("Tilapia")

rabbit.eat()     # From Animal
rabbit.flee()    # From Prey

fish.flee()      # From Prey
fish.hunt()      # From Predator
fish.sleep()     # From Animal
```

### Inheritance Hierarchy

```
                Animal
                /    \
            Prey    Predator
            /  \      /  \
        Rabbit  Fish  Hawk
```

**Key points:**
- **Multilevel**: Rabbit → Prey → Animal (chain)
- **Multiple**: Fish inherits from both Prey and Predator
- Fish has access to methods from all three classes

---

## Polymorphism

```python
# Polymorphism - Greek word that means to "Have many forms or faces"
# poly - Many
# Morphe - Form

# Two ways of achieving Polymorphism:
# 1. Inheritance - an object could be treated of the same type as the parent class
# 2. "Duck Typing" - Object must have necessary attributes/methods
```

### Method 1: Polymorphism Through Inheritance

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

# Polymorphism in action - same method name, different behaviors
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("BBQ", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")
# Output:
# 50.24cm²
# 25cm²
# 21.0cm²
# 706.5cm²
```

### Method 2: Duck Typing

```python
# Duck Typing - Another way of achieving polymorphism besides inheritance
# objects must have the minimum necessary attributes/methods
# "if it looks like a duck and quacks like a duck, it must be a duck"
```

```python
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Dog):
    def speak(self):
        print("Meow")

class Car:
    def speak(self):
        print("BEEP")
    
    alive = False

# Duck typing - all have speak() method
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()      # Polymorphic behavior
    print(animal.alive)

# Output:
# WOOF
# True
# Meow
# True
# BEEP
# False
```

### Polymorphism Explained

**Key concept:** Same method name behaves differently depending on the object.

**Benefits:**
- Write generic code that works with multiple types
- Add new types without changing existing code
- Flexible and extensible design

**Duck typing principle:** If it has the methods you need, you can use it - inheritance not required.

---

## How to Run

1. Navigate to the project directory
2. Run any Python file:
   ```bash
   python object_oriented_programming.py
   python class_variables.py
   python static_method.py
   python class_methods.py
   python magic_methods.py
   python inheritance.py
   python super()_function.py
   python multiple_multilevel_inheritance.py
   python polymorphism.py
   python polymorphism_duck_typing.py
   ```

---

## Key Concepts Learnt

### 1. Classes and Objects

**Class**: Blueprint for creating objects
**Object**: Instance of a class with specific data
**`__init__`**: Constructor method
**`self`**: Reference to current instance

### 2. Attributes and Methods

**Instance attributes**: Unique to each object (`self.name`)
**Class attributes**: Shared among all objects (`ClassName.variable`)
**Instance methods**: Operate on object data (`self` parameter)
**Static methods**: Utility functions (`@staticmethod`)
**Class methods**: Operate on class data (`@classmethod`, `cls` parameter)

### 3. Magic Methods

**Dunder methods**: Special methods with double underscores
**Operator overloading**: Customize behavior of operators
**Common magic methods**: `__init__`, `__str__`, `__eq__`, `__add__`, etc.

### 4. Inheritance

**Parent class**: Class being inherited from
**Child class**: Class inheriting from parent
**Syntax**: `class Child(Parent):`
**Benefits**: Code reusability, extensibility, hierarchy

### 5. The super() Function

**Purpose**: Call parent class methods
**Usage**: `super().__init__()` or `super().method()`
**Benefit**: Extend parent functionality without rewriting

### 6. Multiple Inheritance

**Syntax**: `class Child(Parent1, Parent2):`
**Use case**: Inherit from multiple parents
**Method Resolution Order (MRO)**: Left to right

### 7. Multilevel Inheritance

**Structure**: Grandparent → Parent → Child
**Hierarchy**: Chain of inheritance
**Access**: Child has access to all ancestors' methods

### 8. Polymorphism

**Definition**: Same interface, different implementations
**Method 1**: Through inheritance (override methods)
**Method 2**: Duck typing (same method name, no inheritance required)
**Benefit**: Write flexible, generic code

---

## OOP Principles Summary

### Encapsulation
Bundling data and methods that operate on that data within a class.

### Inheritance
Creating new classes from existing ones to reuse code.

### Polymorphism
Objects of different types can be accessed through the same interface.

### Abstraction
Hiding complex implementation details and showing only necessary features.

---

## Best Practices

### Naming Conventions
- **Classes**: PascalCase (`MyClass`, `StudentRecord`)
- **Methods/Attributes**: snake_case (`get_info`, `total_count`)
- **Constants**: UPPER_CASE (`MAX_SIZE`, `DEFAULT_COLOR`)

### Method Organization
1. `__init__` first
2. Other magic methods
3. Class methods
4. Static methods
5. Instance methods

### When to Use What

**Instance methods** when:
- Operating on object data
- Need access to `self`

**Static methods** when:
- Utility function related to class
- Don't need class or instance data

**Class methods** when:
- Operating on class-level data
- Need access to `cls`
- Factory methods

### Inheritance Guidelines

**Use inheritance when:**
- "is-a" relationship exists
- Child is specialized version of parent
- Want to reuse parent's code

**Avoid inheritance when:**
- "has-a" relationship (use composition)
- No clear hierarchical relationship
- Would violate Liskov Substitution Principle

---

## Common Patterns

### Factory Pattern with Class Methods
```python
@classmethod
def from_string(cls, string):
    # Parse string and create object
    return cls(parsed_data)
```

### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Template Method Pattern
```python
class Template:
    def template_method(self):
        self.step1()
        self.step2()
        self.step3()
    
    def step1(self):
        pass  # Override in subclass
```

---

**Happy Coding!**