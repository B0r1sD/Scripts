#!/usr/bin/python
'''
num = input("num: ")

if 100 < int(num) < 1000:
    print("ok")
elif int(num) > 2000:
    print("ok2")
else:
    print("not ok")'''

def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))