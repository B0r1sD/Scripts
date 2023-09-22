#!/usr/bin/python3
################################################################################
# MySQL (example-code-6-ensembl.py)
################################################################################
import MySQLdb as my
from datetime import datetime, timedelta

now1 = datetime.now()

current_time = now1.strftime("%H:%M:%S")
print("Start Time =", current_time)


# Reading data from Ensembl
print("\nREADING DATA FROM ENSEMBL DATABASE")
# Core databases: <genus_species>_core_<version>_<assembly_version>
# Ensembl Release 104 (May 2021)
try:
    db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_104_38")

except:
    print('failed to connect')

c = db.cursor()


resultx = c.execute("""SELECT gene.gene_id,transcript.transcript_id, gene.description FROM gene join transcript on gene.gene_id=transcript.gene_id""")
# Fetch all results
print(c.fetchone())
# Iterate over result
resultx = c.fetchall()
#print(resultx)

################################################################################
import sqlite3
conn2 = sqlite3.connect('ensembl.db')
c2 = conn2.cursor()

i=0

try:
    c2.execute('''CREATE TABLE ex62 (gene_id, transcript_id, description);''')
    for x in resultx:
        c2.execute('''insert into ex62 values(?,?,?)''',(x[0],x[1],x[2]))
        i += 1
    

except:
    print('idk what went wrong')
    
conn2.commit() # commit changes
db.close()
conn2.close()

now2 = datetime.now()
print("Delta Time =", now2-now1)

print("records: {}".format(i))