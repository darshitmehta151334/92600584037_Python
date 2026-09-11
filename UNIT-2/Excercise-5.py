# Program to demonstrate break, continue and pass statements

# 1. break statement
print("Using break:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)


# 2. continue statement
print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 3. pass statement
print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
