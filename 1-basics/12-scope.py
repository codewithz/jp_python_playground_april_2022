message="Hello All"

def greet(name):
    message="Hello"
    print(name)


def send_email():
    global message
    message="Hi"
    print("Email Sent")


print(message)
greet("Zartab")
print(message)
send_email()
print(message)

# --------------- Python doesn't support block scope

def some_func():
    for number in range(1,6):
        print(number)

    print("Number",number)

some_func()