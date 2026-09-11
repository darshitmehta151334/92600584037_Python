# Program to find the sum of digits using while loop

num1 = int(input("Enter a number:- "))

sum = 0

while num1 > 0:
    digit = num1 % 10
    sum = sum + digit
    num1 = num1 // 10

print("Sum of digits =", sum)
