#!/usr/bin/python3
fasta = open("Rosalind/inputs/hamming.txt","r")

lines = []
i = 0
counter = 0

for line in fasta:
    lines.append(line.strip())

print(lines)


for i in range(0,len(lines[0])):
    if lines[0][i] != lines[1][i]:
        #print(i)
        counter += 1

print(counter)
