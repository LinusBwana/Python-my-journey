# while loop = executes a condition WHILE some condition remains true

# example 1
# name = input("Enter your name: ")
# while name == "":
#     # print("Enter a valid name")
#     name = input("Enter a valid name: ")
# print(f"Hello {name}")


# example 2
# age = int(input("Enter your age: "))
# while age < 0:
#     age = int(input("Age can't be negative. Input age again: "))
# print(f"You are {age} years old")


# example 3
# food = input("Enter the food you like (q to quit): ")
# while not food == "q":
#     # print(f"You like {food}")
#     food = input(f"You like {food}. Enter the food you like (q to quit): ")
# print("Bye")


# example 4
num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num >10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")
