def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    low = 0
    high = rows * cols - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = matrix[mid // cols][mid % cols]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
print(f"Target found: {search_matrix(matrix, target)}")
