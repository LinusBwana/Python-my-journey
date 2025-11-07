# Iterables = An object/collection that can be return its elements one at a time, allowing it to be iterated
# over in a loop

# Lists are iterables
# Tuples are iterables
# Sets are not iterables
# dictionaries are iterables

# example1
# name = "Linus Bwana"
# for character in name:
#     print(character, end=" ")

my_dictionary = {"A": 1, "b":2, "c":3}

for key, value in my_dictionary.items():
    print(f"{key} : {value}")