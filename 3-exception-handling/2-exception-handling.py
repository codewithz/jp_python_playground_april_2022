try:
    age=int(input("Enter Age :"))
    print(f"Age is {age}")
except ValueError as ex:
    print("You entered invalid age")
    print(ex)
    print(type(ex))
else:
    print("Else after try executes when there is no exception")


print("Execution Continues.....")