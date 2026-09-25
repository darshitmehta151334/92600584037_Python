s = input("Enter a string: ")

count = 0
sum = 0

for ch in s:
    if ch.isdigit():
        count = count + 1
        sum = sum + int(ch)

print("No. of digits:", count)
print("Sum of digits:", sum)
