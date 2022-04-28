class Animal:
    def eat(self):
        print("Eat")

class Bird(Animal):
    def fly(self):
        print("Fly")

# -----------------------------------------------
# Animal --> Bird --> Eagle
# Animal --> Bird --> Chicken

# -----------------------------------------------
class Eagle(Bird):
    pass
# ----------------------------------------------
class Chicken(Bird):
    pass
# ---------------------------------------------

e=Eagle()
e.eat()
e.fly()

c=Chicken()
c.eat()
c.fly()