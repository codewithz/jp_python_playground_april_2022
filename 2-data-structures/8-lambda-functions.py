cart=[("Bread",5),("Butter",7),("Jam",4)]
print("Cart:",cart)

# def sort_cart(item):
#     return item[1]
#
# sorting_key=lambda item:item[1]

cart.sort(key=lambda item:item[1])
print("Cart",cart)
# --------------------------------------------
print(40*'-')
# Traditional Way

prices=[]

for name,price in cart:
    prices.append(price)

print("Prices",prices)

x=list(map(lambda item:item[1],cart))
print("Price using Lambda",x)

# -----------------------------------------

print(40*'-')

filtered_cart=[]

for item in cart:
    name,price=item
    if price>=5:
        filtered_cart.append(item)

print("Filtered Cart",filtered_cart)

y=list(filter(lambda item:item[1]>=5,cart))
print("Filtered using Lambda",y)
