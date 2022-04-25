if True:
    print("Hello")

print("I will execute")
# ----------------------------------
print(40*'-')

x=2

if x>3:
    print("Tom")
else:
    print("Alex")

# ---------------------------------
print(40 * '-')
a=300
b=330
if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

# -----------------------------------
print(40*'-')

a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
c=int(input("Enter third value:"))

if (a>b and a>c):
    print(f"{a} is greater than {b} and {c}")
elif (b>a and b>c):
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {b} and {a}")