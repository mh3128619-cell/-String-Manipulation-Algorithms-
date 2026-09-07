def remove_duplicates(s):
    if not s:
        return ""
    
    result = ""
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            result += s[i]
            
    result += s[-1]
    
    return result

input_str = "aaabbbcccdd"
print(remove_duplicates(input_str))
