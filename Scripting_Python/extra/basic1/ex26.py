#!/usr/bin/python

def histogram(list):
    for value in list:
        i=0
        while i < int(value):
            print("#",end="")
            i = i + 1
        print("")
    return
histogram([10, 8, 2, 15])