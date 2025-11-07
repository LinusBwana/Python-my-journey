import random

options = ("rock", "paper", "scissors")
results = ("You win", "You Lose", "Draw")
your_score = 0
computer_score = 0

while True:
    computer_move = random.choice(options)
    your_move = input("Pick a move: (rock, paper or scissors). Press q to quit game: ").lower()
    if your_move not in options:
        if your_move == "q":
            if your_score > computer_score:
                result = results[0]
            elif your_score < computer_score:
                result = results[1]
            else:
                result = results[2]
            print(f"Your score:{your_score} | computer score:{computer_score} | Results:{result}")
            print("Bye")
            break
        else:
            print("Incorrect Option")
            print(f"Your score:{your_score} | Computer score:{computer_score}")
            continue

    if your_move == computer_move:
        result = results[2]
    elif (your_move == "rock" and computer_move != "paper") or \
            (your_move == "paper" and computer_move != "scissors") or \
            (your_move == "scissors" and computer_move != "rock"):
        result = results[0]
    else:
        result = results[1]

    if result == results[0]:
        your_score += 5
    if result == results[1]:
        computer_score += 5

    print(f"Your move:{your_move} | computer move:{computer_move} | Results:{result}")
    print(f"Your score:{your_score} | Computer score:{computer_score}")
    continue

