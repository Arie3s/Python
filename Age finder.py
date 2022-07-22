from datetime import date
import math
dob=input("enter date of birth")
indexd=dob.find('/')

indexm=dob.find('/',indexd+1)

day=(int(dob[indexd-2])*10)+int(dob[indexd-1])
print(day)
month=(int(dob[indexm-2])*10)+int(dob[indexm-1])
print(month)
year=(int(dob[indexm+1])*1000)+(int(dob[indexm+2])*100)+(int(dob[indexm+3])*10)+int(dob[indexm+4])
print(year)
today=date.today()
agey= today.year-year
agem=today.month-month-1
aged=today.day+(30-day)

print('%d years %d months %d days'%(agey,abs(agem),abs(aged)))
