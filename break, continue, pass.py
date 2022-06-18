# Python program to demonstrate break, continue and pass

s = 'aliensarealiens'

for letter in s:
    if letter == 'e' or letter == 's':
        break
    print(letter, end=" ")
print()

for letter in s:
    if letter == 'e' or letter == 's':
        continue
    print(letter, end=" ")
print()

for letter in s:
    if letter == 'e' or letter == 's':
        pass
    print(letter, end=" ")
