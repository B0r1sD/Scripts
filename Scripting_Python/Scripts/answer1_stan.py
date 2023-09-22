#!/usr/bin/python3

# imports
import MySQLdb as my
import re
from openpyxl import Workbook

# initialize excel workbook
wb = Workbook()
ws = wb.active
ws.title = "SNP output"
# header for excel file
ws.append(["Accession no.","SNP","Chr:start-stop"])

###############################################################
# A Input
###############################################################
print("This script will look for SNP's using RefSeq accession numbers")
print("="*62)
accessions = []

# if user inputs 0, enters 0, writes 0 --> the input ask will stop and the script will continue
while True:
    acc = input("Enter accession no. or type 0 to stop: ")
    if acc != "0":
        accessions.append(acc)
        continue
    else:
        break
print("\nYour list:")
print(accessions)
print("="*62,"\n")

###############################################################
# B handling data
###############################################################
# connect to UCSC
db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
    user="genomep",
    passwd="password",
    db="hg38")
cursor = db.cursor()
for accession in accessions:
    # find all SNP's
    query = "SELECT * FROM snp151CodingDbSnp WHERE transcript = " 
    no_snp = cursor.execute("""{}'{}'""".format(query,accession))
    print(no_snp)
    
    print("Getting SNPs for:",accession)
    print("using query: {}'{}'".format(query,accession))
    print("Total SNPs found for",accession,":",no_snp,"\n")
    # get all results of the SNP query
    result = cursor.fetchall()
    # iterate over result
    for row in result:
        # header = ["Accession no.","SNP","Chr:start-stop"]
        accno = "{}".format(row[5])
        snp = "{}".format(row[4])
        chr_region = "{}:{}-{}".format(row[1],row[2],row[3])
        ws.append([accno, snp, chr_region])

# make the excel cells wider
ws.column_dimensions["A"].width = 25.0
ws.column_dimensions["B"].width = 25.0
ws.column_dimensions["C"].width = 25.0

# save the excel file
wb.save("./trial_exams/SNPs.xlsx")
