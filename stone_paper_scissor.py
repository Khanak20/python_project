import random
a = 'stone'
b = 'paper'
c = 'scissor'
d = 'stone' , 'paper' , 'scissor'
def QUES():
    e = input("STONE , PAPER OR SCISSOR : ")
    e.lower()
    comp = random.choice(d)
    print(comp)

    if (e == a and comp == b) or (e == b and comp == c) or (e == c and comp == a):
        print('Computer is winner.') 
    elif (e == a and comp == c) or (e == b and comp == a) or (e == c and comp == b):
        print('You are winner.') 
    elif e == comp:
        QUES()

    QUES()    
QUES()  


