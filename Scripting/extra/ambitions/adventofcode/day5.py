#!/usr/bin/python

cratedict = {
            1:["F","D","B","Z","T","J","R","N"],
            2:["R","S","N","J","H"],
            3:["C","R","N","J","G","Z","F","Q"],
            4:["F","V","N","G","R","T","Q"],
            5:["L","T","Q","F"],
            6:["Q","C","W","Z","B","R","G","N"],
            7:["F","C","L","S","N","H","M"],
            8:["D","N","Q","M","T","J"],
            9:["P","G","S"]
            }

print(cratedict)
i = 1

import fileinput
instructions = fileinput.input("input_files/crates.txt")
for x in instructions:
    i = 1
    splitted = x.strip().split(" ")
    Quant = splitted[1]
    From = int(splitted[3])
    To = splitted[5]
    #print(Quant,From,To)
    while i <= int(Quant):
        krat = cratedict[From][-1]
    
        del cratedict[From][-1]

        #print("Quant: {}, From: {}, To: {}".format(Quant, From, To))
        #print(krat)
        cratedict[int(To)] += [krat]
        #print(cratedict)
        i += 1
    
        #for x in cratedict:
        #pop = cratedict.pop(1)
        #cratedict[1].append("[]")

for x in cratedict:
    print(cratedict[x][-1],end="")