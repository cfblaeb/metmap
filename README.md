#CURRENT RULES: TO BE CHANGED WHEN TORBJØRN GIVES YOU MORE INFO
>2N'er = ambiguous ellers non-ambigious
ambigious = 12 random kopier
non-ambigious = 10 kopier af alle varianter
Åbenlyse spørgsmål/issues:
Skal ATVVVAT virkelig laves i 3^3 * 10 = 270 kopier mens ATNNNAT kun skal laves i 12?


# metmap
DNA methyltransferase binding motif plasmid assembler

## Overall purpose:
* To identify the motifs of multiple DNA methyltransferases (DNA MTase) simultaneously.

## Overview (example project):
* You have an organism with multiple identified DNA MTases and you wish to know their individual motifs.
* You use NGS to obtain motifs of all methylated DNA sites.
  * Some of those motifs will contain ambiguous bases and some will not
* You submit those motifs to this program
* This program then:
   * stitches together in random order:
     * K copies of motifs containing ambiguous bases
       * The output will be "de-ambigulated" (not contain ambiguous bases). E.g. Motif ATGNNTTA have a total of 16 possible actual sequences. If K<16 then the program will random pick K variants (without duplicates). If K>16 then each possible variant will be picked at least K/16 times and some will be picked 1 more than that.
     * L copies of motifs NOT containing ambiguous bases
       * These motifs CAN contain ambiguous bases but e.g. the sequence "SATC" will then be treated as 2 sequences: "GATC" and "CTAC" that will each appear in L copies. 
   * puts 1 N between each motif
   * It will produce M of these cassettes
   * It will try to make them fulfill requirements for IDT gBlock synthesis, but since I don't have a clear list of what those are, that may fail.
* You then clone this casette into a plasmid with 1 DNA MTase in each plasmid. 
* You then transform this library into an organism that doesnt natively methylate DNA.
* Grow, Harvest, Sequence plasmids.
* ?
* Profit?  


## Motif file format
* The motifs should be stored in a standard text file with one motif per line
* If the motif contains a group of N's it will be treated as a promiscuous
  Example:  
  ATGCATGCATGC
  STGCAGTCATCGTTK    
  ATCNNNNAAA            <---  
  CGTAGCANNNATCGATGC  
  
## Possibly gBlock synthesis issues:
* extremely low or high GC content (less than 25% and greater than 75%)
* homopolymeric runs of 10 or more As and Ts or 6 or more Gs and Cs
* Other structural motifs such as repeats or hairpins
* 125-3000 bp


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