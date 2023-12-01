#!/usr/bin/python
#BDP

from string import digits
import os
os.chdir("/data/projects/s20/bodep/test/AoC2023")

input = open("input/1A.txt", "r")
begin = None
end = None

matrix = []

def calc():
    for line in input:
        #print(line)
        append = False
        for char in line:
            if char in digits:
                begin = char
            else: continue
            if begin != None:
                for char in line[::-1]:
                    if char in digits:
                        end = char
                        matrix.append(int(begin + end))
                        append = True
                        break
            else: continue
            if append == True:
                break
    return matrix   

sum = 0
for numb in calc():
    sum += numb

print(sum)
