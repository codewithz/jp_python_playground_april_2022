cart=[("Bread",5),("Butter",7),("Jam",4)]
print("Cart:",cart)

# [expression for item in items]

prices=list(map(lambda item:item[1],cart))
print("Prices",prices)

prices_lc=[item[1] for item in cart]
print("LC",prices_lc)

filtered_list=list(filter(lambda item:item[1]>=5,cart))
print("Filtered",filtered_list)

# [expression for item in items if condition]

filtered_lc=[item for item in cart if item[1]>=5]
print("Filtered LC:",filtered_lc)

names=["Tom","Alex","Ricky","Leanord","Sheldon"]

len_list=[len(name) for name in names]

print("Names",names)
print("Length",len_list)

filtered_names=[name for name in names if len(name)>=5]

print("Filtered:",filtered_names)
# ------------------------------------------------------------------------------------------
employees=[
    (1,"Tom","IT",30000),
    (2,"Alex","Accounts",33000),
    (3,"Mike","Finance",43000),
    (4,"John","HR",39000),
    (5,"Penny","IT",45000)
]

#  Q1 -- Find the list of departments in employees list
# Q2 -- find those employees whose salary is greater than 32k and work in IT


dept_list=[employee[2] for employee in employees]
print(dept_list)

filtered_emp=[employee for employee in employees if (employee[2]=='IT' and employee[3]>32000)]
print(filtered_emp)