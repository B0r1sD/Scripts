#!/usr/bin/python3
nts = open("inputs/02-DNA.txt", "r")

for nucleotides in nts:
    for n in nucleotides:
        if n == "T":
            print("U", end="")
        else:
            print(n, end="")
            
nts.close()