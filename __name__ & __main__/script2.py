from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")


def main():
    print("This is script2")
    favourite_food("Chips")
    favourite_drink("coffee")
    print("Bye")

if __name__ == '__main__':
    main()