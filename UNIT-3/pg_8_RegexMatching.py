#Write a program to demonstrate basic regular expression pattern matching.

import re

text = "My phone number is 9876543210"

# Find 10 digit number
result = re.search(r"\d{10}", text)

if result:
    print("Number Found:", result.group())
else:
    print("Number Not Found")
