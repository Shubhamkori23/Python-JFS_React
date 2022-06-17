# Creating an empty Dictionary
Dict = {}
print(Dict)

# with Integer Keys
Dict = {1: 'Aliens', 2: 'Are', 3: 'Aliens'}
print(Dict)

# with Mixed keys
Dict = {'Name': 'Shubham', 1: [1, 2, 3, 4]}
print(Dict)

# Creating a Nested Dictionary as shown in the below image
Dict = {1: 'Aliens', 2: 'Are',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Earth'}}

print(Dict)

# Creating an empty Dictionary
Dict = {}

# Adding elements one at a time
Dict[0] = 'Aliens'
Dict[2] = 'Exist'
Dict[3] = 1
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print(Dict)

# Python program to demonstrate accessing an element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Aliens', 'name': 'Are', 3: 'Aliens'}

# accessing a element using key
print(Dict['name'])

# accessing a element using get()
print(Dict.get(3))

# Removing Elements from Dictionary

# Initial Dictionary
Dict = {5: 'Welcome', 6: 'To', 7: 'Earth',
        'A': {1: 'Aliens', 2: 'Are', 3: 'Aliens'},
        }

# using pop()
Dict.pop(5)
print(Dict)

# using popitem()
Dict.popitem()
print(Dict)
