#!/usr/bin/python
'''
li = []
li2 = []
word = print("input words (type 'stop' to stop): ")
while word != "stop":
    word = input()
    li.append(word)

amount = 0
for value in li:
    print(type(value))
    if isinstance(value, str) == True:
        amount = amount + 1
        li2.append(value)
print(li[:int(amount - 1):])
print("Number of strings: " + str(amount - 1))
'''

li = []
li2 = []
word = print("input words (type 'stop' to stop): ")
while word != "stop":
    word = input()
    li.append(word)

for value in li:
    if value[0] == value [len(value)-1]:
        li2.append(value)
print("Number of strings: "  + str(len(li2)))
print(li2)