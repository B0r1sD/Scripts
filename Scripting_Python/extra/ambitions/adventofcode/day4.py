#!/usr/bin/python

import fileinput
assignments = fileinput.input("input_files/assignments.txt")
i = 0
a = 0

for line in assignments:
    clean = line.strip()
    linesplit = clean.split(",")
    ass1 = linesplit[0].split(",")
    num1 = ass1[0].split("-")

    ass2 = linesplit[1].split(",")
    num2 = ass2[0].split("-")

    elf1 = set(range(int(num1[0]),int(num1[1]) + 1))
    elf2 = set(range(int(num2[0]),int(num2[1]) + 1))
    
    if int(num1[0]) <= int(num2[0]) and int(num1[1]) >= int(num2[1]):
        i += 1
        print(num1,num2)
    elif int(num1[0]) >= int(num2[0]) and int(num1[1]) <= int(num2[1]):
        i += 1
        print(num1,num2)
    if (elf1.intersection(elf2)):
        a += 1

print(i)

print(a)


'''
import re

with open('input_files/assignments.txt', 'r') as f:
    elvish_work = f.read().split("\n")

part_one = 0
part_two = 0
for elf_pair in elvish_work:
    l1, l2, r1, r2 = [int(x) for x in re.split('[,-]', elf_pair)]
    elf1 = set(range(l1, l2+1))
    elf2 = set(range(r1, r2+1))

    if (elf1.issubset(elf2) or elf2.issubset(elf1)):
        part_one += 1
    if (elf1.intersection(elf2)):
        part_two +=1

print("Part one:", part_one)
print("Part two", part_two)'''