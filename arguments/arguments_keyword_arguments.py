# keyword arguments = an argument preceded by an identifier
# helps with readability
# order of arguments does not matter


# example1
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
hello("Hello", title="Mr",last="Ogero", first="Linus")


#example2
for x in range(1,10):
    print(x, end=" ") #end is  keyword argument found within built in print statement
print()


#example3
print("1","2","3","4","5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_number= get_phone(country=254, area="711", first="618", last="688")
print(phone_number)

