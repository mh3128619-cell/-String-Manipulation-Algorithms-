def kthSmallest(matrix, k):
    n = len(matrix)
    low = matrix[0][0]
    high = matrix[n-1][n-1]
    
    while low < high:
        mid = low + (high - low) // 2
        count = get_count_less_equal(matrix, mid)
        
        if count < k:
            low = mid + 1
        else:
            high = mid
            
    return low

def get_count_less_equal(matrix, target):
    count = 0
    n = len(matrix)
    row = n - 1
    col = 0
    
    while row >= 0 and col < n:
        if matrix[row][col] <= target:
            count += (row + 1)
            col += 1
        else:
            row -= 1
            
    return count 

matrix1 = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k1 = 8
print(f"Matrix: {matrix1}")
print(f"The {k1}th smallest element is: {kthSmallest(matrix1, k1)}") 

matrix2 = [
    [-5]
]
k2 = 1
print(f"\nMatrix: {matrix2}")
print(f"The {k2}th smallest element is: {kthSmallest(matrix2, k2)}") 

matrix3 = [
    [1,2],
    [1,3]
]
k3 = 2
print(f"\nMatrix: {matrix3}")
print(f"The {k3}th smallest element is: {kthSmallest(matrix3, k3)}") 
