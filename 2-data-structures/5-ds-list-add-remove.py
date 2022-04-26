letters=["a","b","c","e","e"]

print("Orignal",letters)

# Add elements
letters.append("d")
print("Append",letters)

# Insert Elements
letters.insert(0,'-')
print("Insert",letters)

# Remove
removed=letters.pop(0)
print("Removed Value from List",removed)
print("Popped",letters)

letters.remove("e")
print("Remove",letters)

del letters[1]
print("Del",letters)

numbers=list(range(1,11))
print("Numbers",numbers)

del numbers[4:6]
print("Del",numbers)