# list compression = a concise way to create list in Python
#                    compact and easier way to read than traditional loops
#                    [expression for value in iterable if condition]


# traditional
doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

# list compression
# example1
doubles = [x * 2 for x in range(1,11)]
print(doubles)

# example2
triples = [y * 3 for y in range(1,11)]
print(triples)

squares = [y * y for y in range(1,11)]
print(squares)

fruits = ["apple", "orange", "banana"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruits = [print(fruit.capitalize()) for fruit in ["apple", "orange", "banana"]]
fruit_char = [print(fruit[0]) for fruit in ["apple", "orange", "banana"]]

# ETC ----------------------------------------------
# name = input("Enter the name to count characters: ")
# print(name.count("a"))
# print(len(name))

# example3
numbers = [1, -2, 3, -5, 12, -24, 14, 4, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [print(num) for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [85, 76, 59, 78, 49, 30, 78, 63]
pass_grade = [print(grade, end=" ") for grade in grades if grade >= 75]
