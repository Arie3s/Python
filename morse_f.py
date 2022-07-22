#morse code
#Automatically convert morse code into english and viceversa
def split(word):
    return [char for char in word]

def morse(string):
    string=string.lower()
    test=split(string)
    out=''
    for i in test:
        if i=='e' or i=='a'or i=='i'or i=='s'or i=='u'or i=='r'or i=='w'or i=='h'or i=='v'or i=='f'or i=='l'or i=='p'or i=='j':
            out=out+'.'
            if i=='i'or i=='s'or i=='u'or i=='h'or i=='v'or i=='f':
                out=out+'.'
                if  i=='s'or i=='h'or i=='v':
                    out=out+'.'
                    if i=='h':
                        out=out+'.'
                    elif i=='v':
                        out=out+'-'
                elif i=='u' or i=='f':
                    out=out+'-'
                    if i=='f':
                        out=out+'.'
            elif i=='a'or i=='r'or i=='w'or i=='l'or i=='p'or i=='j':
                out=out+'-'
                if i=='w'or i=='p'or i=='j':
                    out=out+'-'
                    if i=='j':
                        out=out+'-'
                    elif i =='p':
                        out=out+'.'
                elif i=='r' or i=='l':
                    out=out+'.'
                    if i=='l':
                        out=out+'.'
        elif i=='t'or i=='n'or i=='m'or i=='d'or i=='k'or i=='g'or i=='o'or i=='b'or i=='x'or i=='c'or i=='y'or i=='z'or i=='q':
             out=out+'-'
             if i=='n'or i=='d'or i=='k'or i=='b'or i=='x'or i=='c' or i=='y':
                 out=out+'.'
                 if i=='d'or i=='b'or i=='x':
                     out=out+'.'
                     if i=='b':
                         out=out+'.'
                     elif i=='x':
                         out=out+'-'
                 elif i=='k'or i=='c'or i=='y':
                     out=out+'-'
                     if i=='c':
                         out=out+'.'
                     elif i=='y':
                         out=out+'-'
        
             elif i=='m'or i=='g'or i=='o'or i=='z'or i=='q':
                 out=out+'-'
                 if i=='g'or i=='z'or i=='q':
                     out=out+'.'
                     if i=='z':
                         out=out+'.'
                     elif i=='q':
                         out=out+'-'
                 elif i=='o':
                     out=out+'-'
        out=out+'   '
    return out
def sentence(string):
    words=string.split(' ')
    code=[]
    for i in words:
        code.append(morse(i))
        code.append(' // ')
    return code
def eng(string):
    letter=split(string)
    out=''
    n=len(letter)
    if n==1:
        if letter[0] == '.':
            out+='e'
        else:
            out+='t'
    elif n==2:
         if letter[0] == '.':
            if letter[1]=='.':
                out+='i'
            else:
                out+='a'
         else:
            if letter[1]=='.':
                out+='n'
            else:
                out+='m'

    elif n==3:
         if letter[0] == '.':
            if letter[1]=='.':
                if letter[2]=='.':
                    out+='s'
                else:
                    out+='u'
            else:
                if letter[2]=='.':
                    out+='r'
                else:
                    out+='w'
         else:
            if letter[1]=='.':
                if letter[2]=='.':
                    out+='d'
                else:
                    out+='k'
            else:
                if letter[2]=='.':
                    out+='g'
                else:
                    out+='o'
        
    elif n==4:
         if letter[0] == '.':
            if letter[1]=='.':
                if letter[2]=='.':
                    if letter[3]=='.':
                        out=out+'h'
                    else:
                        out=out+'v'
                else:
                    out+='f'
            else:
                if letter[2]=='.':
                    out+='l'
                else:
                    if letter[3]=='.':
                        out+='p'
                    else:
                        out+='j'
         else:
            if letter[1]=='.':
                if letter[2]=='.':
                    if letter[3]=='.':
                        out+='b'
                    else:
                        out+='x'
                else:
                    if letter[3]=='.':
                        out+='c'
                    else:
                        out+='y'
            else:
                if letter[3]=='.':
                    out+='z'
                else:
                    out+='q'
    return out


select=int(input("1.English to Morse\n2.Morse to English \nselection: "))
if select==1:
    string=input("Enter a string")
    ans=sentence(string)
    for i in ans:
        print(i,end='')
elif select==2:
    sentence=input("Enter morse :")    
    words=sentence.split(' ')
    for i in words:
        print(eng(i),end=' ')
