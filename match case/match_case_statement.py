# match-case statement (switch) - An alternative to using many elif statements
# Execute some code if a value matches a case
# Benefits - cleaner and the syntax is more readable

# example1
def day_of_week(day):
    match day:
        # if day == 1:
        case 1:
            return "It is Sunday"
        # elif if day == 2
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is friday"
        case 7:
            return "It is Saturday"
        case _: #is a wildcard.print incase all other cases fail
            return "Invalid day"
print(day_of_week(9))

# example2
def is_weekend(day):
    match day:
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case "Sunday":
            return True
        case _: #is a wildcard.print incase all other cases fail
            return "Invalid day"
print(is_weekend("Monday"))


# example3
def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _: #is a wildcard.print incase all other cases fail
            return "Invalid day"
print(is_weekend("Pizza"))