# Python program to illustrate while and while-else loop
i = 0
while (i < 3):
    i = i + 1
    print("Hello Aliens")

# checks if list still contains any element
a = [1, 2, 3, 4]
while a:
    print(a.pop())

i = 10
while i < 12:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
