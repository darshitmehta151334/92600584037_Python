# Program to generate a sequence of numbers
# using generator function and yield keyword

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

num = int(input("Enter the limit:- "))

print("Sequence of numbers:")

for number in generate_numbers(num):
    print(number)
