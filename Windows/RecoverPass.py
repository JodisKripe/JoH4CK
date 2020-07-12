import os

os.system("netsh wlan show profiles")

def passRec(wlan0):
    command="netsh wlan show profile "+wlan0+" key=clear > temp.txt"
    os.system(command)
    with open("temp.txt","r") as Contents:
        List=Contents.read().split()
        #print(List)
    if(List[List.index("key")+2]=="Absent"):
        print("OpenWifi")
        return ""
    elif(List[List.index("key")+2]=="Present"):
        return List[List.index("Content")+2]
    else:
        return "3RR03"

wlan0=input("Please enter the Network for which you want to recover the password(Case Sensitive):")
print(passRec(wlan0))

os.system("del temp.txt")
