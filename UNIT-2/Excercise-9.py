# Program to demonstrate Iterables and Iterators in Python

# Iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:")
for num in numbers:
    print(num)

# Iterator
print("\nIterator:")

my_iterator = iter(numbers)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
