class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee,Person):
    pass

m=Manager()
m.greet()
# -------------------------------------------------------------
print("_"*40)

class Flyer:
    def fly(self):
        print("Fly")

class Swimmer:
    def swim(self):
        print("Swim")



class FlyingFish(Flyer,Swimmer):
    pass

ff=FlyingFish()
ff.fly()
ff.swim()