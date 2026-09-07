def remove_duplicates_case_sensitive(s):
    seen = set()
    result = ""
    
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
            
    return result

input_str = "AaBbAa"
print(remove_duplicates_case_sensitive(input_str))
