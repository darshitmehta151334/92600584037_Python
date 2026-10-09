#Write a program to illustrate method resolution order and magic methods.

# Demonstration of MRO and Magic Methods
class A:
    def show(self):
        print("Class A method")

class B(A):
    def show(self):
        print("Class B method")

class C(A):
    def show(self):
        print("Class C method")

class D(B, C):
    def show(self):
        print("Class D method")


# Creating object
obj = D()

print("Method Resolution Order (MRO):")
print(D.mro())

print("\nCalling show() method:")
obj.show()

# Magic Methods
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return "Name: " + self.name + ", Marks: " + str(self.marks)

    def __len__(self):
        return len(self.name)


s1 = Student("Darshit", 90)

print("\nMagic Methods:")
print(s1)
print("Length of name:", len(s1))
