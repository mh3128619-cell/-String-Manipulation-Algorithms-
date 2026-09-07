def reversePairs(nums):
    def merge_sort_and_count(arr_indices):
        if len(arr_indices) <= 1:
            return 0, arr_indices

        mid = len(arr_indices) // 2
        left_count, left_half_indices = merge_sort_and_count(arr_indices[:mid])
        right_count, right_half_indices = merge_sort_and_count(arr_indices[mid:])

        count = left_count + right_count

        j = 0
        for i in range(len(left_half_indices)):
            while j < len(right_half_indices) and nums[left_half_indices[i]] > 2 * nums[right_half_indices[j]]:
                j += 1
            count += j

        merged_indices = []
        i = 0
        j = 0
        while i < len(left_half_indices) and j < len(right_half_indices):
            if nums[left_half_indices[i]] <= nums[right_half_indices[j]]:
                merged_indices.append(left_half_indices[i])
                i += 1
            else:
                merged_indices.append(right_half_indices[j])
                j += 1
        merged_indices.extend(left_half_indices[i:])
        merged_indices.extend(right_half_indices[j:])

        return count, merged_indices

    initial_indices = list(range(len(nums)))
    result_count, _ = merge_sort_and_count(initial_indices)
    return result_count

nums1 = [1, 3, 2, 3, 1]
print(f"Original array: {nums1}")
print(f"Number of reverse pairs: {reversePairs(nums1)}")

nums2 = [2, 4, 3, 5, 1]
print(f"\nOriginal array: {nums2}")
print(f"Number of reverse pairs: {reversePairs(nums2)}")

nums3 = [5, 4, 3, 2, 1]
print(f"\nOriginal array: {nums3}")
print(f"Number of reverse pairs: {reversePairs(nums3)}")
