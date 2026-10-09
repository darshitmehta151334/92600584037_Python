#Write a program to perform file pointer operations using seek and tell methods.

# Program to demonstrate seek() and tell()

# Create and write data into a file
f = open("demo.txt", "w")
f.write("Hello Python Programming")
f.close()

# Open file for reading
f = open("demo.txt", "r")

# Display current file pointer position
print("Initial position:", f.tell())

# Read first 5 characters
data = f.read(5)
print("Read data:", data)
print("Position after reading:", f.tell())

# Move file pointer to position 6
f.seek(6)
print("Position after seek:", f.tell())

# Read remaining data from current position
print("Remaining data:", f.read())

f.close()
