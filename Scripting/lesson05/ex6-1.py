#!/usr/bin/python

import MySQLdb as my

# Reading data from UCSC
print("\nREADING DATA FROM UCSC DATABASE")


"""db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")"""

try:
    db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_104_38")
except: 
    print("connection failed")

c = db.cursor()
no_rows = c.execute("""SELECT gene.gene_id, transcript.stable_id, gene.description FROM transcript JOIN gene on gene.gene_id = transcript.gene_id LIMIT 100""")
# Fetch one row (ENST + ENSG)
result = c.fetchone()
#print(c.fetchall())
print("Total rows: {}".format(no_rows))

'''
i = 0
for x in result:
    print(x)
    i += 1
    lijn += [(x)]

print(lijn)
'''
db.close()