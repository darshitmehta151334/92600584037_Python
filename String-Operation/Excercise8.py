s = input("Enter a string: ")

v = 0
c = 0

for ch in s:
    if ch in "aeiouAEIOU":
        v = v + 1
    elif ch.isalpha():
        c = c + 1

total = v + c

print("Vowels =", v)
print("Consonants =", c)
print("Vowel Percentage =", (v / total) * 100, "%")
print("Consonant Percentage =", (c / total) * 100, "%")
