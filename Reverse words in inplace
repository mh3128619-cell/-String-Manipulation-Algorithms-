def reverse_words_inplace(s):
    # Convert string to list because strings are immutable
    chars = list(s)
    n = len(chars)
    
    # 1. Reverse the entire string
    def reverse_range(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    reverse_range(chars, 0, n - 1)
    
    # 2. Reverse each word individually
    start = 0
    for end in range(n + 1):
        # If we reach a space or the end of the array, it means a word has ended
        if end == n or chars[end] == ' ':
            reverse_range(chars, start, end - 1)
            start = end + 1
            
    return "".join(chars)

# Test the code
input_str = "the sky is blue"
result = reverse_words_inplace(input_str)
print(f'Input: "{input_str}"')
print(f'Output: "{result}"')
# Output should be: "blue is sky the"
