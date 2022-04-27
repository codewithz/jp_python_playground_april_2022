def calcualate_xfactor(number):
    if number<=0:
        raise ValueError("Number cannot be zero or less")
    return 10/number;

# -----------------------------------------------

try:
    xfactor=calcualate_xfactor(-20)
    print(xfactor)
except ValueError as ex:
    print(ex)



print("\n\nExecution Continues.....")