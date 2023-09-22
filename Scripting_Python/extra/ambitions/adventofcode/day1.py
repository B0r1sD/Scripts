#!/usr/bin/python
import fileinput
calories = fileinput.input("input_files/calories1.1.txt")

i = 0
summ = 0
list1 = []

for line in calories:
    if line != "\n":
        summ = summ + int(line)
    elif line == "\n":
        #print(summ)
        list1.append(summ)
        summ = 0

#print(list1)
print(max(list1))

'''total = 0
for x in list1:
    if int(x) > total:
        total = x
print(x)'''

list1.sort()
som = (list1[-1] + list1[-2] + list1[-3])
print(som)