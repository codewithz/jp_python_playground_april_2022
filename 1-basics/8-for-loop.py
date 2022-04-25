for number in range(3):
    print("Attempt",(number+1),(number+1)*'.')

# -----------------------------------------------
print("-"*40)

for number in range(1,5):
    print("Attempt",(number),(number)*'.')

print("-"*40)

# for..else

successful=False

for number in range(1,6):
    print("Attempting to send a message")
    if number==2 and successful:
        print("Message send successfully!!")
        break
else:
    print("Attempted for 5 times and failed")
# else after for .. will be executed only if the for loop completed
# without breaking