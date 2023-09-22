#!/usr/bin/python

def seperator():
    string = input("string: ")
    sep = input("give symbol to split on: ")
    joinon = input("give symbol to join on: ")
    new = string.split(sep)
    out = joinon.join(new)
    return out

print(seperator())
