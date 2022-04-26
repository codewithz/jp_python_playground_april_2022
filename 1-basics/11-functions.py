print("-"*20,"Normal Function",20*"-")

def greet():
    print("Hi There")
    print("Welcome Aboard")


greet()

print("-"*20,"Functions with parameters",20*"-")

def greeting(first_name,last_name):
    print(f"{first_name},{last_name}")


greeting("Zartab","Nakhwa")
greeting("Micheal","Smith")


print("-"*20,"Functions with return type",20*"-")

# Types of Functions

# 1. Perform a Task
# 2. Do some processing and return a value

# 1. Perform a Task

def greet(name):
    print("Hi",name)

greet("Tom")

# ---------------------------
def get_greeting(name):
    return "Hi "+name

message=get_greeting("Alex")

# Send this in email
# Store this in DB
# Store it in a file
# Send it over a network
# Print in log
print(message)

print("-"*20,"Keyword Arguments",20*"-")

import math
def increment_after_factorial(number,by):
    number=math.factorial(number)
    added_values=number+by
    return  added_values

result=increment_after_factorial(4,1)
print(result)

result=increment_after_factorial(number=5,by=2)
print(result)

print("-"*20,"Default Arguments",20*"-")

def increment(number,by=1):
    return number+by;

result=increment(4)
print(result)

result=increment(6,3)
print(result)

print("-"*20,"Varying Arguments [xargs]",20*"-")

def multiply(*numbers):
    print(numbers,type(numbers))
    total=1
    for number in numbers:
        total=total*number
    return  total

print(multiply(6,5))
print(multiply(6,5,4))
print(multiply(6,5,4,3))

print("-"*20,"Varying Arguments for Dict [xxargs/kwargs]",20*"-")

def save_user(**user):
    print(user)
    print(type(user))

save_user(id=1,name="Tom",dept="IT",salary=30000)
save_user(id=2,name="Alex",color="Green",sport="Cricket")

