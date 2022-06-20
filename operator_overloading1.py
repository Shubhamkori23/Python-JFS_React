# Python Program illustrate how to overload a binary + operator

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Aliens ")
ob4 = A("Exist")

print(ob1 + ob2)
print(ob3 + ob4)
