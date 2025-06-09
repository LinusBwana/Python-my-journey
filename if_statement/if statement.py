response = str(input("Do you like food? (Y/N) ").upper())

if response == "Y":
    print("The order is on the way")
elif response == "N":
    print("Ohh, you are full")
else:
    print("Wrong input")

