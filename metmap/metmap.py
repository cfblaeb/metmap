from random import choice

# IUPAC nucleotide code
dnc = {
    'R': ['A', 'G'],
    'Y': ['C', 'T'],
    'S': ['G', 'C'],
    'W': ['A', 'T'],
    'K': ['G', 'T'],
    'M': ['A', 'C'],
    'B': ['C', 'G', 'T'],
    'D': ['A', 'G', 'T'],
    'H': ['A', 'C', 'T'],
    'V': ['A', 'C', 'G'],
    'N': ['A', 'T', 'C', 'G']
}


def deambigulate_random(seq: str) -> str:
    """
    Create 1 random variant of seq
    :param seq: A DNA sequence using ATCG or IUPAC degenerate code
    :return: a random deambigulated version of seq
    """
    return [n if n in dnc['N'] else choice(dnc[n]) for n in seq.upper()]


def deambigulate_all(seq: str, start_pos: int = 0) -> str:
    """
    create all variants of seq
    :param seq: A DNA sequence using ATCG or IUPAC degenerate code
    :param start_pos:
    :return: A list of all variants
    """
    clean = True
    for i, nuc in enumerate(seq[start_pos:].upper()):
        if nuc in dnc:
            clean = False
            for snuc in dnc[nuc]:
                deamb = seq[:i+start_pos] + snuc + seq[i+start_pos+1:]
                for x in deambigulate_all(deamb, i+start_pos+1):
                    yield x
            break
    if clean:
        yield seq



def do_it_all(motif_file, copy_nonambig: int=10, copy_ambig: int=12,  nresults: int=1):
    """
    :param motif_file: a file in a format that i need to come up with
    :param copy_nonambig: Copies of each de-ambigulated sequence generated from motifs with less than 2 N's.
    :param copy_ambig: Copies in total of motifs with 2 or more N's.
    :param nresults: number of motif assemblies to output
    return: actual results
    """
    # read file to list
    raw_motifs = [x.strip() for x in motif_file.readlines()]
    # go over motifs and identify ambig and non-ambig and de-ambigulate the non-ambigs and randomize the ambigs
    motifs = []
    for motif in raw_motifs:
        if motif.count('N') >= 2:  # we have an ambig. Create random copies
            random_ambigs = []
            potential

    print(motifs)

    results = ["fakse"]
    print(copy_ambig)
    print(copy_nonambig)
    print(nresults)

    return results
