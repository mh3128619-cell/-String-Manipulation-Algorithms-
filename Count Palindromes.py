def count_palindromes(s):
    total = 0
    for i in range(len(s)):
        total += expand(s, i, i)
        total += expand(s, i, i + 1)
    return total

def expand(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count

print(count_palindromes("aaa"))
