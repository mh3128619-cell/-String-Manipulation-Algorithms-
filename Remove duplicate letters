def remove_duplicate_letters(s):
    stack = []
    seen = set()
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    for i, char in enumerate(s):
        if char not in seen:
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            stack.append(char)
            seen.add(char)
            
    return "".join(stack)

print(remove_duplicate_letters("cbacdcbc"))
