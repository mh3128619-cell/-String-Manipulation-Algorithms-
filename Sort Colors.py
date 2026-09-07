def sortColors(nums):
    low = 0
    current = 0
    high = len(nums) - 1

    while current <= high:
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            low += 1
            current += 1
        elif nums[current] == 2:
            nums[high], nums[current] = nums[current], nums[high]
            high -= 1
        else:
            current += 1

nums1 = [2, 0, 2, 1, 1, 0]
print(f"Original array: {nums1}")
sortColors(nums1)
print(f"Sorted array: {nums1}")

nums2 = [2, 0, 1]
print(f"\nOriginal array: {nums2}")
sortColors(nums2)
print(f"Sorted array: {nums2}")

nums3 = [0]
print(f"\nOriginal array: {nums3}")
sortColors(nums3)
print(f"Sorted array: {nums3}")

nums4 = [1]
print(f"\nOriginal array: {nums4}")
sortColors(nums4)
print(f"Sorted array: {nums4}")

nums5 = []
print(f"\nOriginal array: {nums5}")
sortColors(nums5)
print(f"Sorted array: {nums5}")
