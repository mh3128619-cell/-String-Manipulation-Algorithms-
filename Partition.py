def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

nums = [10, 80, 30, 90, 40, 50, 70]
low = 0
high = len(nums) - 1

print(f"Original array: {nums}")
pivot_index = partition(nums, low, high)
print(f"Array after partition (pivot at index {pivot_index}): {nums}")

nums2 = [5, 3, 8, 4, 2, 7, 1, 6]
low2 = 0
high2 = len(nums2) - 1

print(f"\nOriginal array 2: {nums2}")
pivot_index2 = partition(nums2, low2, high2)
print(f"Array 2 after partition (pivot at index {pivot_index2}): {nums2}")
