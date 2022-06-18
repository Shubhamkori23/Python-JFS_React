# Python program to illustrate Iterating over a list
print("List Iteration")
l = ["Aliens", "Are", "Aliens"]
for i in l:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Aliens"
for i in s:
    print(i)

print("\nFor-else loop")
for i in s:
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

for i in s:
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
