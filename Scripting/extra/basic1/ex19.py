#!/usr/bin/python
import re


inp = input("here: ")
'''
x = re.search('^ls', inp)
#print(x)
if bool(x) == True: 
    spl = inp.split("ls")
    print(spl[1])
else: 
    print(inp)'''

x = re.search('^ls', inp)
if bool(x) == True:
    print(inp)
else:
    print("ls" + inp)