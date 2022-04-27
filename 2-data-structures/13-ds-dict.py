# Dictionary
# Key-Value Pairs
#  {key:value}
#  Contact Book  Name-> Contact Number

print("_"*40)
point={"x":1,"y":2}
print(point)
print(type(point))

print("_"*40)

point=dict(x=1,y=2)
print(point)
print(type(point))

print("_"*40)

point["x"]=10
point["y"]=20
point["z"]=30

print(point)

print("_"*20,"Accessing the Data","_"*20)

print("X",point.get("x"))
print("A",point.get("a"))
print("A",point.get("a",0))

if "a" in point:
    print(point.get("a"))

print("_"*40)
for something in point:
    print(something)

print("_"*40)
for key in point:
    print(key)

print("_"*40)
for item in point.items():
    print(item)

print("_"*40)
for key,value in point.items():
    print(key,"-",value)

values_list=point.values()

for value in values_list:
    print(value)

print(values_list)
