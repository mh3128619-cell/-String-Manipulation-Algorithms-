def find_all_patterns(grid, word):
    word = word.lower()
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    results = []

    def check(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc].lower() != word[i]:
                return False
        return True

    directions = [(0, 1), (1, 0), (1, 1), (-1, -1)]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check(r, c, dr, dc):
                    results.append({"start": (r, c), "direction": (dr, dc)})
    
    return results if results else -1

grid = [
    ['A', 'b', 'c', 'd'],
    ['e', 'F', 'g', 'h'],
    ['i', 'j', 'G', 'l'],
    ['m', 'n', 'o', 'H']
]
word = "fgh"
print(find_all_patterns(grid, word))
