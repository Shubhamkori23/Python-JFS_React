# Python program to demonstrate encapsulation

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "AliensareAliens"
        self.__c = "AliensareAliens"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__a)


# Driver code
obj = Derived()
