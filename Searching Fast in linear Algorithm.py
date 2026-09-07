def search_in_matrix_fast(matrix, target):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if matrix[row_index][col_index] == target:
                return (row_index, col_index)
    return -1

matrix = [
    [10, 50, 30],
    [50, 20, 60],
    [70, 80, 90]
]

result = search_in_matrix_fast(matrix, 50)
print(f"Element found at location: {result}")

result_not_found = search_in_matrix_fast(matrix, 99)
print(f"Search result for missing number: {result_not_found}")
