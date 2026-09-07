def counting_sort(arr):
    max_val = max(arr)
    
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
        
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1
            
    return sorted_arr

my_list = [1, 4, 1, 2, 7, 5, 2]
result = counting_sort(my_list)
print(f"Sorted array: {result}")
