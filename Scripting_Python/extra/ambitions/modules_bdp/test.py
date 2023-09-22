#!/usr/bin/python
'''
import mymodul as mine
mine.greeting("Boris")'''

#mymodul has te be in the same folder!!
from mymodul import greeting
greeting("Boris")

import time

timetuple = time.time()
print("{}".format(timetuple))