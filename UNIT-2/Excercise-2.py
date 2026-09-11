# Program to check whether a number is positive, negative or zero
# using nested conditions

num1 = int(input("Enter a number:- "))

if num1 >= 0:
    if num1 == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")
