from time import sleep
#a function to convert list to integer
def integer(a):
    strings = [str(integer) for integer in a]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer
#a function to rotate list
def rotate(a,n):
    #rotating the list
    for i in range(n):
        temp=a[0]
        a.append(temp)
        a.pop(0)
    return a
#a function to ccheck if a number is prime
def is_prime(x):
    status=True
    x=int(x)
    for i in range(2,x,1):
        if x % i==0:
            status=False
    return status
#a function to chck if number is a circular prime
def is_circular(x):
    status=True
    x=list(x)
    for i in range(len(x)):
        if is_prime(integer(x)):
            x=rotate(x,i)
            continue
        else:
            return False
    return status
a=input('Enter a number to check if its a circular prime : ')
print('{} is a circular prime : {}'.format(a,is_circular(a)))
sleep(10)       
        
        
    
