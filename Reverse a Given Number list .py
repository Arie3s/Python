#Write Python Program to Reverse a Given Number
num=input("Enter a number")
num1=num[::-1]
rev=0
#making reversed list usable integer
for i in range(len(num1),0,-1):
    rev=rev+(int(i)*pow(10,i-1))
#reversing list for display
print(num1)
#printing reversed variable
print(rev)

    
    
