#Write a program to read and write data into a file using different file modes.

# Program to demonstrate different file modes

# 1. Write mode (w)
f = open("student.txt", "w")
f.write("Name: Darshit\n")
f.write("Course: Python\n")
f.write("Marks: 90\n")
f.close()
print("Data written successfully.")

# 2. Read mode (r)
f = open("student.txt", "r")
print("\nReading file:")
print(f.read())
f.close()

# 3. Append mode (a)
f = open("student.txt", "a")
f.write("College: Marwadi University\n")
f.close()
print("Data appended successfully.")

# 4. Read and write mode (r+)
f = open("student.txt", "r+")
print("\nReading data using r+ mode:")
print(f.read())
f.close()

# 5. Write and read mode (w+)
f = open("student2.txt", "w+")
f.write("Welcome to Python Programming")
f.seek(0)
print("\nReading data using w+ mode:")
print(f.read())
f.close()
