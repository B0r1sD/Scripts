#!/usr/bin/python

from datetime import date

date1 = date(2013, 7, 2)
date2 = date(2014, 7, 11)
delta = date2 - date1
print("difference: " + str(delta.days))
#print("The difference is " + str(int(li[0][2]) - int(li[1][2])))
