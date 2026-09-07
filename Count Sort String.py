def count_sort_string(text):
    count = [0] * 26
    
    for char in text:
        index = ord(char) - ord('a')
        count[index] += 1
        
    sorted_chars = []
    for i in range(26):
        char = chr(i + ord('a'))
        sorted_chars.append(char * count[i])
        
    return "".join(sorted_chars)

word = "banana"
print(f"Sorted word: {count_sort_string(word)}")
