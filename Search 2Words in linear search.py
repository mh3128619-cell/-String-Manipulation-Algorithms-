def search_word_2d(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                
                if c + word_len <= cols:
                    match_h = True
                    for i in range(word_len):
                        if grid[r][c + i] != word[i]:
                            match_h = False
                            break
                    if match_h: return f"Found horizontally at ({r}, {c})"
                
                if r + word_len <= rows:
                    match_v = True
                    for i in range(word_len):
                        if grid[r + i][c] != word[i]:
                            match_v = False
                            break
                    if match_v: return f"Found vertically at ({r}, {c})"
                    
    return -1

grid = [['a', 'b', 'c'], ['f', 'g', 'h'], ['i', 'j', 'k']]
print(search_word_2d(grid, "fgh"))
