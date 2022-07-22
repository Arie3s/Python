import  os
from time import sleep
#win check
cond=True
#grid coordinates
a=[     [1,2,3],
          [4,5,6],
          [7,8,9]
        ]
#displaying the grid
def grid():
    print('   {}   |   {}   |   {}'.format(a[0][0],a[0][1],a[0][2]))
    print('   --------------')
    print('   {}   |   {}   |   {}'.format(a[1][0],a[1][1],a[1][2]))
    print('   --------------')
    print('   {}   |   {}   |   {}'.format(a[2][0],a[2][1],a[2][2]))
#updating the list elements
def update(p,index):
    i=index[0]
    j=index[1]
    if p=='p1':
        a[i][j]='x'
    else:
        a[i][j]='O'
#adding in delay
def delay():
    sleep(1)
    os.system('cls')
#assigng box number coordinates    
def assign(n):
    n=int(n)
    coord=[]
    if n==1:
        coord=[0,0]
    elif n==2:
        coord=[0,1]
    elif n==3:
        coord=[0,2]
    elif n==4:
        coord=[1,0]
    elif n==5:
        coord=[1,1]
    elif n==6:
        coord=[1,2]
    elif n==7:
        coord=[2,0]
    elif n==8:
        coord=[2,1]
    elif n==9:
        coord=[2,2]
    return coord
#checking winning conditions
def win():
    temp=None
    if (a[0][0]==a[0][1] and a[0][1]==a[0][2]) or (a[1][0]==a[1][1] and a[1][1]==a[1][2])or(a[2][0]==a[2][1] and a[2][1]==a[2][2]):
        temp=False
    elif (a[0][0]==a[1][0] and a[1][0]==a[2][0]) or (a[0][1]==a[1][1] and a[1][1]==a[2][1])or(a[0][2]==a[1][2] and a[1][2]==a[2][2]):
        temp=False
    elif (a[0][0]==a[1][1] and a[1][1]==a[2][2]) or (a[0][2]==a[1][1] and a[1][1]==a[2][0]):
        temp=False
    return temp
#checking whick player won
def win_check():
    if (a[0][0]=='x' and a[0][1]==a[0][0] and a[0][2]==a[0][0])or(a[1][0]=='x' and a[1][1]==a[1][0] and a[1][2]==a[1][0])or(a[2][0]=='x' and a[2][1]==a[2][0] and a[2][2]==a[2][0]) :
        print('Player One wins!!')
    elif (a[0][0]=='O' and a[0][1]==a[0][0] and a[0][2]==a[0][0])or(a[1][0]=='O' and a[1][1]==a[1][0] and a[1][2]==a[1][0])or(a[2][0]=='O' and a[2][1]==a[2][0] and a[2][2]==a[2][0]) :
        print('Player Two wins!!')
    elif (a[0][0]=='x' and a[0][0]==a[1][1] and a[1][1]==a[2][2]) or (a[0][0]=='x' and a[0][2]==a[1][1] and a[1][1]==a[2][0]):
        print('Player One wins!!')
    elif (a[0][0]=='O' and a[0][0]==a[1][1] and a[1][1]==a[2][2]) or (a[0][0]=='O' and a[0][2]==a[1][1] and a[1][1]==a[2][0]):
        print('Player Two wins!!')
 #main program loop             
while cond==True:
    if win()==False:
        os.system('cls')
        grid()
        win_check()
        delay()
        break
    grid()
    p1=input('Player 1 enter box  :')
    update('p1',assign(p1))
    if win()==False:
        os.system('cls')
        grid()
        win_check()
        delay()
        break
    os.system('cls')
    grid()
    p2=input('Player 2 enter box :')
    update('p2',assign(p2))
    if win()==False:
        os.system('cls')
        grid()
        win_check()
        delay()
        break
    os.system('cls')

