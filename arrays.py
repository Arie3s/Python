import array as arr
#page 1 rows
row1=arr.array('i',[1,2,3])
row2=arr.array('i',[3,4,5])
row3=arr.array('i',[6,7,8])
#page 2 rows
row4=arr.array('i',[11,12,13])
row5=arr.array('i',[23,24,25])
row6=arr.array('i',[36,37,38])
#page 3 rows
row7=arr.array('i',[0,0,0])
row8=arr.array('i',[0,0,0])
row9=arr.array('i',[0,0,0])
#pages 
page_1=[row1,row2,row3]
page_2=[row4,row5,row6]
page_3=[row7,row8,row9]
pages=[page_1,page_2,page_3]

#variable intialization
row,col,depth=len(page_1),len(row1),2
print("""         3x3 Matrix Addition
          |1 2 3|   |1 2 3|
          |4 5 6| + |4 5 6| 
          |7 8 9|   |7 8 9|
                     """)
#for loop for manipulating array
for k in range(depth):
    print("Enter the matrix elememts for {} 3 x3 Matrix".format(k+1))
    for j in range(row):
        for i in range(col):
            #[page][row][column]
            pages[k][j][i]=int(input("Enter element :"))
       
#for loop for addition
for j in range(row):
    for i in range(col):
        pages[2][j][i]=pages[0][j][i]+pages[1][j][i]
                      
for j in range(row):
    for i in range(col):
        print(pages[2][j][i],end=',')
    print('\n')


