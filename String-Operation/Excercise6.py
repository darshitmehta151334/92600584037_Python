s1 = input("Input String one: ")
s2 = input("Input String two: ")

result = ""

for i in range(len(s1)):
    result = result + s1[i] + s2[i]

print("Output:", result)
