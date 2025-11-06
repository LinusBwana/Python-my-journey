# collection - single "variable" used to store multiple values
#               List = [] ordered and changeable. Duplicates OK
#               Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#               Tuple = () ordered and unchangeable. Duplicates OK.FASTER

# LIST = = = = = = = = = = = =
fruits = ["apple", "banana", "coconut", "oranges", "water mellon", "pineapples", "guavas"]
print(fruits[2:7:2])
print(fruits[::2])
print(fruits[::-2])
print(len(fruits))
print("oranges" in fruits)
fruits[3] = "tomatoes"
print(fruits)
fruits.append("carrot")
print(fruits)
fruits.insert(1, "cucumber")
print(fruits)
fruits.remove("coconut")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.index("water mellon"))
print(fruits.count("guavas"))
fruits.clear()
print(fruits)
print(dir(fruits))

# example 2
for fruit in  fruits:
    if fruit == "oranges":
        continue
    print(fruit)


# SET = = = = = = = = = = = =
# fruits = {"apple", "banana", "coconut", "oranges", "water mellon", "guavas"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("oranges" in fruits)
# fruits.add("pineapples")
# fruits.remove("guavas")
# print(fruits)
# fruits.pop()
# print(fruits)
# for fruit in  fruits:
#     if fruit == "oranges":
#         continue
#     print(fruit)



# TUPLES = = = = = = = = = = = =
# fruits = ("apple", "banana", "coconut", "oranges", "water mellon", "guavas")
# print(fruits)
# print(fruits.index("water mellon"))
# print(fruits.count("guavas"))
# for fruit in  fruits:
#     if fruit == "oranges":
#         continue
#     print(fruit)