def countSmaller(nums):
    n = len(nums)
    result = [0] * n
    indices = list(range(n))

    def merge_sort(left, right):
        if right - left <= 1:
            return indices[left:right]
        
        mid = (left + right) // 2
        left_part = merge_sort(left, mid)
        right_part = merge_sort(mid, right)
        
        return merge(left_part, right_part)

    def merge(left_part, right_part):
        merged = []
        i = j = 0
        right_count = 0
        
        while i < len(left_part) and j < len(right_part):
            if nums[left_part[i]] <= nums[right_part[j]]:
                result[left_part[i]] += right_count
                merged.append(left_part[i])
                i += 1
            else:
                right_count += 1
                merged.append(right_part[j])
                j += 1
        
        while i < len(left_part):
            result[left_part[i]] += right_count
            merged.append(left_part[i])
            i += 1
            
        merged.extend(right_part[j:])
        return merged

    merge_sort(0, n)
    return result

nums1 = [5, 2, 6, 1]
print(f"Original array: {nums1}")
print(f"Smaller elements to the right: {countSmaller(nums1)}")

nums2 = [-1]
print(f"\nOriginal array: {nums2}")
print(f"Smaller elements to the right: {countSmaller(nums2)}")

nums3 = [-1, -1]
print(f"\nOriginal array: {nums3}")
print(f"Smaller elements to the right: {countSmaller(nums3)}")
