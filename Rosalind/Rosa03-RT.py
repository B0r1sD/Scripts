#!/usr/bin/python3
nts = open("inputs/03-DNA.txt", "r")

for nucleotides in nts:
    for n in nucleotides[::-1]:
        if n == "A":
            print("T", end="")
        elif n == "T":
            print("A", end="")
        elif n == "C":
            print("G", end="")
        elif n == "G":
            print("C", end="")
        else:
            print("Error")