def most_repeated_char(text):
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_repeated = max(char_count, key=char_count.get)
    
    return most_repeated

result = most_repeated_char("apple")
print(f"The most repeated character is: {result}")
