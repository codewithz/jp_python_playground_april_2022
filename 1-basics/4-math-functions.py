i=10
print(i)
print(type(i))

f=4.5
print(f)
print(type(f))

c=10+5j
print(c)
print(type(c))

# Convert this values
print("----------------------------")
f1=float(i)
print(i)
print(f1)


i1=int(f)
print(f)
print(i1)

c1=complex(f)
print(f)
print(c1)

# In Build Functions
print("-"*40)
min_value=min(1,2,3,4,5,6,7)
print("Min:",min_value)

max_value=max(1,2,3,4,5,6,7)
print("Max:",max_value)

a=-3
print(a)
a=abs(a)
print("Abs",a)

cube_of_four=pow(4,3)
print("4 to power of 3 is",cube_of_four)

print(40*"-")
import math

print(dir(math))
print("PI",math.pi)

print("Square root of 64 is ",math.sqrt(64))

print("Remainder",math.remainder(5,2))

number=4

factorial=math.factorial(number)
print("Factorial of ",number,'is',factorial)
# Trignoetry Function
print(40*"-")
radian=math.radians(90)
print("Radian of 90 is",radian)
print("Sin 90",math.sin(radian))