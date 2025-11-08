# multiple inheritance = inherit from more than one parent class
#                        C(A,B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is sleeping")

    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predictor(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predictor):
    pass

class Fish(Prey, Predictor):
    pass

# Rev2
#*************************************************
rabbit = Rabbit("Kasuku")
# hawk = Hawk()
fish = Fish("Tilapia")
rabbit.eat()
fish.flee()
fish.hunt()
fish.sleep()

#*************************************************

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Eagle")
# fish = Fish("Dolphin")
# #
# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()
#
# rabbit.eat()
# hawk.sleep()
# fish.hunt()
