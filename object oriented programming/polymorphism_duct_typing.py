# Duck Typing - Another way of achieving polymorphism besides inheritance
# objects must have the minimum necessary attributes/methods
# if it looks like a duct and quacks like a duct, it must be a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOW")

class Cat(Dog):
    def speak(self):
        print("Meow")

class Car:
    def speak(self):
        print("PIIIIIP")

    alive = False

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
