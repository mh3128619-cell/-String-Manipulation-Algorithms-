def reverse_str(s, k):
    s_list = list(s)
    n = len(s_list)
    
    for i in range(0, n, 2 * k):
        start = i
        end = min(i + k, n)
        s_list[start:end] = s_list[start:end][::-1]
        
    return "".join(s_list)

print(reverse_str("abcdefg", 2))
