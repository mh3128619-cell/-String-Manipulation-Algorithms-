def rotate_string(s, k):
    n = len(s)
    if n == 0:
        return s
    
    k = k % n
    result = s[k:] + s[:k]
    
    return result

print(rotate_string("abcde", 2))
print(rotate_string("abcde", 7))
