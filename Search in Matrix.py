def search_in_matrix(matrix, target):
    indices = []
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if matrix[row_index][col_index] == target:
                indices.append((row_index, col_index))
    return indices

matrix = [
    [10, 50, 30],
    [50, 20, 50],
    [70, 80, 50]
]
target = 50

results = search_in_matrix(matrix, target)

if results:
    print(f"The number {target} was found at the following locations: {results}")
    print(f"Total count: {len(results)}")
else:
    print("The number was not found in the matrix.")
