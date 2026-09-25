#Write a program to copy move and delete files using shutil module.

import shutil
import os

# Create a file
with open("file1.txt", "w") as f:
    f.write("Hello Python")

# Copy file
shutil.copy("file1.txt", "file2.txt")
print("File Copied")

# Move file
shutil.move("file2.txt", "file3.txt")
print("File Moved")

# Delete file
os.remove("file3.txt")
print("File Deleted")
