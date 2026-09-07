def find_peak_element(nums):
    low = 0
    high = len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
            
    return low

nums = [10, 2, 1, 3, 0]
peak_index = find_peak_element(nums)
print(f"Peak index: {peak_index}, Peak value: {nums[peak_index]}")
