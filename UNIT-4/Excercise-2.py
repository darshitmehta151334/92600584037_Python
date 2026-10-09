#Write a program to demonstrate constructor and destructor usage.

class Student:
    def __init__(self):
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called")

s1 = Student()
print("Student object created")
del s1
