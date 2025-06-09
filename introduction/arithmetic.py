import math

a = float(input("Enter the side a: "))
b = float(input("Enter the side b: "))
c = math.sqrt(pow(a,2) + pow(b,2))

# radius = float(input("Enter the radius: "))
# circumference = 2 * math.pi * radius
# area = math.pi * pow(radius, 2)
#
#
# print(f"the circumference is: {round(circumference, 2)}cm")
# print(f"the area is: {round(area, 3)}cm")
print(f"side C is: {round(c, 2)}cm")