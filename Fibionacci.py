
test=False
while test==False:
    num=input("enter number :")
    for i in num:
        test=ord(i)>40 and ord(i)<58
        if test==False:
            print("enter an integer only")
if test==True:
    t1=0
    t2=1
    c=0
    for i in range(1,int(num)+1):
            print(t1)
            c=t1+t2
            t1=t2
            t2=c
            
    
