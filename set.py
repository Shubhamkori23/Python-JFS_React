# Python program to demonstrate Creation of Set in Python

# Creating a Set
set1 = set()

# Creating a Set of String
set1 = set("AlenWorld")
print(set1)

# Creating a Set of List
set1 = set(["Aliens", "Are", "Aliens"])
print(set1)

# Python program to demonstrate Addition of elements in a Set

set1 = set()

# Adding to the Set using add()
set1.add(8)
set1.add((6, 7))
print(set1)

# Additio to the Set using Update()
set1.update([10, 11])
print(set1)

# Python program to demonstrate Accessing of elements in a set

# Creating a set
set1 = set(["Aliens", "Are", "Aliens"])

# Accessing using for loop
for i in set1:
    print(i, end=" ")

# Python program to demonstrate Deletion of elements in a Set

set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])

# using Remove() method
set1.remove(5)
set1.remove(6)
print(set1)

# using Discard() method
set1.discard(8)
set1.discard(9)
print(set1)

# Set using the pop() method
set1.pop()
print(set1)

# Set using clear() method
set1.clear()
print(set1)
