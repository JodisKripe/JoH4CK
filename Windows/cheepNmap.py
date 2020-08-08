#CheepNmap
import os
import time

def gen(BaseIp , Range):
    global esto , endo ,bint, glorange
    glorange=Range
    #esto = start
    #endo = stop
    bint = BaseIp
    for i in Range:
        filename="Scan/nmap"+str(i)+".py"
        with open(filename,"w+") as dope:
            command="import os\n\nos.system(\"ping -n 1 -w 10 " + BaseIp + "." + str(i) + " > Scan/RES/" + str(i) + ".txt\")"
            dope.write(command)

def doIt():
    for i in glorange:
        command="python ./Scan/nmap"+str(i)+".py"
        os.system(command)

def check():
    print("\n\n")
    for i in glorange:
        filename="./Scan/RES/"+str(i)+".txt"
        with open(filename,"r") as yo:
            lines=yo.read().split()
            if("bytes=" in lines[10]):
                output=bint + "." + str(i) + " is UP and Scannable\n"
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
        seyt=[]
        baseip=input("Enter base ip(eg. 192.168.0): ")
        option=int(input("\nEnter the way you want to select the range:\n1.Give them Individual Separated by space\n2.Starting and Ending Range\n3.Default(0-255)\n"))
        if(option == 1):
        	seyt=input("Give the last part of the address individually:\n").split()
        	os.system('cls')
        elif(option == 2):
	        RangeStart=int(input("Enter starting of range: "))
	        RangeEnd=int(input("Enter Ending of range: "))
	        for i in range(RangeStart,RangeEnd+1):
	        	seyt.append(i)
	        os.system("cls")
        elif(option==3):
            for i in range(0,256):
                seyt.append(i)
            os.system("cls")
        
        gen(baseip , seyt)
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
