# nested loop = a loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# example 1
# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()

# example 2
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()