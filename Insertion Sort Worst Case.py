def insertion_sort_worst_case(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Current element being sorted: {key}")
        while j >= 0 and arr[j] > key:
            print(f"  - Shifting {arr[j]} to the right for {key}")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Array after this step: {arr}")
        print("-" * 40)
    return arr

numbers = [100, 80, 60, 40, 20]
sorted_numbers = insertion_sort_worst_case(numbers)
print(f"Final sorted array: {sorted_numbers}")
