def find_longest_palindrome(s: str) -> str:
    longest = ""
    
    def get_palindrome_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(len(s)):
        p1 = get_palindrome_from_center(i, i)
        if len(p1) > len(longest):
            longest = p1
            
        p2 = get_palindrome_from_center(i, i + 1)
        if len(p2) > len(longest):
            longest = p2
            
    return longest

text = "The racecar is fast, but malayalam is a language"
print(f"The longest palindrome is: {find_longest_palindrome(text)}")
