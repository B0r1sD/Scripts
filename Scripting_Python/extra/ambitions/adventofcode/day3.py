#!/var/bin/python

import fileinput
import math
import string
import re

list1 = []
list2 = []
i = 0
part1 = ''
part2 = ''
som = 0
match = ''

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
range1 = list(range(1,27))
range2 = list(range(27,53))
dict1 = dict(zip(lower,range1))
dict2 = dict(zip(upper,range2))
c = 0
counter = 0
z = []
u = 0

for line in fileinput.input("input_files/rucksak3.1.txt"):
    i += 1
    list1.append(line.strip())
    if i == 3:
        list2.append(list1)
        list1 = []
        i = 0

for lijst in list2:
    for indiv in lijst:
        u += 1
        if u == 1:
            l1 = set(indiv)
        if u == 2:
            l2 = set(indiv)
        if u == 3:
            l3 = set(indiv)
            z = l1.intersection(l2,l3)
                #print(z)
            match = z.pop()
            print(match)
            u = 0
                
    if match.islower():
        for key in dict1:
            if key == match:
                som = som + int(dict1[key])
                print(som)

    elif match.isupper():
        for key in dict2:
            if key == match:
                som = som + int(dict2[key])
                print(som)
                

        
        '''for c in lijst[counter]:
            if len(lijst[counter]) 
            print(c)
            counter += 1

        print(l1,l2,l3)'''
        
        '''for line in lijst:
            for char in lijst:
                if char '''
#print(list2)





'''
for line in fileinput.input("input_files/rucksak3.1.txt"):
    fpart, lpart = line[:len(line)//2], line[len(line)//2:]
    for x in fpart:
        for y in lpart:
            if x == y:
                if match != x:
                    match = x
                else:
                    continue

    if match.islower():
        for key in dict1:
            if key == match:
                som = som + int(dict1[key])

    elif match.isupper():
        for key in dict2:
            if key == match:
                som = som + int(dict2[key])

print("som: {}".format(som))'''
'''
counter = 0
i = 0
dicti = {}
high = 0

for line in fileinput.input("input_files/rucksak3.1.txt"):
    counter += 1
    while line != "":
	    slen0 = len(line)
	    ch = line[0]
	    line = line.replace(ch, "")
	    slen1 = len(line)
	    if slen1 == slen0-1:
		    print ("First non-repeating character = ",ch)
		    break
	    else:
		    print ("No Unique Character Found!")
    for x in line:
        dicti = {x:0}
        dicti[x].append(1)
        print(dicti)
        
    if counter == 3:
        high = max(dicti)
        print(high)
        counter = 0

    if dicti[x].islower():
        for key in dict1:
            if key == match:
                som = som + int(dict1[key])

    elif match.isupper():
        for key in dict2:
            if key == match:
                som = som + int(dict2[key])'''

print("som: {}".format(som))