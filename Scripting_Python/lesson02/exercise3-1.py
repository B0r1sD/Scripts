#!/usr/bin/python
''' a)
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list2 = [x for x in list1 if x % 2 == 0]

print(list2)
'''
import datetime

today = datetime.datetime.today()
year_now = today.year
#or today.strftime("%Y")
print(year_now)

years = [1990, 1995, 1990, 1991, 1992, 1991]

ages = [year_now - x for x in years]

print(ages)