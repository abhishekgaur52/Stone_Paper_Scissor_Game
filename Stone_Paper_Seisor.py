# STONE PAPER SEISOR GAME

'''
0 = Stone
1 = Paper
2 = seisor

'''
print("0 = Stone")
print("1 = Paper")
print("2 = seisor")


import random
computer =random.choice([0,1,2])
you = int(input("ENTER YOUR NUMBER:"))
dict = {0:"stone",1:"paper",2:"seisor"}
print(f"you choose: {dict[you]}\ncomputer choose: {dict[computer]}")



if(you==0 and computer==1):
    print("YOU WIN")
elif(you==1 and computer==2):
    print("YOU WIN")
elif(you==2 and computer==0):
    print("YOU WIN")
elif(you==2 and computer==1):
    print("YOU LOOSE")
elif(you==0 and computer==2):
    print("YOU LOOSE")
elif(you==1 and computer==0):
    print("YOU LOOSE")
elif(you == computer):
    print("GAME DRAW")
else:
    print("something went wrong")
    
    

