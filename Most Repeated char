def most_repeated_chars_hard(text):
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char == " ":
            continue
        char_count[char] = char_count.get(char, 0) + 1
            
    if not char_count:
        return []

    max_val = max(char_count.values())
    
    result = []
    for char, count in char_count.items():
        if count == max_val:
            result.append(char)
            
    return result

input_text = "aabbc"
result = most_repeated_chars_hard(input_text)
print(f"The most repeated characters are: {result}")
