#Write Python Program to Convert Decimal to Binary, Octal and Hexadecimal and vice versa without using built in functions.
def dectobin(num):
    test=[0,0,0,0,0,0,0,0]
    for j in range(8,0,-1):
         test[j-1]=num%2
         num=num//2
    return test
def bintodec(num):
    dec=0
    j=7
    for i in num:
        temp=i*(2**j)
        dec+=temp
        j-=1
    return dec
tf=[0, 0, 1, 1, 1, 0, 0, 0]
print(dectobin(56))
print(bintodec(tf))
           
           
                
