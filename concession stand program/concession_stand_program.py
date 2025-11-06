# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25,}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: Ksh{value:.2f}")
print("--------------------------")

while True:
    food = input("Select and item (q to quit): ").lower()

    if food == "q":
        break

    if food not in menu.keys():
        if food == "q":
            break
        else:
            print("Not Available. Check the menu")
            continue
    else:
        menu.get(food)
        cart.append(food)


if cart:
    print("--------YOUR ORDER--------")
    for food in cart:
        price = menu.get(food)
        price += price
        print(f"{food:10} Ksh{price:.2f}")

    print(f"Total amount: {total:.2f}")
    print("--------------------------")
else:
    print("--------------------------")
    print("You didn't order anything. Goodbye!")
    print("--------------------------")
