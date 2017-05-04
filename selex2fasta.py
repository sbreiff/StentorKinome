'''
Script takes in Selex format file from hmmalign output and creates a fasta file.
'''
from sys import argv

infile = argv[1]
outfile = argv[2]

with open(infile, 'r') as selex:
    # replace all . characters in alignment with - (for gaps)
    lines = [line.replace('.', '-').rstrip('\n').split() for line in selex.readlines() if line != '\n']

seq_dict = {}

# concatenate lines for each sequence
for line in lines:
    if line[0] in seq_dict:
        seq_dict[line[0]] += line[1]
    else:
        seq_dict[line[0]] = line[1]

# create fasta file
with open(outfile, 'w') as fasta:
    for gene in seq_dict.keys():
        if not gene.startswith('#'):
            fasta.write('>%s\n%s\n' % (gene, seq_dict[gene]))            

