# Program to demonstrate variable scope
# using local, global and nonlocal variables

# Global variable
x = 10

def outer():
    y = 20

    def inner():
        nonlocal y
        y = 30

        # Local variable
        z = 40

        print("Global variable:", x)
        print("Nonlocal variable:", y)
        print("Local variable:", z)

    inner()

outer()
