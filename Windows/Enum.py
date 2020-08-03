import os
from colorama import init 
from termcolor import colored 
  
init() 
  
print(colored('Hello, World!', 'green', 'on_red'))

'''
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

'''

os.system("echo Enum-ing")
# Basics
print(colored("SystemInfo","green",'on_red'))
os.system("systeminfo")
os.system("echo ")
print(colored("HostName",'green','on_red'))
os.system("hostname")

# Who am I?
os.system("echo ")
print(colored("whoami","green","on_red"))
os.system("whoami")
os.system("echo ")
print(colored("Username","green","on_red"))
os.system("echo %username%")
os.system("echo ")

# What users/localgroups are on the machine?
print(colored("net users","green","on_red"))
os.system("net users")


# Firewall
os.system("echo ")
print(colored("netsh firewall show state","green","on_red"))
os.system("netsh firewall show state")
os.system("echo ")
print(colored("netsh firewall show config","green","on_red"))
os.system("netsh firewall show config")
os.system("echo ")
# Network
print(colored("ipconfig/all","green","on_red"))
os.system("ipconfig /all")
os.system("echo ")
print(colored("Route print","green","on_red"))
os.system("route print")
print(colored("ARP","green","on_red"))
os.system("arp -A")


# How well patched is the system?
print(colored("wmic qfe get Caption,Description,HotFixID,InstalledOn","green","on_red"))
os.system("wmic qfe get Caption,Description,HotFixID,InstalledOn")
os.system("echo ")
os.system("echo <------------------------NETSTAT------------------------>")
print(colored("NETSTAT","green","on_red"))
os.system("netstat -ano")


os.system("echo <-----------------Looking for Passes-------------------------->")
os.system("findstr /si password *.txt")
os.system("findstr /si password *.xml")
os.system("findstr /si password *.ini")

#Find all those strings in config files.
os.system("dir /s *pass* == *cred* == *vnc* == *.config*")

print(colored("wmic process list brief","green","on_red"))
os.system("wmic process list brief | find \"winlogon\"")
print(colored("OSArchitecture","green","on_red"))
os.system("wmic os get OSArchitecture")
print(colored("nbtstat","green","on_red"))
os.system("nbtstat -n")

# Find all passwords in all files.
#os.system("findstr / /spin \"password\" *.*")
#os.system("findstr / /spin \"password\" *.*")


while True:
    foo=input()
