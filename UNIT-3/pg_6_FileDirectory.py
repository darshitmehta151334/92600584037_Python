#Write a program to perform file and directory operations using os and sys modules.

import os
import sys

print("Current Directory:", os.getcwd())

print("Files and Folders:", os.listdir())

# Create directory if it does not exist
if not os.path.exists("TestFolder"):
    os.mkdir("TestFolder")
    print("Directory Created")
else:
    print("Directory Already Exists")

print("Directory Exists:", os.path.exists("TestFolder"))

print("Python Version:", sys.version)
