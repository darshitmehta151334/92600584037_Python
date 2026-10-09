#Write a program to demonstrate encapsulation and abstraction using classes.

from abc import ABC, abstractmethod

# Encapsulation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


# Abstraction
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Creating objects
print("Encapsulation:")
account = BankAccount("Darshit", 50000)
account.deposit(10000)
account.display_balance()

print("\nAbstraction:")
r = Rectangle(10, 5)
print("Area of Rectangle:", r.area())
