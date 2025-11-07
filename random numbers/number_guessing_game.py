import random

lower = 1
upper = 10
no_guesses = 0
number = random.randint(lower,upper)

print("----Python Number Guessing Game----")
while True:
    guess = input(f"Guess a number between {lower} and {upper}: ")
    if guess.isdigit():
        guess = int(guess)
        no_guesses += 1
        if guess == number:
            # no_guesses += 1
            print(f"CORRECT GUESS.The answer is {guess}")
            print(f"The number of guesses is: {no_guesses}")
            break
        elif guess < number:
            # no_guesses += 1
            print("Too Low! Try again.")
            print(f"The number of guesses is: {no_guesses}")
            continue
        elif guess > number:
            # no_guesses += 1
            print("Too High! Try again.")
            print(f"The number of guesses is: {no_guesses}")
            continue
    else:
        if guess == "q":
            print(f"The number of guesses is: {no_guesses}.\nThe correct answer was {number}")
            print("Bye")
            break
        else:
            no_guesses += 1
            print("Guess should an integer:")
            print(f"The number of guesses is: {no_guesses}")