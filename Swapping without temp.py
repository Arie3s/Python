#2.	Write Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a=5
b=7
print("before swap\na={} , b={}".format(a,b))
a=a+b
b=abs(a-b)
a=abs(a-b)
print("After Swap\na={} , b={}".format(a,b))
