letters=["a","b","c","d","e"]
print(letters)

# access the first element
print("First Element",letters[0])

# access the last element
print("Last Element",letters[-1])

# Access in Ranges

print(letters[0:2])
print(letters[:3])
print(letters[2:])

# Clone
letters_clone=letters[:]
print("Clone",letters_clone)

# Steppers
numbers=list(range(1,21))

print(numbers[::2])
print(numbers[::-1])

matrix=[[0,1],[2,3]]
print(matrix)

matrix_one=matrix[0]
print(matrix_one)
print(matrix_one[0])
print(matrix_one[1])

print(matrix[1][1])