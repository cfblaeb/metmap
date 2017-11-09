#!/usr/bin/env python
import argparse
from metmap.metmap import do_it_all
from Bio.SeqIO import write

parser = argparse.ArgumentParser(description="Generate DNA MTase binding cassettes. Output on screen and written to genbank and fasta.")
parser.add_argument("motif_file", type=argparse.FileType(), help="Plain text file with 1 motif per line")
parser.add_argument("-k", type=int, default=10, help="Copies of rule 1 motifs")
parser.add_argument("-l", type=int, default=12, help="Copies of rule 2 motifs")
parser.add_argument("-m", type=int, default=1, help="number of N's between each motif")
parser.add_argument("-p", type=int, default=1, help="number of cassettes to generate")
args = parser.parse_args()


print("/------------------------------------\\")
print("|-----------METMAP RUNNING-----------|")
print("\------------------------------------/")
print("")
print("")
cassettes = do_it_all(args.motif_file, args.k, args.l, args.m, args.p)
print("")
print("")
for i, cas in enumerate(cassettes):
    print(f"Cassette {i+1}")
    print(cas)
    print("")
    write(cas, open(f"cas{i+1}.gb", 'w'), 'genbank')
    write(cas, open(f"cas{i+1}.fa", 'w'), 'fasta')

