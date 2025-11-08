import random

from wordslist import words

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" 0 ",
                   " | ",
                   "   "),
               3: (" 0 ",
                   "/| ",
                   "   "),
               4: (" 0 ",
                   "/|\\",
                   "   "),
               5: (" 0 ",
                   "/|\\",
                   "/  "),
               6: (" 0 ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guess):
    print("*****************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("*****************")
    # for key in hangman_art.keys():
    #     if key == wrong_guess:
    #         print("\n".join(hangman_art[key]))

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(f"The answer is: {answer}")
            print("YOU LOST")
            is_running = False

if __name__ == '__main__':
    main()



# LEARNING------------------------------------------
# print(hangman_art[4][0])

# for key in hangman_art.keys():
#     if key == 6:
#         print("\n".join(hangman_art[key]))