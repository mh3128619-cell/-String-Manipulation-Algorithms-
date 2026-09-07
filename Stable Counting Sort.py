def stable_counting_sort(arr):
    if not arr: return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(arr) - 1, -1, -1):
        current_element = arr[i]
        position = count[current_element] - 1
        output[position] = current_element
        count[current_element] -= 1

    return output

nums = [4, 2, 2, 8, 3]
print(f"Stable sorted: {stable_counting_sort(nums)}")
