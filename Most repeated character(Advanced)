def most_repeated_char_advanced(text):
    text = text.lower()
    
    char_count = {}
    
    for char in text:
        if char == " ":
            continue
            
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    if not char_count:
        return None
        
    most_repeated = max(char_count, key=char_count.get)
    
    return most_repeated

input_text = "Apple Tree"
result = most_repeated_char_advanced(input_text)
print(f"The most repeated character in '{input_text}' is: '{result}'")
