#!/usr/bin/python

str1 = "ijsiofn111451"

diti = {}



for n in str1:
    keys = diti.keys()
    if n in keys:
        diti[n] += 1
    else:
        diti[n] = 1
print(diti)
'''

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))'''