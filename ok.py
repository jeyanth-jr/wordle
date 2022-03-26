import random
import numpy as np
import colorama
from colorama import Fore
from colorama import Style
colorama.init()
f=open("5 letter word file.txt","r")
r=f.readlines()
a=random.choice(r)
g=1
flag=0
print("Enter a 5 letter word")
while(g<=5):
    b=str(input())
    if len(b)==5:
        for i in range(0,5):
                if(a[i]==b[i]):
                    print(Fore.GREEN  + b[i].upper() + Style.RESET_ALL,end="")
                    flag=flag+1
                elif b[i]==a[0] or b[i]==a[1] or b[i]==a[2] or b[i]==a[3] or b[i]==a[4]:
                    print(Fore.YELLOW + b[i].upper() + Style.RESET_ALL,end="")
                    flag=flag+0
                else:
                    print(Fore.RED +  b[i].upper() + Style.RESET_ALL,end="")
                    flag=flag+0            
        if flag==5:
            print("Congrats!!!")
            exit()
        flag=0
        g=g+1                
    else:
        print("enter 5 letter word")
print("You completed 5 tries")        