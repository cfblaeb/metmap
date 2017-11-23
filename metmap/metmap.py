from random import choice, shuffle
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import IUPACUnambiguousDNA

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


def calculate_number_of_possible_variants(seq: str) -> int:
    """

    :param seq:
    :return:
    """
    res = 1
    for x in [len(dnc[x]) for x in seq if x in dnc]:
        res *= x
    return res


def deambigulate_random(seq: str) -> str:
    """
    Create 1 random variant of seq
    :param seq: A DNA sequence using ATCG or IUPAC degenerate code
    :return: a random deambigulated version of seq
    """
    return "".join([n if n in dnc['N'] else choice(dnc[n]) for n in seq.upper()])


def pick_n_random_without_duplicates(seq: str, n: int) -> set:
    # sanity check
    max_variants = calculate_number_of_possible_variants(seq)
    if max_variants < n:
        raise ValueError(f"I can't possibly find {n} unique variants of {seq}. {max_variants} is max.")
    elif max_variants == n:
        return deambigulate_all(seq)
    else:
        picks = set()
        while len(picks) != n:
            picks.add(deambigulate_random(seq))
        return picks


def deambigulate_all(seq: str, start_pos: int = 0) -> list:
    """
    create all variants of seq
    :param seq: A DNA sequence using ATCG or IUPAC degenerate code
    :param start_pos: Used in the iterative process
    :return: A list of all variants
    """
    for i, nuc in enumerate(seq[start_pos:].upper()):  # go over each nuc
        if nuc in dnc:  # if ambiguous then dig deeper
            variants = []  # we store final results in this
            for snuc in dnc[nuc]:  # go over each mutant
                deamb = seq[:i+start_pos] + snuc + seq[i+start_pos+1:]  # new deambigulated sequence
                variants += deambigulate_all(deamb, i+start_pos+1)  # send it in again to check for additional ambiguity
            return variants  # final return of all the non-ambiguous sequences
    return [seq]  # if you got here you the endpoint of 1 completely deambigulated sequence


def generate_parts_for_cassette(motif_file, copy_rule1: int=10, copy_rule2: int=12) -> list:
    # read file to list
    raw_motifs = [[y.strip() for y in x.strip().split(",")] for x in motif_file.readlines()]

    # go over motifs and identify ambig and non-ambig and de-ambigulate the non-ambigs and randomize the ambigs
    motifs = []
    for i, (motif, rule) in enumerate(raw_motifs):
        how_many = calculate_number_of_possible_variants(motif)
        if rule == '1':
            print(f"{motif}: rule {rule}: {how_many} variants of which {copy_rule1} copies will be picked at random.")
            if how_many <= copy_rule1:  # make all variants, possibly more than once
                copies = copy_rule1 / how_many
                all_variants = [(motif, x) for x in deambigulate_all(motif)]
                adding = all_variants * int(copies)
                motifs += adding
                motifs += [(motif, x) for x in pick_n_random_without_duplicates(motif, copy_rule1 - len(adding))]
            else:
                motifs += [(motif, x) for x in pick_n_random_without_duplicates(motif, copy_rule1)]
        elif rule == '2':
            print(
                f"{motif}: rule {rule}: {how_many} variants which will each be added in {copy_rule2} copies. {copy_rule2*how_many} total.")
            if how_many > 10:
                print(
                    f"Warning: This motif will be deambigulated into {how_many} variants. Each variant will receive {copy_rule2} copies. Thats {copy_rule2*how_many} targets for just 1 methyltransferase!")
            motifs += [(motif, x) for x in deambigulate_all(motif)] * copy_rule2
        else:
            print(f"Rule not recognized for motif '{motif}' on line {i}: '{rule}'. Rule must be either 1 or 2.")

    return motifs


def shuffle_motifs(motif_list):
    motifs = motif_list.copy()  # stupid in place mutability
    searching_for_motif_order = True
    x = 0
    while searching_for_motif_order:
        x += 1
        print(f"Attempt {x} at finding valid motif order")

        # do naive shuffle
        shuffle(motifs)
        # check for repeat motifs
        bad_poss = [i for i, (motif, de_motif) in enumerate(motifs[:-1]) if motif == motifs[i + 1][0]]
        if not bad_poss:
            return motifs

        # attempt to fix bad positioned motifs
        # THIS METHOD WILL PLACE MORE PREVALENT MOTIFS IN THE LEFT END OF THE CASSETTE, POTENTIALLY A BAD THING FOR SYNTHESIS
        # ALTERNATIVE IS TO ATTEMPT TO RANDOMLY PLACE THE BAD ELEMENTS....but thats left as an exercise for the reader
        bad_elements = [motifs.pop(pos) for pos in bad_poss[::-1]]

        all_placed = True
        for (motif, de_motif) in bad_elements:
            placed = False
            for i, (mmotif, mde_motif) in enumerate(motifs):
                if i == 0:  # first pos
                    if motif != mde_motif:  # place here at first pos
                        motifs = [(motif, de_motif)] + motifs
                        placed = True
                        break
                elif i == len(motifs)-1:  # last pos
                    if motif != mde_motif:  # place at last pos
                        motifs.append((motif, de_motif))
                        placed = True
                        break
                else:  # middle pos
                    if motif != mde_motif and motif != motifs[i-1][0]:  # place between i-1 and i
                        motifs = motifs[:i] + [(motif, de_motif)] + motifs[i:]
                        placed = True
                        break
            if not placed:  # no possible position, start over
                all_placed = False
                break
        if all_placed:  # positions fixed
            return motifs


def do_it_all(motif_file, copy_rule1: int=10, copy_rule2: int=12,  how_many_Ns: int=1, nresults: int=1) -> list:
    """
    :param motif_file: a file in a format that i need to come up with
    :param copy_rule1: pick this many random variants
    :param copy_rule2: make each possible variant in this many copies
    :param how_many_Ns: How many N's between motifs?
    :param nresults: number of motif assemblies to output
    return: actual results
    """

    # generate de-ambigulated motifs in the right copy numbers
    motifs = generate_parts_for_cassette(motif_file, copy_rule1, copy_rule2)

    # shuffle motif positions in the cassette
    motif_set = set()
    while len(motif_set) != nresults:
        motif_set.add(tuple(shuffle_motifs(motifs)))

    cassette_strs = []
    for i, x in enumerate(motif_set):
        # link with N's
        cassette_str = SeqRecord(Seq("", IUPACUnambiguousDNA()), id=f"id_cassette_{i+1}", name=f"name_cassette_{i+1}", description=f"metmap generated cassette", annotations={'date': "08-MAR-1983"})
        current_pos = 0
        for (motif, de_motif) in x:
            cassette_str += deambigulate_random("N"*how_many_Ns)
            current_pos += how_many_Ns
            cassette_str += de_motif
            cassette_str.features.append(SeqFeature(FeatureLocation(current_pos, current_pos+len(de_motif)), type='misc_binding', qualifiers={'note': motif}))
            current_pos += len(de_motif)
        cassette_strs.append(cassette_str)
    return cassette_strs
