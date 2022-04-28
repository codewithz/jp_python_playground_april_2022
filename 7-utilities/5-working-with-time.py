import time

print(time.time())

def some_function():
    for x in range(100000):
        print(x)

# ----------------------------------

start=time.time()
some_function()
end=time.time()

print("Duration",(end-start))