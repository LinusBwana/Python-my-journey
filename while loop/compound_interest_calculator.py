principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))
    error = []

    if principle < 0:
        error.append("Principle can't be less than zero")

    if rate < 0:
        error.append("Interest rate can't be less than zero") 

    if time < 0:
        error.append("Time can't be less than zero")
    
    if error:
        for e in error:
            print("-", e)
        print("Try again")
        continue
    else:
        total = principle * pow((1 + (rate / 100)), time)
        print(f"Balance after {time} year/s: ${total:.2f}")
        break