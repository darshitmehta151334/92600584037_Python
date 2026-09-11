# Program to demonstrate List, Dictionary and Set Comprehensions

# 1. List Comprehension
numbers = [1, 2, 3, 4, 5]
square = [num * num for num in numbers]

print("List Comprehension:")
print(square)


# 2. Dictionary Comprehension
dictionary = {num: num * num for num in numbers}

print("\nDictionary Comprehension:")
print(dictionary)


# 3. Set Comprehension
set_values = {num * num for num in numbers}

print("\nSet Comprehension:")
print(set_values)
