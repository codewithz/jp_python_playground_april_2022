values=[]

for x in range(1,6):
    values.append(x*2)

print(values)

# [expression for item in items]

values=[value*2 for value in range(1,6)]
print(values)

print(20*'-',"Dictionary Comprehension",20*'-')

# {key:value for item in items}

value_dict={x:x*3 for x in range(1,11)}
print(value_dict)

value_dict={"A"+str(x):x*3 for x in range(1,11)}
print(value_dict)