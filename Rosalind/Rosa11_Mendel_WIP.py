#!/bin/python3
#BDP

k = 2 #homozygous dominant
m = 2 #heterozygous 
n = 2 #homozygous recessive

tot = k + m + n
x = 4

pairs = (tot*(tot-1)/2) #each org mates with another, besides itself 
total = pairs*x #total amount of possibilities

#XX * XX -> 1
c1 = 1
#XX * Xx -> 1
#XX * xx -> 1
#Xx * Xx -> 0.75
c2 = 0.75
#Xx * xx -> 0.5
c3 = 0.5
#xx * xx -> 0

prob = ((1*4)*3+(0.75*4)+(0.5*4))

print(prob)

print(pairs,total)
