def reverse_string_manually(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
        
    return "".join(chars)

def reverse_each_word(sentence):
    words = sentence.split()
    reversed_words = []
    
    for word in words:
        reversed_words.append(reverse_string_manually(word))
    
    return " ".join(reversed_words)

input_text = "Hello World from Python"
print(reverse_each_word(input_text))
