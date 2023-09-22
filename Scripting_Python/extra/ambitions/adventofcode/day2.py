#!/var/bin/python

import fileinput
X = 1
Y = 2
Z = 3

W = 6
L = 0
D = 3

summ = 0
total = 0

for line in fileinput.input("input_files/strategy2.1.txt"):
        if line[0] == "A":
            if line[2] == "X":
                total += Z + L
            elif line[2] == "Y":
                total += X + D
            elif line[2] == "Z":
                total += Y + W
        
        elif line[0] == "B":
            if line[2] == "X":
                total += X + L
            elif line[2] == "Y":
                total += Y + D
            elif line[2] == "Z":
                total += Z + W

        elif line[0] == "C":
            if line[2] == "X":
                total += Y + L
            elif line[2] == "Y":
                total += Z + D
            elif line[2] == "Z":
                total += X + W
        summ = summ + total
        total = 0

print(summ)