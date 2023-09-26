#!/bin/python3
#BDP

file = open('motif.txt', 'r')

counter = 0
counter2 = 0
final = 0

positions = []

for line in file:
    counter+=1
    print(line, end='')
    if counter==1:
        Main = line
        continue
    else:
        motif = line
        for nt in Main:
            
            if motif in Main[counter2:len(motif)+counter2]:
                print('succes')
                final+=1
                positions.append(counter2+1)

            counter2+=1 #append at end or skip first nt


    

print(f'\n{counter} strings, and Main = {Main}, motif = {motif}')

print('='*30)
print(final)

for x in positions:
    print(x, end=' ')


file.close()

