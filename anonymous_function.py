# Python code to demonstrate labmda function
# also known as a lamda function

# Cube using lambda
cube = lambda x: x * x * x
print(cube(7))

# List comprehension using lambda
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)
