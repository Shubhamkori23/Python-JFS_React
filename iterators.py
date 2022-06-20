# Here is an example of a python inbuilt iterator value can be anything which can be iterate
iterable_value = 'Aliens'
iterable_obj = iter(iterable_value)

while True:
    try:

        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break

# Sample built-in iterators

# Iterating over a list
print("List Iteration")
l = ["aliens", "for", "aliens"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("aliens", "for", "aliens")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Aliens"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
