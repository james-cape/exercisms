def to_rna(dna_strand):
    replacements = { 'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U' }
    string = ""
    for letter in dna_strand:
        string += letter.replace(letter, replacements[letter])
    return string
