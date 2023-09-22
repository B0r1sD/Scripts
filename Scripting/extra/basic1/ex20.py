#!/usr/bin/python

slip = input("input string: ")
n = input("how many times do you want it repeated?: ")
i = 0
if int(n) > 0:
    while i <= int(n):
        print(slip, end='')
        i+=1
else:
    print("error, n not positive!")