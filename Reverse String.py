def reverse_string(s):
    if len(s) <= 1:
        return s
    
    return reverse_string(s[1:]) + s[0]

word = "Mohamed"
print(f"Original word: {word}")
print(f"Reversed word: {reverse_string(word)}")
