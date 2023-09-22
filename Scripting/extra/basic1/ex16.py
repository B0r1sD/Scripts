#!/usr/bin/python

number = input("number: ")

if int(number) > 17:
    print(abs((17 - int(number))*2))
else:
    print(17 - int(number))