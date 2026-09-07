def maximumGap(nums):
    if len(nums) < 2:
        return 0
    
    low, high, n = min(nums), max(nums), len(nums)
    if low == high:
        return 0
    
    bucket_size = max(1, (high - low) // (n - 1))
    num_buckets = (high - low) // bucket_size + 1
    
    buckets_min = [float('inf')] * num_buckets
    buckets_max = [float('-inf')] * num_buckets
    
    for x in nums:
        idx = (x - low) // bucket_size
        buckets_min[idx] = min(buckets_min[idx], x)
        buckets_max[idx] = max(buckets_max[idx], x)
    
    max_gap = 0
    prev_max = low
    
    for i in range(num_buckets):
        if buckets_min[i] == float('inf'):
            continue
        max_gap = max(max_gap, buckets_min[i] - prev_max)
        prev_max = buckets_max[i]
        
    return max_gap

nums1 = [3, 6, 9, 1]
print(f"Original array: {nums1}")
print(f"Maximum gap: {maximumGap(nums1)}")

nums2 = [10]
print(f"\nOriginal array: {nums2}")
print(f"Maximum gap: {maximumGap(nums2)}")

nums3 = [1,1,1,1]
print(f"\nOriginal array: {nums3}")
print(f"Maximum gap: {maximumGap(nums3)}")

nums4 = [1, 5, 10]
print(f"\nOriginal array: {nums4}")
print(f"Maximum gap: {maximumGap(nums4)}")
