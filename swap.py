a = 5  # 101
b = 6  # 110

c = 5
d = 6

i = 13
j = 17

x = 25
y = 34

# using of 3rd variable
temp = a
a = b
b = temp

print(a)
print(b, "\n")

# without using of third variable in this method we still wasting 1bit so we didn't use this method
c = c + d  # 11  but it takes 4 bit so we still wasting 1 bit
d = c - d  # 5
c = c - d  # 6

print(c)
print(d, "\n")

# another method by using xor
i = i ^ j
j = i ^ j
i = i ^ j

print(i)
print(j, "\n")

# simple way is swaps the two top most stack items
x, y = y, x

print(x)
print(y)
