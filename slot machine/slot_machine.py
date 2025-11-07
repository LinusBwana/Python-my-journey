import random
import time

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔',  '⭐']
    # results = []
    return [random.choice(symbols) for _ in range(3)]
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

def print_row(row):
    print("****************************")
    print(" | ".join(row))
    print("****************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100
    print("****************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("****************************")

    while balance > 0:

        print(f"Current balance: Ksh {balance}")

        bet = input("Place your bet amount Ksh: ")

        if not bet.isdigit():
            print("Please enter a valid amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("Bet amount can not be greater than balance")
            continue

        if bet <= 0:
            print("Bet amount must be greater than 0")

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(3)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won Ksh{payout}. Remaining balance Ksh {balance}")
        else:
            print(f"You lost the bet. Remaining balance Ksh {balance}")

        balance += payout

        while True:
            if balance == 0:
                print(f"Gave over: Your balance is Ksh {balance}")
                return

            play_again = input("Do you want to spin again? (y/n): ").upper()

            if play_again == "Y":
                break
            elif play_again == "N":
                print("****************************")
                print(f"Gave over: Your balance is Ksh {balance}")
                print("****************************")
                return # Exits the entire function/method (and can optionally return a value)
            else:
                print("Invalid Input. ")

    print("****************************")
    print(f"insufficient Funds: Your balance is Ksh {balance}")
    print("****************************")

if __name__ == '__main__':   
    main()