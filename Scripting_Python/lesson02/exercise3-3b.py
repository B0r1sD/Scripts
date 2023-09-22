#!/usr/bin/python
num = 6
while int(answer) != int(num):
    print(answer)
    answer = input("guess between 1 and 9: ")
    
    print(type(answer))
    if answer == num:
        print("YES")
        exit()
    
