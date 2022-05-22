def read_file(input_name):
    sequence = ''
    with open(input_name) as input_file:
        input_file.readline()
        while True:
            seq = input_file.readline().strip()
            if len(seq) == 0:
                break
            sequence += seq
    return sequence

def reverse_complement(sequence):
    complement_seq = ""
    complement_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for letter in sequence:
        complement_seq += complement_dict[letter]
    return complement_seq[::-1]

def find_start_end(gene, variant):
    # using find to find the start index
    # start index + length of gene to find the end index
    indices = []
    count = 0
    index = variant.find(gene)
    # print(f'index before entering while loop: {index}')
    while index >= 0:
        # print(f'entered while loop')
        indices.append((index+1, index+len(gene)+1))  # bp locations of genes reported by databases start from 1
        count += 1
        if count % 10:
            print(f'found at index {index}, len(variant): {len(variant)}')
        index = variant.find(gene, index + len(gene))
    return indices

input_name1 = 'Forrest B100B10 BAC sequence Rhg4.txt'
input_name2 = 'Forrest SHMT.txt'
forrest_sequence = read_file(input_name1)
print(f'First 50 nucleotides of Forrest sequence: {forrest_sequence[:50]}')
shmt = read_file(input_name2)
print(f'First 50 nucleotides of SHMT gene sequence: {shmt[:50]}')
sequence = shmt[2340:3657]
variant = forrest_sequence
gene = reverse_complement(sequence)
boundary_indices = find_start_end(gene, variant)
print(f'boundary_indices: {boundary_indices}')