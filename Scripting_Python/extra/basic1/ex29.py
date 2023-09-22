#!/usr/bin/python
sets = set()

"""
def check(li1,li2):
    for x in li1:
        for y in li2:
            if x == y:
                sets.add(y)
    return sets
            
print(check(set(["White", "Black", "Red"]),set(["Red", "Green"])))


def check(li1,li2):
    for x in li1:
        for y in li2:
            if x != y:
                sets.add(x)
            else:
                break
    return sets
            
print(check(set(["White", "Black", "Red"]),set(["Red", "Green"])))

#program doesn't work when appending li2 with Black e.g."""

def check(li1,li2):
    for x in li1:
        if x not in li2:
            sets.add(x)
        else:
            break
    return sets
            
print(check(set(["White", "Black", "Red"]),set(["Red", "Green"])))