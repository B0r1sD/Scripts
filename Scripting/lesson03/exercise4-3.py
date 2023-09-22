#!/usr/bin/python

def basecount():
    seq = input("enter DNA seq: ")
    dictio = {'A':0, 'G':0,'C':0,'T':0}
    length = len(seq)
    #keys = dictio.keys()
    for nt in seq:
        for x in dictio:
            if nt == x:
                dictio[x] += 1
    print(dictio)
    dict2 = dictio
    for x in dict2:
        dict2[x] = dict2[x]/length
    return dict2
print(basecount())
