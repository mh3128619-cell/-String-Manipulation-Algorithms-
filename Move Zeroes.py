def moveZeroes(nums):
    last_non_zero_found_at = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

nums1 = [0, 1, 0, 3, 12]
print(f"Original array: {nums1}")
moveZeroes(nums1)
print(f"Array after moving zeroes: {nums1}")

nums2 = [0, 0, 1]
print(f"\nOriginal array: {nums2}")
moveZeroes(nums2)
print(f"Array after moving zeroes: {nums2}")

nums3 = [1, 0]
print(f"\nOriginal array: {nums3}")
moveZeroes(nums3)
print(f"Array after moving zeroes: {nums3}")

nums4 = [1, 2, 3]
print(f"\nOriginal array: {nums4}")
moveZeroes(nums4)
print(f"Array after moving zeroes: {nums4}")

nums5 = [0]
print(f"\nOriginal array: {nums5}")
moveZeroes(nums5)
print(f"Array after moving zeroes: {nums5}")
