def bucket_sort_integers(arr, num_buckets=5):
    max_val = max(arr)
    range_per_bucket = (max_val + 1) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int(num / range_per_bucket)
        buckets[index].append(num)

    result = []
    for b in buckets:
        result.extend(sorted(b))
    return result

nums = [20, 10, 55, 99, 41, 15, 88]
print(f"Sorted array: {bucket_sort_integers(nums)}")
