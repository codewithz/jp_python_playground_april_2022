# Tuples are Read Only List
#  ()


# Ways to define a Tuple

point=(1,2)
print(type(point))
print(point)

point=1,
print(type(point))
print(point)

point=1,2
print(type(point))
print(point)

point=(1,2)+(3,4)
print(type(point))
print(point)

point=(1,2)*3
print(type(point))
print(point)

# -------------------------------------------
# Access elements in Tuple
print(40*'-')
point=(1,2,3)

print(point)
print("Index 1:",point[1])
print("Range Access:",point[0:2])

x,y,z=point

print(x,",",y,",",z)

if 10 in point:
    print("10 is  in tuple")
else:
    print("10 is not in tuple")

 # ----------------------------------
print(40*'-')

# point[1]=20
# TypeError: 'tuple' object does not support item assignment
