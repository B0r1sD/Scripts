#!/usr/bin/python
r = 0
print(r, end=", ")
i = 0
y = 1
while r <= 50:
    
    r = i + y
    print(r, end=", ")

    y = i
    i = r

    
