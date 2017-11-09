# metmap
DNA methyltransferase binding motif plasmid assembler

## Overall purpose:
* To identify the motifs of multiple DNA methyltransferases (DNA MTase) simultaneously.

### Quick start
* This script requires python 3.6 or newer.
* Install using "pip install metmap"
* This will put a script named "run_metmap.py" in your pythons bin folder.
  * Linux: You should just be able to type "run_metmap.py" from terminal
  * Windows: The script will be placed in your python folders "Scripts" subfolder and you can run it with "python path\to\python\Scripts\run_metmap.py" from command line
  * Mac: Who knows..probably works like linux?


## Overview:
* You have an organism with multiple identified DNA MTases and you wish to know their individual motifs.
* You use NGS to obtain motifs of all methylated DNA sites.
  * Some of those motifs will contain ambiguous bases and some will not
* You submit those motifs to this program
* This program then stitches these motifs together in random order
* Motifs may contain ambiguous bases per the IUPAC nucleotide code
  * We can't synthesize lots of ambiguous bases, so we "de-ambigulate" them before putting them into the final construct.
  * De-ambigulation happens according to 1 of 2 rules:
    * Rule 1:
      * Make K copies of each completely "de-ambigulated" variant: E.g. the sequence "SATC" will then be treated as 2 sequences: "GATC" and "CTAC" that will each appear in K copies.
    * Rule 2:
      * Pick L random variants of the motif. E.g. Motif ATGNNTTA have a total of 16 possible actual sequences. If L<16 then the program will random pick L variants (without duplicates). If L>16 then each possible variant will be picked at least L/16 times and some will be picked 1 more than that.
* We put M N's between each motif
* And the program will output P versions of these cassettes
* You then clone this cassette into a plasmid with 1 DNA MTase in each plasmid.
* You then transform this library into an organism that doesnt natively methylate DNA.
* Grow, Harvest, Sequence plasmids.
* ?
* Profit?  


## Motif file format
* The motifs should be stored in a standard text file
* One motif per line, then a comma then a 1 or a 2 to indicate whether either rule 1 or 2 should be used for this motif
  Example:  
  ATGCATGCATGC, 1  
  STGCAGTCATCGTTK, 1  
  ATCNNNNAAA, 2  
  CGTAGCANNNATCGATGC, 2  
  

### IUPAC nucleotide code:
|code | nucs|
|:---:|:---:|
|R|A or G|
|Y|	C or T  
|S|	G or C  
|W|	A or T  
|K|	G or T  
|M|	A or C  
|B|	C or G or T  
|D|	A or G or T  
|H|	A or C or T  
|V|	A or C or G  
|N|	any base  
