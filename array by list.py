import array as arr
row,col,depth=2,3,3
arr=[[[0]*col]*row]*depth
#[col][row][depth]
for k in range(depth):
    for j in range(row):
        for i in range(col):
            arr[k][j][i]=i+j+k
       
                      

for k in range(depth):
    for j in range(row):
        for i in range(col):
            print(arr[k][j][i],end=',')
        print('\n')
    print('\n')


print(arr)
