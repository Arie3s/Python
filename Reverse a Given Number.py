#Write Python Program to Reverse a Given Number
num=input("Enter a number")
num1=int(num)
revnum=0
while num1>00:
    temp=num1%10
    num1=num1//10
    revnum=(revnum*10)+temp
print(revnum)     
    
