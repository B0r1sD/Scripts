#!/usr/bin/python3

import pprint

fasta = open("Rosalind/inputs/GC_content_fastas.txt","r")

scores = {}

i = 0

for line in fasta:
        #print(line)
    if line.startswith('>'):                             #header line
            print(line,end="")
            header = line.strip('>\n')
            scores[header] = 0
            nt_lib = {"A":0,"C":0,"G":0,"T":0}
    else:                            #sequence
        print(line,end="")
        for nt in line:
            if nt in nt_lib:
                nt_lib[nt]+=1
        print(nt_lib)
        GC_content = ((nt_lib["G"] + nt_lib["C"]) / (nt_lib["A"] + nt_lib["T"] + nt_lib["G"] + nt_lib["C"])) * 100
        scores[header] = GC_content


pprint.pprint(final := {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])})

print(list(final)[-1])
print(final[list(final)[-1]])