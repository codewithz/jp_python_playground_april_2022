try:
    file=open("1-exceptions.py")
    print("Is file closed?:",file.closed)
    age=int(input("Enter Age:"))
    xfactor=10/age
    print(f"Age is {age} and xfactor is {xfactor}")

except ValueError as ex:
    print("VE:Invalid Age Entered")

except ZeroDivisionError as ex:
    print("ZDE:You seem to enter age as zero")

except Exception as ex:
    print("Some other exception occurred")
    print("Reason:",ex)
else:
    print("No exception occured")
finally:
    print("This block executes in all conditions [Exception occurred or not]")
    file.close()
    print("Is file closed?:",file.closed)

print("\n\nExecution continues.....")

















#
# file.close()
# print("Is file closed?:",file.closed)