import tkinter as tk

def validate_input(char):
    if char in 'ATGC':
        return True
    else:
        return False

def validate_dna_sequence(sequence):
    valid_chars = set("ATGC")
    if not all(char in valid_chars for char in sequence):
        return False
    return True

def convert_to_mrna(dna_sequence):
    mrna_strand = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    mrna_sequence = ''.join(mrna_strand[base] for base in dna_sequence)
    return mrna_sequence

def get_complementary_strand(dna_sequence):
    base_complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complementary_strand = ''.join(base_complement[base] for base in dna_sequence)
    return complementary_strand

def get_tRNA_sequence(dna_sequence):
    trna_sequence = dna_sequence.replace("T", "U")
    return trna_sequence

def get_protein_sequence(mrna_sequence):
    codon_table = {
        'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAU': 'Tyr', 'UAC': 'Tyr', 'CAU': 'His', 'CAC': 'His',
        'CAA': 'Gln', 'CAG': 'Gln', 'AAU': 'Asn', 'AAC': 'Asn',
        'AAA': 'Lys', 'AAG': 'Lys', 'GAU': 'Asp', 'GAC': 'Asp',
        'GAA': 'Glu', 'GAG': 'Glu', 'UGU': 'Cys', 'UGC': 'Cys',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AGA': 'Arg', 'AGG': 'Arg', 'AGU': 'Ser', 'AGC': 'Ser',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
        'UGG': 'Trp', 'UGA': 'STOP', 'UAA': 'STOP', 'UAG': 'STOP',
        # Add more codons as needed
    }

    protein_sequence = []
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3]
        if codon in codon_table and codon_table[codon] != 'STOP':
            protein_sequence.append(codon_table[codon])
        else:
            break

    return '-'.join(protein_sequence)

def process_sequence():
    dna_input = entry_dna_sequence.get().upper()

    if validate_dna_sequence(dna_input):
        mrna_sequence = convert_to_mrna(dna_input)
        complementary_strand = get_complementary_strand(dna_input)
        trna_sequence = get_tRNA_sequence(dna_input)
        protein_sequence = get_protein_sequence(mrna_sequence)

        text_mrna_sequence.config(text="mRNA Sequence: " + mrna_sequence)
        text_complementary_strand.config(text="Complementary Strand: " + complementary_strand)
        text_trna_sequence.config(text="tRNA Sequence: " + trna_sequence)
        text_protein_sequence.config(text="Protein Sequence: " + protein_sequence)
    else:
        text_mrna_sequence.config(text="Invalid input. Please use only A, T, G, C characters.")
        text_complementary_strand.config(text="")
        text_trna_sequence.config(text="")
        text_protein_sequence.config(text="")

# Create the main application window
root = tk.Tk()
root.title("DNA Sequence Processor")

# Create and place widgets
label_dna_sequence = tk.Label(root, text="Enter a DNA sequence (A, T, G, C only) (Turn on capslock):")
label_dna_sequence.pack()

validate_input_cmd = root.register(validate_input)
entry_dna_sequence = tk.Entry(root, validate='key', validatecommand=(validate_input_cmd, '%S'))
entry_dna_sequence.pack()

button_process = tk.Button(root, text="Process Sequence", command=process_sequence)
button_process.pack()

text_mrna_sequence = tk.Label(root, text="")
text_mrna_sequence.pack()

text_complementary_strand = tk.Label(root, text="")
text_complementary_strand.pack()

text_trna_sequence = tk.Label(root, text="")
text_trna_sequence.pack()

text_protein_sequence = tk.Label(root, text="")
text_protein_sequence.pack()

root.mainloop()
