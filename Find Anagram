def findAnagrams(s, p):
    res = []
    p_len, s_len = len(p), len(s)
    
    if p_len > s_len:
        return []
    
    p_count = {}
    s_count = {}
    
    for i in range(p_len):
        p_count[p[i]] = p_count.get(p[i], 0) + 1
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        
    if p_count == s_count:
        res.append(0)
        
    for i in range(p_len, s_len):
        new_char = s[i]
        s_count[new_char] = s_count.get(new_char, 0) + 1
        
        old_char = s[i - p_len]
        if s_count[old_char] == 1:
            del s_count[old_char]
        else:
            s_count[old_char] -= 1
            
        if s_count == p_count:
            res.append(i - p_len + 1)
            
    return res

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
