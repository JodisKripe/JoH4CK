#CheepNMAP

import os
import time

def gen(BaseIp , start , stop):
    global esto , endo ,bint
    esto = start
    endo = stop
    bint = BaseIp
    for i in range(start,stop):
        filename="Scan/nmap"+str(i)+".py"
        with open(filename,"w+") as dope:
            command="import os\n\nos.system(\"ping -n 1 -w 10 " + BaseIp + "." + str(i) + " > Scan/RES/" + str(i) + ".txt\")"
            dope.write(command)

def doIt():
    for i in range(esto, endo):
        command="python ./Scan/nmap"+str(i)+".py"
        os.system(command)

def check():
    print("\n\n")
    for i in range(esto, endo):
        filename="./Scan/RES/"+str(i)+".txt"
        with open(filename,"r") as yo:
            lines=yo.read().split()
            if("bytes=" in lines[10]):
                output=bint + "." + str(i) + " is UP and Scannable"
                print(output)
            #print(lines)
            #print(lines[7])

'''ip="192.168.0"
n=13
gen(ip,n)

check()
'''

def initialize():
    try:
        os.system("mkdir Scan")
        os.system("md Scan\\RES")
    except:
        pass

def cleanup():
    os.system("rd /Q /S Scan")

def dope():
    if (__name__=="__main__"):
        initialize()
        baseip=input("Enter base ip(eg. 192.168.0): ")
        RangeStart=int(input("Enter Starting of range: "))
        RangeEnd=int(input("Enter Ending of range: "))
        os.system("cls")
        gen(baseip , RangeStart , RangeEnd)
        doIt()
        check()
        cleanup()
        pewds=input("\n\nFinished")

dope()

#cleanup(100,125)
#doIt(125)



'''dat=112
bint="192.168.0"
'''



"""
for i in range(4):
    command="import os\n\nos.system(\"ping " + "192.168.0" + "." + str(i) + " > Scan/RES/" + str(i) + ".txt\")"
    print(command)
    filename = "nmap" + str(i) + ".py"
    print(filename)
    
"""
