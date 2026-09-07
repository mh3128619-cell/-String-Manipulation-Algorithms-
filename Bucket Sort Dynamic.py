def bucket_sort_dynamic(arr, num_buckets=3):
    if not arr: return arr
    
    min_val, max_val = min(arr), max(arr)
    data_range = max_val - min_val
    
    if data_range == 0: return arr 
    
    buckets = [[] for _ in range(num_buckets)]
    
    for num in arr:
        index = int((num - min_val) / (data_range / num_buckets))
        if index == num_buckets:
            index -= 1
        buckets[index].append(num)
    
    result = []
    for b in buckets:
        result.extend(sorted(b))
    return result

nums = [10, 10, 10, 50, 50, 50, 90, 90]
print(f"Dynamically bucket sorted array: {bucket_sort_dynamic(nums)}")
