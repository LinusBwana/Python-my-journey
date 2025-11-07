def show_balance(balance):
    print("******************************")
    print(f"Your balance is Ksh.{balance:.2f}")
    print("******************************")

def deposit():
    amount = float(input("Enter amount to deposit in Ksh: "))

    if amount < 0:
        print("******************************")
        print("That is an invalid amount")
        print("******************************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw in Ksh: "))

    if amount > balance:
        print("******************************")
        print("Insufficient amount")
        print("******************************")
        return 0
    elif amount < 0:
        print("******************************")
        print("Amount must be greater than 0 ")
        print("******************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("******************************")
        print("Welcome To ABSA Bank")

        print("1. Show balance\n2. Deposit\n3. Withdraw\n4. Exit")
        print("******************************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            # break
            is_running = False
        else:
            print("******************************")
            print("You have entered an invalid choice")
            print("******************************")

    print("******************************")
    print("Thank You Have A Nice Day")
    print("******************************")
    
if __name__ == "__main__":
    main()


