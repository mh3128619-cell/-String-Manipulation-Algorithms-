def firstMissingPositive(nums):
    n = len(nums)
    
    for i in range(n):
        while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
            
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
            
    return n + 1 

nums1 = [1, 2, 0]
print(f"Original array: {nums1}")
print(f"First missing positive: {firstMissingPositive(nums1)}") 

nums2 = [3, 4, -1, 1]
print(f"\nOriginal array: {nums2}")
print(f"First missing positive: {firstMissingPositive(nums2)}") 

nums3 = [7, 8, 9, 11, 12]
print(f"\nOriginal array: {nums3}")
print(f"First missing positive: {firstMissingPositive(nums3)}") 

nums4 = [1]
print(f"\nOriginal array: {nums4}")
print(f"First missing positive: {firstMissingPositive(nums4)}") 

nums5 = [2]
print(f"\nOriginal array: {nums5}")
print(f"First missing positive: {firstMissingPositive(nums5)}")
