#Write a program to use re module functions such as match search and findall.

import re

text = "Python is easy. Python is powerful."

# match()
print("Match:", re.match("Python", text))

# search()
print("Search:", re.search("easy", text))

# findall()
print("Findall:", re.findall("Python", text))
