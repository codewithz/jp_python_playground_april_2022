numbers=[3,51,2,45,8,67]
print("O:",numbers)

numbers.sort()
print("S:",numbers)
print("O:",numbers)

numbers.sort(reverse=True)
print("RS:",numbers)
print("O:",numbers)

# ---------------------------------------------------------
print(40*'-')

other_numbers=[43,65,34,0,23,89]
print("O:",other_numbers)

sorted_list=sorted(other_numbers)
print("S:",sorted_list)
print("O:",other_numbers)

reverse_sorted_list=sorted(other_numbers,reverse=True)
print("RS:",reverse_sorted_list)
print("O:",other_numbers)