# Polymorphism - Greek word that means to "Have many forms or faces"
# poly - Many
# Morphe - From

# Two ways of achieving Polymorphism
# 1. Inheritance - an object could be treated of the same type as the parent class
# 2. "Duck Typing" - Object must have necessary attributes/methods


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.radius = side

    def area(self):
        return self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        # Circle.__init__(self, radius)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("BBQ", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")