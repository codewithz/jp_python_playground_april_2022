# Set --> NO DUPLICATES | UNORDERED

# {}

numbers=[1,2,3,4,4,4,5]

print("List:",numbers)
first=set(numbers)
print("Set:",first)

first={*numbers}
print("Set with list:",first)

second={1,4,5}

print(40*'-')
print("First:",first)
print("Second:",second)

# Add and Remove
second.add(6)
print("Second:",second)
print(40*'-')
second.add(6)
print("Second:",second)
print(40*'-')
second.remove(4)
print("Second:",second)

# second.remove(4)
# print("Second:",second)
# KeyError: 4
print(40*'-')
second.discard(4)
print("Second:",second)

print("--------------- Set Operations --------------------")
print("First:",first)
print("Second:",second)

print("Union",first.union(second))
print("Union",first | second)

print("Intersection:",first.intersection(second))
print("Intersection:",first & second)

print("Difference:",first.difference(second))
print("Difference:",first - second)

print("Symmetric Difference:",first.symmetric_difference(second))
print("Symmetric Difference:",first^second)

