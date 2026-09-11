# Program to generate multiplication table using for loop

num1 = int(input("Enter a number:- "))

for i in range(1, 11):
    print(num1, "x", i, "=", num1 * i)
