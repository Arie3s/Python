#Automatically convert morse code into english and viceversa
def split(word):
    return [char for char in word]
cypher=         {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....',
                       'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..','m' : '--','n' : '-.','o' : '---','p' : '.--.',
                       'q' : '--.-','r' : '.-.','s' : '...','t' : '-','u' : '.--','v' : '...-','w' : '.--','x' : '-..-',
                       'y' : '-.--','z' : '--..'}
decypher=      {'.-' : 'a', '-...' : 'b', '-.-' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h',
                       '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l','--' : 'm','-.' : 'n','---' : 'o','.--.' : 'p',
                       '--.-' : 'q','.-.' : 'r','...' : 's','-' : 't','.--' : 'u','...-' : 'v','.--' : 'w','-..-' : 'x',
                       '-.--' : 'y','--..' : 'z'}
def morse(string):
    text=list(string)
    out=''
    for i in text:
        out+=cypher[i]+'  '
    return out
def eng(string):
    code=string.split()
    out=''
    for i in code:
        out+=decypher[i]
    return out    

n=input('1.Morse to english\n2.English to Morse\nSelection: ')
if n=='1':
    msg=input('Enter morse code : ')
    print(eng(msg))
elif n=='2':
    msg=input('Enter text: ')
    print(morse(msg))
