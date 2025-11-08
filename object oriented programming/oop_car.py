class Car :
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self): #drive, stop and describe are the methods. Identical for each object
        print(f"You drive the {self.colour} {self.model}")

    def stop(self):
        print(f"You stop the {self.colour} {self.model}")

    def describe(self):
        return f"{self.year} {self.colour} {self.model}"
