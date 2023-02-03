#!/usr/bin/python3
#Boris Depoortere, 19/01/2023, Scripting exam pt. 2
#importing modules
import regex as re
import csv
#from openpyxl import load_workbook
from openpyxl import Workbook

#for sorted dict
from collections import OrderedDict
import numpy as np

# initialize excel workbook
wb = Workbook()
ws = wb.active
# header for excel file
ws.append(["Species","LPSN link","NCBI Genome link","LPSN status","LPSN reference"])

counter = 0
dict = {}
Name = []
SpeciesID = []

textfile = open('NCBI_Genome_result_Legionella.txt', 'r')
for line in textfile:
    #print(line)
    
    #species names
    if re.match("\d\d\. ",line):
        counter += 1
        print("{}: {}".format(counter,line[4:]),end="")
        name = line[4:]
        name1 = name.rstrip()
        Name.append(name1)
    
    #species ID
    if re.match("Genome ID:",line):
        #print(line[11:],end="")
        spec = line[11:]
        spec1 = spec.rstrip()
        SpeciesID.append(spec1)
    

print("\nData from NCBI Genome file stored in dictionary:\n")

for key in Name:
    for value in SpeciesID:
        dict[key] = value
        SpeciesID.remove(value)
        break

#print(dict)

#sorting dictionary on genus
'''
keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
 
print(sorted_dict)


dict_sort = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
print(dict_sort)
'''

######## reading second .csv file ########

found_c = 0
c = 0

with open('lpsn_export.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    #print("Reading LPSN file and searching for {}:".format())
    for rowlist in csv_reader:
        #print(line)
        
        #! printing first 1000 lines as test, set to >28213 for whole list or delete if else loop statement.
        
        if c <= 1000:
        #print("{} {}".format(rowlist[0],rowlist[1]))
            for specie_genus in Name:
                
                specie = specie_genus.split(" ")

                specie_csv = rowlist[0] + ' ' + rowlist[1]
                
                #print(specie_csv)
                #print(specie_genus)
                
                if specie[0] == "Legionella":
                    
                    found_c +=1
                    
                    #data for in excel workbook
                    
                    if rowlist[10] != None:
                        Genome = "https://www.ncbi.nlm.nih.gov/genome/?term={}".format(dict[specie_genus])
                    else:
                        Genome = "-"
                    
                LPSNref = rowlist[3]
                status = rowlist[4]
                LPSNlink = rowlist[6]
                print(specie_genus, LPSNlink,Genome,status,LPSNref)
                
                
                #if dict[specie_genus] == None:
                    #print('##########################')
                
                ws.append([specie_genus, LPSNlink,Genome,status,LPSNref])
                    
                    #print(status,LPSNlink,LPSNref)
                
                #if specie_genus == specie_csv:
                    
                print("Found ({}) {}".format(found_c,specie_genus))
                print("\t--> {}".format(rowlist[6]))
                print("\t--> Genome: {}".format(Genome))
                c += 1
        else:
            break

       
print("Done")
# save the excel file
wb.save("Legionalla.xlsx")
