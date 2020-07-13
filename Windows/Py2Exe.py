#py2exec auto
import os


def make(file):
    string="pyinstaller --onefile "+file
    os.system(string)


file=input("Enter the file to convert to .exe format:")

make(file)