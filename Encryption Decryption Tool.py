import pyfiglet
import sys
import socket
from datetime import datetime
  
print("-"*50)
print(" ")
ascii_banner = pyfiglet.figlet_format("  CyberSec")
print(ascii_banner)
print(" "*18+"Encryption / Decryption Tool")
print("-"*50)
print(" ")

def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("E-" + filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    


choice = ""
while choice != "3":
    print(" Please select you option.")
    print(" [+] Encrypt File -> 1 ")
    print(" [+] Decrypt File -> 2 ")
    print(" [+] Quit         -> 3 ")
    choice = input(" => ")
    if choice == "1" or choice == "2":
        key = int(input(" [+] Enter a key as int!\n => "))
        filename = input(" [+] Enter filename with extension:\n => ")
    if choice == "1":
        Encrypt(filename, key)
    if choice == "2":
        Decrypt(filename, key)

