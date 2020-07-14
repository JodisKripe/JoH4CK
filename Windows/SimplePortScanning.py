#Basic nMap
import socket
import os
import multiprocessing
'''from testing import *'''
PortList=[20,22,23,80,110,443]

def PScan(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #print("running")
   try:
        s.connect((str(ip), int(port)))
   #s.shutdown(2)
        print(str(port) + " is open on " + ip)
   except:
      print(str(port) + " is down")
#PScan("50.62.117.19",22)
#PScan("50.62.117.19",22)



TIMEOUT=0.5

def BasicScan(iP):
    for i in PortList:
        #print(__name__)
        if (__name__ == "__main__"):
            #print("bef")
            p = multiprocessing.Process(target=PScan, name="PScan", args=(iP,i))
            #print(iP,i)\
            p.start()
            #print("running")
            p.join(TIMEOUT)

            if (p.is_alive()):
                #print('port', i, "closed on",iP)
                p.terminate()
                p.join()
    jar=input()

#IP=input("Enter IP to scan for mostly open ports:")
#BasicScan(IP)

def mainMenu():
    if(__name__=="__main__"):
        #print(__name__)
        os.system("cls")
        global IP
        IP =input("Enter IP to scan for mostly open ports:")
        global PortList
        PortList = [20, 22, 23, 80, 110, 443]
        portCh = input("Most Used Ports(M)\nCustom Ports Listing(C)\nRange(R)\n\n")
        if(portCh.lower()=="m"):
            BasicScan(IP)
        elif(portCh.lower()=="c"):
            PortList=input("Enter the individual ports with spacing:\n").split()
            print(PortList)
            BasicScan(IP)
        elif(portCh.lower()=="r"):
            st=int(input("Starting:"))
            en=int(input("Ending:"))
            PortList=[]
            for i in range(st,en+1):
                PortList.append(i)
            BasicScan(IP)
        else:
            print("Invalid")
if (__name__=="__main__"):
    #print("runnn")
    mainMenu()
