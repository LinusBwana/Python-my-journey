# arbitrary meaning varying amount of arguments
# *args = allows you to pass multiple non-key arguments
# **kwargs =  allows you to pass multiple keyword-arguments
# *unpacking operator

# *args _______________________________________
# example1
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add(1,2,3,4,5,6,1))


# example2
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Eng", "Linus", "Bwana","EBK")


# **kwargs ______________________________________
# example1
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:8}: {value}")
print_address(street="Clay CIty",
                    city="Nairobi",
                    state="Kasarani",
                    zip="00618")