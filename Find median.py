def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    n, m = len(nums1), len(nums2)
    left, right = 0, n

    while left <= right:
        part_x = (left + right) // 2
        part_y = (n + m + 1) // 2 - part_x

        max_left_x = float('-inf') if part_x == 0 else nums1[part_x - 1]
        min_right_x = float('inf') if part_x == n else nums1[part_x]

        max_left_y = float('-inf') if part_y == 0 else nums2[part_y - 1]
        min_right_y = float('inf') if part_y == m else nums2[part_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (n + m) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            right = part_x - 1
        else:
            left = part_x + 1

nums1 = [1, 3]
nums2 = [2]
print(f"Median 1: {find_median_sorted_arrays(nums1, nums2)}")

nums1 = [1, 2]
nums2 = [3, 4]
print(f"Median 2: {find_median_sorted_arrays(nums1, nums2)}")
