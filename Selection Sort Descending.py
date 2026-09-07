def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

numbers = [11, 22, 12, 25, 64]
print(f"Descending order: {selection_sort_descending(numbers)}")
