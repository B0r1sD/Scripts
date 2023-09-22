import csv
import re

#excel
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active


faail = open('/home/guest/Downloads/129P2_OlaHsd.mgp.v5.indels.dbSNP142.normed.vcf', "r")
#csv_reader = csv.reader(faail, delimiter=',')
counter = 0
counter2 = 0

with open('results.csv', "w") as fresults:
    wresults = csv.writer(fresults, dialect="excel", delimiter=';')
    wresults.writerow(["chromosome", "position", "reference", "alternatives"])
    ws.append(["chromosome", "position", "reference", "alternatives"])
for line in faail.readlines():
    counter += 1
    if counter < 100000000:
        #print(line)
        match = re.search("^#",line)
        if match:
            continue
            #print("{}: {}".format(counter,line))

        tab = re.search("INDEL*",line)
        if tab:
            counter2 +=1
            indellist = line.split("\t")
            #print(indellist)
            shift = re.search("frameshift|stop_gained",indellist[7])
            if shift:
                #print(indellist[7])
                ws.append([indellist[0], indellist[1], indellist[3], "frameshift/stop_gained"])
                with open('results.csv', "a") as fresults:
                    wresults = csv.writer(fresults, dialect="excel",delimiter=',')
                    wresults.writerow([indellist[0], indellist[1], indellist[3], "frameshift/stop_gained"])
    else:
        exit
            
wb.save("results.xlsx")   
faail.close()
fresults.close()