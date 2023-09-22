#!/usr/bin/python

numbers = []
print("Enter integers to calculate sum and average.\nInput 0 to exit.\n")
num = 1
while int(num) != 0:
    num = input("")
    numbers.append(num)

print(numbers)

print("calculating sum and average: ")

sumi = 0.0
for value in numbers:
    sumi = sumi + int(value)
print("sum: " + str(sumi))
print("average: " + str(sumi/len(numbers)))