# Program to demonstrate conditional statements

# 1. if statement
num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")


# 2. if-else statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# 3. if-elif-else statement
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
