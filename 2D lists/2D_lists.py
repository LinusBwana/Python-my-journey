# 2D list - a list made up of lists

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]
#we can modify below to be either a List, Set or Tuple
groceries = [("apple", "orange", "banana", "coconut"),
             ("celery", "carrots", "potatoes"),
             ("chicken", "fish", "turkey")]

fruits[0] = "mango"
print(groceries)
print(groceries[0])
print(groceries[2][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()