def reverse_words_cleaned(s):
    words = s.split()
    
    left = 0
    right = len(words) - 1
    
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
        
    return " ".join(words)

input_text = "  hello   world  "
print(f"'{reverse_words_cleaned(input_text)}'")
