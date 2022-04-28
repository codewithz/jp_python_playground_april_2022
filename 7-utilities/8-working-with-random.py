import random
import  string

print(random.random())

print(random.randint(30,50))

print(random.choice([12,23,34,45,56,67,78,89]))

print(random.choices([12,23,34,45,56,67,78,89],k=2))

def genrate_random_password():
    random_password="".join(random.choices(string.digits+string.ascii_letters,k=6))
    return random_password

print("Random Password:",genrate_random_password())