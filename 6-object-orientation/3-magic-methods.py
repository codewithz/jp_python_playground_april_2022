name="Zartab"

print(dir(name))
print(40*"-")

o=object()
print(dir(o))


print(40*"-")
print(isinstance(name,object))



#  __some_method__ --> considered as magic method

# https://rszalski.github.io/magicmethods/
print(40*"-")

class Point:
    def __init__(self,x,y):
        print("Point Constructor")
        self.x=x
        self.y=y
    def __str__(self):
        return f"Point({self.x},{self.y})"

# ------------------------------------------------

p=Point(5,6)
print(p)