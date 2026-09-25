#Write a program to demonstrate different import mechanisms in Python.

# 1. Import complete module
import math

print(math.sqrt(25))


# 2. Import module with alias
import math as m

print(m.pi)


# 3. Import specific function
from math import factorial

print(factorial(5))


# 4. Import multiple functions
from math import sqrt, pow

print(sqrt(16))
print(pow(2, 3))
