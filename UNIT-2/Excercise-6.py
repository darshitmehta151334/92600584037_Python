# Program to iterate over lists, strings and dictionaries using loops

# 1. Iterate over a list
print("List:")
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# 2. Iterate over a string
print("\nString:")
name = "PYTHON"

for ch in name:
    print(ch)


# 3. Iterate over a dictionary
print("\nDictionary:")
student = {
    "Name": "Darshit",
    "Age": 21,
    "Course": "MCA"
}

for key, value in student.items():
    print(key, ":", value)
