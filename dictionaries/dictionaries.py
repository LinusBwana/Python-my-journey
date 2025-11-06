# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


print(dir(capitals))
print(help(capitals))


if capitals.get("Russia"):
    print("Capital exists")
else:
    print("Capital doesn't exists")

capitals["Kenya"] = "Nairobi"
capitals.update({"USA": "USA City"})
capitals.pop("China")
capitals.popitem()
       
print(capitals.get("USA"))
print(capitals.get("Japan"))  
print(list(capitals.items())[0])
print(list(capitals.keys())[0])
print(list(capitals.values())[0])

keys = capitals.keys()
for key in keys:
    print(key)

values = capitals.values()
for value in values:
    print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")


capitals.clear()
print(capitals)