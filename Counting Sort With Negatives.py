def counting_sort_with_negatives(arr):
    if not arr: return arr

    max_val = max(arr)
    min_val = min(arr)
    
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    
    for num in arr:
        count[num - min_val] += 1
        
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i + min_val)
            count[i] -= 1
            
    return sorted_arr

nums = [3, -2, 0, -2, 5]
print(f"Sorted with negative numbers: {counting_sort_with_negatives(nums)}")
