def find_kth_positive(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k

arr = [2, 3, 4, 7, 11]
k = 5
result = find_kth_positive(arr, k)
print(f"The {k}th missing positive integer is: {result}")
