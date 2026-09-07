def findKthLargest(nums, k):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_nums = merge_sort(nums)

    return sorted_nums[-k]


numbers = [3, 2, 1, 5, 6, 4]
k_value = 2
print(f"Original numbers: {numbers}")
print(f"The {k_value}th largest number is: {findKthLargest(numbers, k_value)}")

numbers_2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k_value_2 = 4
print(f"\nOriginal numbers: {numbers_2}")
print(f"The {k_value_2}th largest number is: {findKthLargest(numbers_2, k_value_2)}")
