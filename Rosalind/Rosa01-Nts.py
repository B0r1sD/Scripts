#!/usr/bin/python3
nts = open("inputs/01-nts.txt", "r")

dict = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0
}

for nuclts in nts:
    for n in nuclts:
        #print(n)
        for x in dict:
            #print(x)
            if n == x:
                #print("succes")
                dict[x] += 1

print(dict)

nts.close()