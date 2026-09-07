def binary_search(arr, l, r, target):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
        
    return binary_search(arr, i // 2, min(i, len(arr) - 1), target)

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = exponential_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
