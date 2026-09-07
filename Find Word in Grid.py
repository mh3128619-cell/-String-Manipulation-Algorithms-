def find_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)

    for r in range(rows):
        for c in range(cols - word_len + 1):
            match = True
            for i in range(word_len):
                if grid[r][c + i] != word[i]:
                    match = False
                    break
            
            if match:
                return f"Word found starting at location: ({r}, {c})"
    
    return -1

grid = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l']
]
word = "fgh"

print(find_word_in_grid(grid, word))
