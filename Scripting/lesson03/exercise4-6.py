#!/usr/bin/python
import re

password = input("insert fake password: ")

i = 0

while i == 0:
    if re.search("[a-z]", password) == None:
        print("Bro put [a-z] in your string")
        i+=1
    elif re.search("[0-9]",password) == None:
        print("Bro put [0-9] in your string")
        i+=1
    elif re.search("[$#@]",password) == None:
        print("Bro put [$#@] in your string")
        i+=1
    else:
        if 6 < len(password) < 16:
            print("Secure password.")
            i+=1
        else:
            print("Bro length between 6 and 16.")
            i+=1