import array as arr
rows=2
page=2
row=arr.array('i',[0,0,0])
#pages 
pages=[[0]*rows]*page
#for loop for manipulating array

for k in range(page):
    for j in range(rows):
            #[page][row][column]
        for i in range(3):
            row[i]=int(input("Enter element"))            
        pages[k][j]=row
                             
for j in range(page):
    for i in range(rows):
        print(pages[j][i])
    print('\n\n')




