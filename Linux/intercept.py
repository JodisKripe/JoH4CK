import os

while True:
    os.system("cat up.txt 2>/dev/null > dope.txt")
    with open("dope.txt","r")as file:
        listt=file.read().split()
        if(listt!=[]):
            print(listt)
            os.system("rm dope.txt")
            break
        else:
            continue

