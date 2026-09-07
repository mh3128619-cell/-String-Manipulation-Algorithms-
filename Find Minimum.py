def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1

    return nums[left]

nums = [4, 5, 6, 7, 0, 1, 2]
print(f"Minimum element: {find_min(nums)}")

nums_with_duplicates = [2, 2, 2, 0, 1]
print(f"Minimum element (with duplicates): {find_min(nums_with_duplicates)}")
