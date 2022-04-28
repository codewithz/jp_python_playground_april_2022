# functions and variables --> Snake Casing --> one_two_three_four
# Class  -------------------> Pascal Casing--> OneTwoThreeFour


class Point:
    def draw(self):
        self.x=10
        print("Draw")

# --------------------------------------------------

p=Point()
p.draw()
print(p.x)
print(type(p))

i=20

print(isinstance(i,int))
print(isinstance(p,int))
print(isinstance(p,Point))
print(isinstance(p,int))

