def split_array(nums, k):
    def can_split(max_sum_allowed):
        subarrays = 1
        current_sum = 0
        
        for num in nums:
            current_sum += num
            if current_sum > max_sum_allowed:
                subarrays += 1
                current_sum = num
                
        return subarrays <= k

    low = max(nums)
    high = sum(nums)
    
    while low < high:
        mid = (low + high) // 2
        
        if can_split(mid):
            high = mid
        else:
            low = mid + 1
            
    return low

nums = [5, 5, 5, 5, 5]
k = 2
print(f"Minimum Largest Sum: {split_array(nums, k)}")
