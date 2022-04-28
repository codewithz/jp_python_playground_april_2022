class Product:
    def __init__(self,name,price):
        self.name=name
        self.set_price(price)

    def set_price(self,value):
        print("Set Price is called")
        if value<=0:
            raise ValueError("Price cannot be 0 or less")
        else:
            self.__price=value

    def get_price(self):
        print("Get Price is called")
        return self.__price

    def __str__(self):
        return f"Product Name: {self.name} | Price: {self.__price}"

    price=property(get_price,set_price)

# --------------------------------------------------------------------
try:

    pr1=Product("Earphones",-300)
    print(pr1)
    pr1.price=-450
    print(pr1)
    print(pr1.price)
except ValueError as ex:
    print(ex)

print(40*"-")

pr2=Product("Keyboard",700)
print(pr2)