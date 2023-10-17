#!/usr/bin/python
#BDP

#pseudocode
#if line start with '>', count += 1 and continue to next line
#add all lines to a string until next '>' is found
#save string in a list where motifs can be matched

from difflib import SequenceMatcher

seqs = open("inputs/seqs.txt","r")
count = 0
seq1 = ''
list = []
strings = []
string = ''
count2 = 0
IsSeq = False

for seq in seqs:
    
    #printing
    #print(f'line: {seq}')
    #print(f'string: {string}',end='')

    #processing
    if seq[0] != '>':
        IsSeq = True
        string += seq.strip()

    else:
        if IsSeq == False: #skip first line
            print('first line')
        else:
            IsSeq = False
            strings.append(string)
            #holds sequence number 
            count+=1
            string = ''
        #print('=== loop done ===')
        

#print(strings)

# Find the longest common subsequence between the first two sequences
matcher = SequenceMatcher(None, strings[0], strings[1],autojunk=False)
match = matcher.find_longest_match(0, len(strings[0]), 0, len(strings[1]))
motif = strings[0][match.a:match.a + match.size]



# Find the longest common subsequence between the motif and each subsequent sequence
for sequence in strings[2:]:
    matcher = SequenceMatcher(None, motif, sequence,autojunk=False)
    match = matcher.find_longest_match(0, len(motif), 0, len(sequence))
    motif = motif[match.a:match.a + match.size]
    print(motif)

#print the final motif
print(motif)

