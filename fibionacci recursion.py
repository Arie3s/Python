def fib(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fib(num-2)+fib(num-1)


num=int(input("Enter number"))
for i in range(1,num+1):
    print(fib(i),end=" ")
    
        
    
