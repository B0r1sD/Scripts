#!/bin/usr/python

list1 = list(input("input list: "))
list2 = list1.split(",")

for i in list2:
    print(i)
    if i == int(15):
        print('gotya')