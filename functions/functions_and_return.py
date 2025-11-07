# function = a block of reusable code
#            place () after the function name to invoke it
#            we use def to define a function

# return = statement used to end a function and send a result back to the caller

# example1
def happy_birthday(name, age):
    print(f"Happy birthday {name}")
    print(f"You are {age} years old")
    print()
happy_birthday("Linus", 20)
happy_birthday("Annette", 30)
happy_birthday("bro", 29)


# example2
def add(x,y):
    z = x + y
    return  z
def subtract(x,y):
    z = x - y
    return  z
def multiply(x,y):
    z = x * y
    return  z
def divide(x,y):
    z = x / y
    return  z
print(add(25,5))
print(subtract(25,5))
print(multiply(25,5))
print(divide(25,5))


# example3
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" "+ last
full_name = create_name("linus", "bwana")
print(full_name)