#!/usr/bin/python

import datetime

datum = datetime.date.today()

voor = datum - datetime.timedelta(days=5)
na = datum + datetime.timedelta(days=7)

print("now:  \t\t{}".format(datum))
print("Week after:\t{}".format(na))
print("Five days before: {}".format(voor))