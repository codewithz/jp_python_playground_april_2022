letters=["a","b","c","d","e"]

for letter in letters:
    print(letter)

print(40*'-')

for element in enumerate(letters):
    print(element)
    print(type(element))

print(40*'-')

item=(0, 'a')
index,value=item
print(index,'-',value)

print(40*'-')

for index,value in enumerate(letters):
    print(index,'#',value)

