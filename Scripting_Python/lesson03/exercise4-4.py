#!/usr/bin/python

import time
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')

timetuple = time.localtime(time.time())

day = time.strftime("%d")
month = time.strftime("%B")

dag = locale.D_FMT
alles = time.strftime("%a, %d %b %Y %H:%M:%S")

############################################################
print("timetuple with time module: ")
print("Timezone: {}".format(timetuple.tm_zone))
print("Day of year: {}".format(timetuple.tm_yday))
print("Day of month: {}".format(timetuple.tm_yday))
print("Day of week: {}".format(timetuple.tm_yday))
print("datetime module: ")
print("Day of month: {}".format(month))
print("Day of week: {}".format(day))

print("Dag vd week: {}".format(dag))
print("Alles: {}".format(alles))
