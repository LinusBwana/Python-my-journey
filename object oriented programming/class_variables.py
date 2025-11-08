# class variables =  shared among all instances of a class (objects)
#                    Defined outside the constructor but instance variables (objects) are defined inside the constructor
#                    Allow you to share data among all objects created from that class

class Student:

    class_year = 2024 #class variable. shared by all objects within the class
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Linus", 29)
student2 = Student("Philip", 30)
student3 = Student("Dan", 25)
student4 = Student("Sandra", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students}")
print(f"{student1.name} is {student1.age} years old")
print(f"{student2.name} is {student2.age} years old")
print(f"{student3.name} is {student3.age} years old")
print(f"{student4.name} is {student4.age} years old")
print(Student.class_year) #it is good practice to access the class variable using the class instead of the object. Helps with clarity and readability
print(Student.num_students)
