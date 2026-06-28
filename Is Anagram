def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for char in s1:
        count[char] = count.get(char, 0) + 1
        
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        
    for val in count.values():
        if val != 0:
            return False
            
    return True

print(is_anagram("Listen", "Silent"))
print(is_anagram("Rat", "Car"))
