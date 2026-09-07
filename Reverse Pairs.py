def reversePairs(nums):
    def merge_and_count(arr):
        if len(arr) <= 1:
            return 0, arr

        mid = len(arr) // 2
        left_count, left_half = merge_and_count(arr[:mid])
        right_count, right_half = merge_and_count(arr[mid:])

        count = left_count + right_count

        j = 0
        for i in range(len(left_half)):
            while j < len(right_half) and left_half[i] > 2 * right_half[j]:
                j += 1
            count += j

        merged_arr = []
        i = 0
        j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                merged_arr.append(left_half[i])
                i += 1
            else:
                merged_arr.append(right_half[j])
                j += 1
        merged_arr.extend(left_half[i:])
        merged_arr.extend(right_half[j:])

        return count, merged_arr

    result_count, _ = merge_and_count(nums)
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
