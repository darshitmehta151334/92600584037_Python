#Write a program to demonstrate instance methods class methods and static methods.

class Student:
    college = "Marwadi University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Class Method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static Method
    @staticmethod
    def message():
        print("Welcome to Python Programming!")


# Creating an object
s1 = Student("Darshit", 21)

print("Instance Method:")
s1.display()

print("\nClass Method:")
Student.show_college()

print("\nStatic Method:")
Student.message()
