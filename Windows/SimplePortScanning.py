#Basic nMap
import socket
import os

PortList=[20,22,23,80,110,443,]

def PScan(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      #s.shutdown(2)
      return str(port) + " is open on " + ip
   except:
      return str(port) + " is down"


def BasicScan(IP):
    os.system("cls")
    for i in PortList:
        print(PScan(IP,i))
    jar=input()

IP=input("Enter IP to scan for mostly open ports:")
#BasicScan(IP)


def mainMenu():
    os.system("cls")
    global PortList
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
while True:
    mainMenu()
bar=input()

