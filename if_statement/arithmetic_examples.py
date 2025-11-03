num1 = float(input("The the 1st number: "))
num2 = float(input("The the 2nd number: "))
operator = input("Choose an operator (+ - * /): ")

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 - num2
    print(round(result, 2))
elif operator == "/":
    result = num1 - num2
    print(round(result, 2))
else:
    print(f"The operator {operator} is invalid")