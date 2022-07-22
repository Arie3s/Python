import array as arr

#page 1 rows
row1=arr.array('i',[1,2,3])
row2=arr.array('i',[3,4,5])
row3=arr.array('i',[6,7,8])
#page 2 rows
row4=arr.array('i',[11,12,13])
row5=arr.array('i',[23,24,25])
row6=arr.array('i',[36,37,38])
#pages 
page_1=[row1,row2,row3]
page_2=[row4,row5,row6]
pages=[page_1,page_2]

#variable intialization
row,col,depth=len(page_1),len(row1),len(pages)
#for loop for manipulating array
for k in range(depth):
    for j in range(row):
        for i in range(col):
            #[page][row][column]
            pages[k][j][i]=i+j+k
       
                      

for k in range(depth):
    for j in range(row):
        for i in range(col):
            print(pages[k][j][i],end=',')
        print('\n')
    print('\n')

