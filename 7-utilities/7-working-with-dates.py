from datetime import datetime
import time

dt1=datetime(2022,4,25)
print(dt1)

dt2=datetime.now()
print(dt2)

incoming_date='23/04/2021'
print("Original:",incoming_date)
dt3=datetime.strptime(incoming_date,"%d/%m/%Y")
print("Formatted:",dt3)

dt4=datetime.fromtimestamp(time.time())
print(dt4)

print("Date",dt2)
print("Formatted Date:",dt2.strftime("%d/%m/%Y"))