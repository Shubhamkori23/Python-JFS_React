# Python program to demonstrate constructors

class Addition:
    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def calculate(self):
        print(self.first + self.second)

# Invoking parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()
