def most_repeated_letters(text):
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
            
    if not char_count:
        return "No letters in this text!"
        
    max_val = max(char_count.values())
    
    result = [char for char, count in char_count.items() if count == max_val]
    
    return result

my_text = "Hello, World! 123"
print(f"Result: {most_repeated_letters(my_text)}")
