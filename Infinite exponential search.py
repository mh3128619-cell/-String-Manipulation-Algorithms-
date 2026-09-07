def binary_search(arr, l, r, target):
    while l <= r:
        mid = l + (r - l) // 2
        try:
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        except IndexError:
            r = mid - 1
    return -1

def exponential_search_infinite(arr, target):
    try:
        if arr[0] == target:
            return 0
    except IndexError:
        return -1

    i = 1
    try:
        while i < float('inf') and arr[i] <= target:
            i *= 2
    except IndexError:
        pass

    return binary_search(arr, i // 2, i, target)

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = exponential_search_infinite(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
