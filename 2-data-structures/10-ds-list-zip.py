list1=[1,2,3,4,5]
list2=[10,20,30,40]

[(1,10),(2,20)]

zipped_list=list(zip(list1,list2,"abcd"))

print(zipped_list)
print(40*'-')
names=["Tom","Alex","Ricky","Leanord","Sheldon"]
len_list=[len(name) for name in names]

zipped_name_length=list(zip(names,len_list))
print(zipped_name_length)