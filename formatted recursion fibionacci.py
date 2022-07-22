def fib(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fib(num-2)+fib(num-1)


num=int(input("Enter number :"))
if num<=30:
    print("position | Sequence")
    for i in range(1,num+1):
        print("{:<9}|      {:<6}".format(i,fib(i)))
else:
    print("  Warning long time required")
        
    
