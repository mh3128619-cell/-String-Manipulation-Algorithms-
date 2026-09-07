def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    
    for num in arr:
        index = int(10 * num)
        buckets[index].append(num)
    
    for i in range(10):
        buckets[i].sort()
        
    k = 0
    for i in range(10):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr

my_list = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21]
print(bucket_sort(my_list))
