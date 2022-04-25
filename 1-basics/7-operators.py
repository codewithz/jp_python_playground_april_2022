# and
# or
# not

# Loan Processing System

high_income=True
good_credit=False
student=True
print(40*'-')
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# -----------------------------------------
print(40*'-')

if(high_income or good_credit) and student:
    print("eligible")
else:
    print("not eligible")

# ------------------Ternary Operator----------------------------

print(40*'-')

age=19
#
# message=''
#
# if age>=18:
#     message="Eligible Age"
# else:
#     message="Not Eligible Age"

message="Eligible Age" if age>=18 else "Uneligible Age"

print("Age",age,"| ",message)

# ----------Chaining Comparison Operatar--------------------------------------------
print(40*'-')
# age should be between 18 and 65

#
# if age>=18 and age<=65:
#     print("Eligible")

if 18<= age <= 65:
    print("Eligible from Chained Operator")













