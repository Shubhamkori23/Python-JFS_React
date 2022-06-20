# Python program to overload equality and less than operators

class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "object1 is less than object2"
        else:
            return "object2 is less than object1"

    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"


ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)
