class Point:
    color="Yellow"
    def __init__(self,abc,xyz):
        print("Point Constructor")
        self.x=abc
        self.y=xyz

    def draw(self):
        print(f"Point({self.x},{self.y})")
        self.z=30
        self.x=self.x*20

    def draw_more(self):
        print("Draw More")
        print(f"Point({self.x},{self.y},{self.z})")

# --------------------------------------------------

print(40*"-")
print(Point.color)

print(40*"-")
p=Point(3,4)
p.draw()
p.draw_more()
print(p.color)
p.color="Red"
print(p.color)

print(40*"-")
p1=Point(5,6)
p1.draw()
p1.draw_more()
print(p1.color)