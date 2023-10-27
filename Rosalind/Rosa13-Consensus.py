#!/usr/bin/env python
#BDP

count = 0
length = 0
row = []
disk = []
strings = []
stringn = ''
test = 0

storage = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

with open('inputs/matrix.txt', 'r') as matrix:
    for line in matrix:
        #print(line.rstrip())
        if line.startswith('>'):
            count += 1
            if count != 1: #skip first line
                test += 1
                strings.append(stringn)
                stringn = ''
            else:
                print('first line')
        else:
            length += 1
            stringn += line.rstrip()

strings.append(stringn)

for linen in strings:
    for nt in linen:
                #print(nt)
                #storage[nt] += 1
        row.append(nt)
    disk.append(row)
    row = []

i = 0
print(disk)

arrayA = []
arrayC = []
arrayG = []
arrayT = []

test1 = 0

print(disk[0][0])
print(storage[disk[0][0]])

for i in range(0, len(disk[0])): #go through the columns
    
    for j in range(0, count): #go through the rows
    #print(disk[i][1])
        storage[disk[j][i]] += 1
        test1 += 1
        # print('succes')
        #print(count)
    arrayA.append(storage['A'])
    arrayC.append(storage['C'])
    arrayG.append(storage['G'])
    arrayT.append(storage['T'])
    storage = {'A': 0, 'C': 0, 'G': 0, 'T': 0}


#print(storage)
# print(disk)
# print(count)
# print(len(disk[0]))

import numpy as np

#combine the arrays into a matrix
matrix = np.array([arrayA, arrayC, arrayG, arrayT])

print('A:', end=' ')
for nt in arrayA:
    print(nt, end=' ')

print('\nC:', end=' ')
for nt in arrayC:
    print(nt, end=' ')

print('\nG:', end=' ')
for nt in arrayG:
    print(nt, end=' ')

print('\nT:', end=' ')
for nt in arrayT:
    print(nt, end=' ')

print('\n',end='')
#print(matrix)

for i in range(0, len(matrix[1])):
    column = matrix[:, i]
    #print(column)
    #print(max(column))
    if max(column) == matrix[0][i]:
        print('A', end='')
    elif max(column) == matrix[1][i]:
        print('C', end='')
    elif max(column) == matrix[2][i]:
        print('G', end='')
    elif max(column) == matrix[3][i]:
        print('T', end='')

# print(len(arrayA))
# print(len(arrayC))
# print(len(arrayG))
# print(len(arrayT))
# print(test)
# print(len(strings[0]))

# print(matrix)
    
