#!/usr/bin/python

import fileinput
signal = fileinput.input('input_files/signal.txt')
#print(signal)

check = []
i = 0

"""
for line in signal:
    #print(line)
    for char in line:
        i += 1
        if i <= 4:
            check = check + char
        '''if i == 4:
            print(len(set(check)))'''
        if i > 4:
            #print(check)
            
            newcheck = check.lstrip(check[0])
            uppercheck = newcheck + char
            #print(check)
            #print(newcheck)
            if len(set(uppercheck)) == 4:
                print(str(i) + uppercheck)
            '''out = check.intersection()
            print(out)'''
        if i >= len(line):
            print("end")
            exit()
"""

 

for line in signal:
    #print(line)
    for char in line:
        i += 1
        check.append(char)

        if i == 14:
            newcheck = check
            #print(newcheck)
        
        if i >= 14:
            uppercheck = newcheck[1:]
            uppercheck.append(char)
            print(uppercheck)
            
            if len(set(uppercheck)) == 14:
                print(str(i))
                print(uppercheck)
                exit()
            
            newcheck = uppercheck