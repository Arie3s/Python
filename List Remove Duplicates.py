'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
def dupli_rem(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
        else:
            pass
    return b

a=[]
n=int(input("Enter number of numbers :"))
for i in range(n):
    c=int(input("Enter element :"))
    a.append(c)
d=dupli_rem(a)
d.sort()
print(d)
