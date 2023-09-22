#!/usr/bin/python3

# imports
import csv, re, itertools


####################################################################################
# A) read file and parse to dictionary
####################################################################################
# read the input file
with open('SRR3233298-20000.sam', mode='r') as file:
    print("Reading file SRR3233298-20000.sam\n")
    comment_counter = 0
    data_counter = 0
    data_dict = {}
    for line in file:
        # filter out comment lines ==> marked by starting with @
        result = re.search("^@", line)
        # comments
        if result:
            comment_counter += 1
            # splitting the lines on a tab will return a list
            comment_split = line.split('\t')
            print("Read comment line {}:".format(comment_counter))
            # comment 6 is special and has more values than the rest
            if comment_counter != 6:
                print("{}\t{}\t{}".format(comment_split[0],comment_split[1],comment_split[2]))
            else:
                print("{}\t{}\t{}\t{}\t{}".format(comment_split[0],comment_split[1],comment_split[2],comment_split[3],comment_split[4]))
        # data (non-comments)
        else:
            data_counter += 1
            # splitting the lines on a tab will return a list
            line_split = line.split('\t')
            # save SRRno as key and mapq as value in a dictionary
            key = line_split[0]
            value = line_split[4]
            data_dict[key] = value
            # print every 4000th value to the terminal
            if data_counter % 4000 == 0:
                print("Parsing read {}: READ={}, MAPQ={}\n".format(data_counter,key,value))
    # total number of reads
    print("Read {} genes!\n".format(data_counter))


####################################################################################
# B) Print the first five and last five records in the dictionary
####################################################################################
# first 5 and last 5 mathias way
counter = 0
first_5 = {}
last_5 = {}

for key, value in data_dict.items():
    if counter < 5:
        first_5[key] = value
    if data_counter - counter < 6:
        last_5[key] = value
    counter += 1

print("First 5 records in dictionary:")
print("{}\n".format(first_5))
print("Last 5 records in dictionary:")
print("{}\n".format(last_5))


####################################################################################
# c) Calculate the frequencies of the MAPQ values
####################################################################################
# set gives us the unique values, from set to list
s = set(data_dict.values())
val_list = list(s)
val_list.sort()
print("Unique MAPQ values:\n{}".format(val_list))

# calculate frequencies
freq = {}
# first for loop is to set the frequency counter to 0 for every unique value
for value in val_list:
    freq[value] = 0
# second for loop is to increase this counter while looping over the original dict
for value in data_dict.values():
    freq[value] += 1
# print the frequency
# loop over both key and value
for key, value in freq.items():
    print("Counting {} --> {}".format(key, value))
