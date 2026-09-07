def bucket_sort_with_negatives(arr, num_buckets=3):
    if not arr: return arr
    
    min_val = min(arr)
    max_val = max(arr)
    
    shifted_arr = [x - min_val for x in arr]
    
    new_max = max(shifted_arr)
    range_per_bucket = (new_max + 1) / num_buckets
    buckets = [[] for _ in range(num_buckets)]
    
    for num in shifted_arr:
        index = int(num / range_per_bucket)
        buckets[index].append(num)
        
    result = []
    for b in buckets:
        result.extend(sorted(b))
    
    final_result = [x + min_val for x in result]
    return final_result

nums = [-5, 12, -10, 8, 2]
print(f"Sorted array with negatives: {bucket_sort_with_negatives(nums)}")
