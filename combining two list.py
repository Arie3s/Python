#write a function that takes two list and makes a new list by taking elements alternatively
#[a,b,c] ,[1,2,3] = [a,1,b,2,c,3]
def newlist(lista,listb):
    new=[]
    n=len(listb)
    for i in range(n):
        new.append(lista[i])
        new.append(listb[i])
    return new
alist=['a','b','c','d']
blist=[1,2,3,4]
print(alist)
print(blist)
print(newlist(alist,blist))
