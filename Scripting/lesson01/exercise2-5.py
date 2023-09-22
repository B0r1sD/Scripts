#!/usr/bin/python

a = int(input("side a: "))
b = int(input("side b: "))
c = int(input("side c: "))

print(type(a))
print(type(b))
print(type(c))

s = int(((a + b + c)/2))

A = float((s*(s-a)*(s-b)*(s-c))**(1/2))

print("triangle is cooked! s = " + str(s) + " cm and A = " + str(round(A,2)) + " cm")
#print("area: {0:10}".format(A))