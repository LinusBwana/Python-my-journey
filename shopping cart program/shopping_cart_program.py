# shopping cart program

from operator import index

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        while True:
            price = input(f"Enter the price of {food}. (Should be numeric): Ksh ")
            try:
                price = float(price)
                foods.append(food)
                prices.append(price)
                break
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue


print("-------YOUR CART-------")

for price in prices:
    total += price

for food in foods:
    for price in prices:
        if foods.index(food) == prices.index(price):
            print(f"{food:15} {price}")
print(f"Your total is: Ksh {total:.2f}")