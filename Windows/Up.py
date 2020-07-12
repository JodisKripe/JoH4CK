import os
import time
def up(IP):
    string="ping "+IP+" > pingRes.txt"
    os.system(string)
    global stat
    stat="down"
    with open("pingRes.txt","r") as op:
        string=op.read().split()
        if(string[7]=="Reply"):
            print("UP")
            stat="up"
        else:
            pass

ip=input("IP:")
stat="down"
while(stat=="down"):
    up(ip)

os.system("del pingRes.txt")




