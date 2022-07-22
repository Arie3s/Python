import os
# import sleep to show output for some time period
from time import sleep  
# define our clear function
def clear():
    _=os.system("cls")
def one():
    print('    o    ')
    print()
    print()
    print()
    print('---------')
def two():
    print()
    print('    o    ')
    print()
    print()
    print('---------')
def three():
    print()
    print()
    print('    o    ')
    print()
    print('---------')
def four():
    print()
    print()
    print()
    print('    o    ')
    print('---------')
def delay():
    sleep(0.05)
    os.system("cls")
  
cond=True
while    cond==True:
    one()
    delay()
    two()
    delay()
    three()
    delay()
    four()
    delay()
    three()
    delay()
    two()
    delay()
    one()
    delay()
