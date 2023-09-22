#!/usr/bin/python

import itertools
import random

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3' ,'2']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

'''
a = random.randint(13, 100)
i = 0


#while i <= a:
#    deck = list(itertools.combinations(ranks, 13))
#    i+=1

#shuffle twice
while i <= 1:
    random.shuffle(ranks)
    i+=1
#print(ranks)

dek = []
n = 0
A = 0
B = 0
C = 0
D = 0

for x in ranks:
    for y in suits:
        while n <= 1:
            rand = random.randint(1, 4)
            pair = [x,y]
            if rand == 1 and A <= 13:
                dek.append(pair)
                A+=1
            elif rand == 2 and B <= 13:
                dek.append(pair)
                B+=1
            elif rand == 3 and C <= 13:
                dek.append(pair)
                C+=1
            elif rand == 4 and D <= 13:
                dek.append(pair)
                D+=1
        n+=1
print(dek)
'''

deck = list(itertools.product(ranks, suits))

i = 0
while i <= 1:
    random.shuffle(deck)
    i+=1

for x in range(4):
    print(deck[x])