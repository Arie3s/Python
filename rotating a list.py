#rotating the list
def rotate(list,n):
    for i in range(n):
        temp=a[0]
        list.append(temp)
        list.pop(0)
    return list
#intialising a list

a=[]
n=int(input('Enter the number of elements in list :'))
#taking a input into list
for i in range(n):
    inp=input('Enter element :')
    a.append(inp)
#taking the input for how to rotate the list by
n=int(input('Enter  number to rotate the list by :'))
#orignal list
print('Orignal list :{}'.format(a))
#printing the rotated list
print('Rotated list :{}'.format(rotate(a,n)))
