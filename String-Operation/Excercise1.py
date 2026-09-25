nm = input("Enter Your Full Name: ")

words = nm.split()

for word in words:
    print(word[0], end=".")
