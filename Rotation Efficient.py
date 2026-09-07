def is_rotation_efficient(dna, pattern):
    n = len(dna)
    m = len(pattern)
    
    if n != m:
        return False
    
    for start in range(n):
        match = True
        for i in range(n):
            if dna[(start + i) % n] != pattern[i]:
                match = False
                break
        
        if match:
            return True
            
    return False

dna_sequence = "ATCGGCTA"
virus_sample = "GGCTAATC"
print(f"Is it a rotation? {is_rotation_efficient(dna_sequence, virus_sample)}")
