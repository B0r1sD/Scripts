#!/usr/bin/python

i = 0

'''
for n in range(5):
    n =+ 1
    while i < n:
        print("*", end="")
        i =+ 1
    print("\n")'''
'''
for x in range(5):
    while i < x:
        print("*", end="")
        i = i + 1
        print(i)
'''


n = 5
l = 0
x = 0
while i < n:
    l = l + 1
    while x < l:
        print("*",end=" ")
        x = x + 1
    print("")   
    i = i + 1
    x = 0

while i > 0:
    l = l - 1
    while x < l:
        print("*",end=" ")
        x = x + 1
    print("")   
    i = i - 1
    x = 0
