def bubble_sort_even_odd(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] % 2 != 0) and (arr[j + 1] % 2 == 0):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_list = [3, 8, 5, 2]
print(f"Sorted (even first): {bubble_sort_even_odd(my_list)}")
