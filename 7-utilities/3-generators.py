from sys import getsizeof


values=[x*2 for x in range(10000000)]
# print(values)
print("Size of memory:",getsizeof(values))

print(40*"-")

values=(x*2 for x in range(10000000))
print(values)
print("Size of memory:",getsizeof(values))

