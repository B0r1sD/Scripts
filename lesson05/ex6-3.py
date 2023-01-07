#!/usr/bin/python

import sqlite3

import MySQLdb as mydb

#connect to UCSC 1
print("\nREADING DATA FROM UCSC DATABASE")
try: 
    db = mydb.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")

except sqlite3.OperationalError:
    print('Nope UCSC')

except:
    print('failed to connect')

c = db.cursor()

c.execute('''
    SELECT ncbiRefSeq.name,ncbiRefSeq.name2,ncbiRefSeq.chrom FROM ncbiRefSeq JOIN kgXref ON kgXref.genesymbol = ncbiRefSeq.name2 LIMIT 10; 
''')



'''for x in c.fetchone():
    print(x)'''

print(c.fetchone())

db.commit()


db.close()

