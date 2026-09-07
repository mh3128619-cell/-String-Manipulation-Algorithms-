def find_first_occurrence(nums, target):
    low = 0
    high = len(nums) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            result = mid
            high = mid - 1
        
        elif nums[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return result

nums = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(f"First occurrence index: {find_first_occurrence(nums, target)}")
