def search_diagonal(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    
    for r in range(rows):
        for c in range(cols):
            if r + word_len <= rows and c + word_len <= cols:
                match = True
                for i in range(word_len):
                    if grid[r + i][c + i] != word[i]:
                        match = False
                        break
                if match:
                    return f"Found diagonally starting at ({r}, {c})"
    return -1

grid = [
    ['f', 'b', 'c'],
    ['a', 'g', 'h'],
    ['i', 'j', 'h']
]

print(search_diagonal(grid, "fgh"))
