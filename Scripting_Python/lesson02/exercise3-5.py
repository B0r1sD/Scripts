#!/usr/bin/python

li = (0, 2, 6, 8, 4, 0, 57, 51, 2, 245, 4)

n = 0

for value in li:
    if value > n:
        n = value
        print("Loop:\t" + str(value) + "\t" + str(n))
    else:
        print("Loop:\t" + str(value) + "\t" + str(n))

print("Largest: " + str(n))