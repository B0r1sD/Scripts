#!/usr/bin/python
'''
def reverse(string):
    index = len(string)
    if index > 0:
        rev = ''
        rev += rev[int(index)-1]
        index -= 1
    else:
        return rev

print(reverse(borisdep))'''

def reverse(string):
    i = len(string)
    for x in string:
        print(string[i-1],end='')
        i = i - 1
    print('')

reverse("hallo")