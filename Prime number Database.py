import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='maou4514',database='NUMBERS')
cursor=mydb.cursor()

#prime function
def prime_check(num):
    stat=True
    for i in range(2,num-1):
        if num%i==0:
            stat=False
            break
        else:
            stat=True
    tup=num,stat
    return tup
#input
num=int(input("Enter num :"))
entree=prime_check(num)
#check
cursor.execute("SELECT * FROM numbers")
in_db=True
for i in cursor:
    if entree==i:
        print('Found' , i)
        in_db=True
        break
    else:
        in_db=False
if in_db==False:
    print('not found in database adding :',entree)
    cursor.execute("INSERT INTO numbers(numbers,prime) VALUE(%s,%s)",entree )    
    mydb.commit()
#cursor.execute("CREATE TABLE numbers(numbers int unsigned,prime bool)")

