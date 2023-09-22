#!/usr/bin/python

num = input("Give number: ")

calc = int(num) % 2

if calc == 0:
    result = "even"
    
else:
    result = "odd"

print("You got a " + result + " number on yo hand!")