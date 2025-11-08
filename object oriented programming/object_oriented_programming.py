# object = a bundle of related attributes (variables) and methods (functions). An instance of a class
#          attributes describes what the object has. Are variables that an object has
#          methods are functions that belong to an object. They define what an object can do.
#          e.g phone, cup, book
#          You need a "class" to create many objects

# class = A blueprint used to design the structure and layout of an object

from oop_car import Car

car1 = Car("Mazda", "2024", "Red", False)
car2 = Car("BMW","2022", "Black", False)
car3 = Car("Crown","2020", "Blue", True)

print(car1.model) #accessing the car attribute
print(car1.year)
print(car1.colour)
print(car1.for_sale)

car1.drive()
car1.stop()
print(car2.describe())