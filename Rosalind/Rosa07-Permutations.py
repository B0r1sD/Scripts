#!/usr/bin/python3

import itertools

#perm = int(input("permutations: "))   --> output in terminal too big, redirect stdout to file on command line
perm = 5

#recursive function to calculate factorial for total amount of possible permutations
def factorial(n):
    if n == 1:
        return 1
    return n * (factorial(n-1))

x = factorial(perm)

numbers = []

for i in range(1,perm+1):
    numbers.append(i)

#print(numbers)

perm_set = itertools.permutations(numbers)

#print amount of total permutations 
print(x) 

for i in perm_set:
    for j in i:
        print(j,end=" ")
    print()

