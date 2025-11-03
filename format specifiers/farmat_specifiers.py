# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value
# := = place a sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 13366.563336
price2 = -73355.25266
price3 = 3242.33536

# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 2 is ${price2:.1f}")
# print(f"Price 3 is ${price3:.1f}")

# print(f"Price 1 is ${price1:12}")
# print(f"Price 2 is ${price2:12}")
# print(f"Price 3 is ${price3:12}")

# print(f"Price 1 is ${price1:012}")
# print(f"Price 2 is ${price2:012}")
# print(f"Price 3 is ${price3:012}")

print(f"Price 1 is ${price1:<012}")
print(f"Price 2 is ${price2:<012}")
print(f"Price 3 is ${price3:>012}")

# print(f"Price 1 is ${price1:+,.2f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}")