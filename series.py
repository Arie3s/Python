#4,16,37,58,89,145,42,20
#add sum of each digit's square to get the next number
#AE000216 Series encyclopedia
# Python3 program to Split string into characters
def series(n):
    number='2'
    for i in range(n):
        n=0
        intList=list(number)
        for i in intList:
            n=n+(int(i)**2)
        print(n,end=',')
        number=str(n)
num=int(input('Enter the number of terms :'))
series(num)
