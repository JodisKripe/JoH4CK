import os
os.system("echo Enum-ing")
# Basics
os.system("systeminfo")
os.system("hostname")

# Who am I?
os.system("whoami")
os.system("echo %username%")

# What users/localgroups are on the machine?
os.system("net users")


# Firewall
os.system("netsh firewall show state")
os.system("netsh firewall show config")

# Network
os.system("ipconfig /all")
os.system("route print")
os.system("arp -A")

# How well patched is the system?
os.system("wmic qfe get Caption,Description,HotFixID,InstalledOn")
os.system("echo <------------------------NETSTAT------------------------>")
os.system("netstat -ano")

os.system("echo <-----------------Looking for Passes-------------------------->")
os.system("findstr /si password *.txt")
os.system("findstr /si password *.xml")
os.system("findstr /si password *.ini")

#Find all those strings in config files.
os.system("dir /s *pass* == *cred* == *vnc* == *.config*")

os.system("wmic process list brief | find \"winlogon\"")

os.system("wmic os get OSArchitecture")

os.system("nbtstat -n")

# Find all passwords in all files.
#os.system("findstr / /spin \"password\" *.*")
#os.system("findstr / /spin \"password\" *.*")


while True:
    foo=input()