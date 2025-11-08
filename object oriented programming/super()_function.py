# super() - Function used in a child class (subclass) to call methods from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        # super().__init__(colour, is_filled)
        Shape.__init__(self,colour, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is circle of area of {3.14 * int(self.radius) * int(self.radius):.1f}cm^2")


class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is square of area {int(self.width) * int(self.width):.1f}cm^2")

class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is triangle of area {0.5 * int(self.width) * int(self.height):.1f}cm^2")

circle = Circle(colour="Red", is_filled=False, radius="4")
square = Square(colour="Black", is_filled=True, width="5")
triangle = Triangle(colour="Blue", is_filled=True, width="7", height="8")

# print(circle.radius)
# print(square.width)
# print(triangle.height)
circle.describe()
square.describe()
triangle.describe()


