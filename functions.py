# Python program to demonstrate functions

# Defining functions
def ask_user():
    print("Hello Aliens")


# Function that returns sum of first 10 numbers
def my_func():
    a = 0
    for i in range(1, 11):
        a = a + i
    return a


# Calling functions
ask_user()
res = my_func()
print(res)
