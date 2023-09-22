#!/usr/bin/python
'''
1)
var1 = input("Gimmme\n")
print(var1.upper())
print(var1.lower())

2)
from stringcolor import * 

sq = input("input sequence\n")
motif = input("input motif\n")
length = len(motif)
place = sq.find(motif)
print("the motif " + motif + " was found on pos " + str(place) + " and is found:\n" + sq[:place] + cs(sq[place:place+length],"orchid") + sq[place+length:] )

3)
'''
sq = input("input sequence\n")
split = input("input cleavage site\n")
length = len(split)
place = sq.find(split)

print(sq[place+length:])

result = sq.split(split)
print("Seq fragments: {}".format(result))