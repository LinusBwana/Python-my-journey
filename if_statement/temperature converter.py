temp = float(input("Enter the Temperature: "))
unit = input("Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    temp = round((temp * (9/5)) + 32, 1)
    unit = "°K."
    print(f"The temperature is {round(temp, 1)}{unit}")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    unit = "°C"
    print(f"The temperature is {round(temp, 1)}{unit}")
else:
    print(f"{unit} was not a valid input")
