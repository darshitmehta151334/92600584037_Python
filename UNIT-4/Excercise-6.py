#Write a program to demonstrate method overriding and polymorphism.

# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds")


# Child class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Child class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects
a = Animal()
d = Dog()
c = Cat()

print("Method Overriding:")
d.sound()
c.sound()

print("\nPolymorphism:")
for obj in [a, d, c]:
    obj.sound()
