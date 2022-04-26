letters=["a","b","c","d","e"]

print(letters.index("a"))
# print(letters.index("f"))
# ValueError: 'f' is not in list

# Way 1- To make sure that program doesn't break if element is not found

if "f" in letters:
    print("Index of f:",letters.index("f"))

# Way 2- To make sure that program doesn't break if element is not found
count=letters.count("d")

if count>0:
    print("Index of d:",letters.index("d"))