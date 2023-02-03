#!usr/bin/python3

import csv

from eutils import Client
# Initialize client that handles all caching and query
# Using API key from NCBI account settings e.g. 
eclient = Client(api_key="face39c63564e706a8dd9eaa4e46086a5a08")
print("\nUsing NCBI E-utilities in Python\n")

# Reading csv file line by line
with open('gene_species.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print column names
            print("Column names are:")
            print("{} | {}".format(row[0],row[1]))
            line_count += 1
        else:
        # print all data
            print("{0:5s} | {1:5s}".format(row[0],row[1]))
            line_count += 1
            
            entrez = '{} [gene] AND "{}" [orgn] AND refseq [filter]'.format(row[0],row[1])
            print(entrez)
            prot_esearch = eclient.esearch(db='protein',term=row[0])
            #print("\n\nResults of gene esearch:\n{}".format(gene_esearch))
            obj_summary_list = dir(prot_esearch)
            #print(obj_summary_list)
            #print("ids: {}".format(gene_esearch.ids))

            
            ################################################################################
            # EFETCH: get record using Id e.g. gene id 7157 for human TNF
            ################################################################################
            with open('sequences.fasta', mode='a+') as output:
                for id in prot_esearch.ids:
                    
                    prot_efetch = eclient.efetch(db='protein', id=id)
                    #print("\n\nResults of gene efetch:\n{}".format(prot_efetch))
                
                    # gbseqs[0] contains the right information
                    refseq = prot_efetch.gbseqs[0]
                    # Gene object attributes
                    refseq_list = dir(refseq)
                    
                    sequence = refseq.sequence
                    print(sequence)

                    # species_splt will split the species name in 2 parts, Mus and musculus
                    species_splt = row[1].split(" ")
                    # printing in terminal
                    print(">{}_{}_{}_id={}".format(row[0],species_splt[0],species_splt[1],id))
                    print("{}".format(sequence))
                    # writing to file
                    output.write(">{}_{}_{}_id={}\n".format(row[0],species_splt[0],species_splt[1],id))
                    output.write("{}\n".format(sequence))

            print("Processed {} lines.".format(line_count))
csv_file.close()
output.close

