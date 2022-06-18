# Python program to demonstrate default arguments

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y, "\n")


# Driver code
myFun(10)


# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Shubham', lastname='Kori')
student(lastname='Kori\n', firstname='Shubham')


# Python program to demonstrate variable length arguments

# variable arguments
def myFun1(*argv):
    for arg in argv:
        print(arg, end=" ")


# variable keyword arguments
def myFun2(**kwargs):
    for key, value in kwargs.items():
        print("% s == % s" % (key, value))


# Driver code
myFun1('Hello', 'Welcome', 'to', 'AlienWorld')
print()
myFun2(first='Aliens', mid='are', last='Aliens')
