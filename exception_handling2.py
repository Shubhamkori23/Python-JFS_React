# Python code to illustrate working of try()
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except:
        print("Sorry ! You are dividing by zero ")


# Look at parameters and note the working of Program
divide(3, 0)
