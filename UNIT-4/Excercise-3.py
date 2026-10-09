#Write a program to illustrate instance variables and class variables.

class Mobile:
    # Class variable
    brand = "Samsung"

    def __init__(self, model):
        # Instance variable
        self.model = model


m1 = Mobile("Galaxy S24")
m2 = Mobile("Galaxy A55")

print("Brand:", Mobile.brand)
print("Mobile 1:", m1.model)
print("Mobile 2:", m2.model)
