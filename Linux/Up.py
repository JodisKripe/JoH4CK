#Program to check if a destination is up. It can Notify you by performing any action.
import os

def up(IP):
    command="ping -c 1 "+IP+">up.txt"
    os.system(command)
    while True:
        with open("up.txt")as dope:
            listt=dope.read().split()
            #print(listt)
            if(listt[8]=="bytes"):
                print("UP")
                break
            else:
                pass

#up("8.8.8.8")



def main():
    IP=input("Enter IP: ")
    up(IP)
    os.system("rm up.txt")

main()
