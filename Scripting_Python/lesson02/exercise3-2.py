#!/usr/bin/python

day = input("day of birth: ")
month = input("month of birth: ")

if month == "January":
    if int(day) >= 20:
        print("astrological sign = cancer")
        exit()
    else:
         print("astrological sign = capricorn")
elif month == "February":
    if int(day) >= 19:
        print("astrological sign = Pisces")
        exit()
    else:
         print("astrological sign = Aquarius")


# Paco: astro = 'sagitarrus' if (day < 22) else 'capricorn'
#copy and continue
'''
if month == "January":
    if int(day) >= 20:
        astro =  "cancer"
    else:
         astro = "capricorn"'''