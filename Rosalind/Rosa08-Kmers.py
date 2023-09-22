#!/usr/bin/python3
from itertools import permutations,product,combinations_with_replacement,combinations

#import string
#dict = list(string.ascii_uppercase)
#print(dict)

listx = []
 
symbols = "A B C D E F G H I"
length = 3

for i in "".join(symbols.split()): #great trick to remove all whitspace
  listx.append(i)

listx.sort()



#makr the perm list
p = product(listx,repeat=length)
 
# Print the obtained permutations
for j in list(p):
  for i in j:
    print(i,end="")
  print("")

#print(listx)