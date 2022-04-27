try:
    with open("1-exceptions.py") as source,open("2-exception-handling.py") as target:
        x=10/1
        print("Value of x is",x)
        print("Source Inside with block | Is file closed?:",source.closed)
        print("Target Inside with block | Is file closed?:",target.closed)
        print("_"*20,"With block ends here",20*'_')


    print("Source Outside with block | Is file closed?:",source.closed)
    print("Target Outside with block | Is file closed?:",target.closed)
except Exception as ex:
    print("Some exception occurred")



print("\n\n Execution Continues...")