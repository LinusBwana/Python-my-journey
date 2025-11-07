import random

low = 1
high = 100

# example 1
# number = random.randint(low,high)
number = random.random()
print(f"{number:.2f}")

# example2 - picking random from a list and tuples
options = ("rock", "paper", "scissors")
pick = random.choice(options)
print(pick)

# example3
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A","JOKER"]
random.shuffle(cards)
print(cards)
