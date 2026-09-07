def removeElement(nums, val):
    k = 0
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
            
    return k

nums1 = [3, 2, 2, 3]
val1 = 3
print(f"Original array: {nums1}, Value to remove: {val1}")
new_length1 = removeElement(nums1, val1)
print(f"New length: {new_length1}, Array after removing elements: {nums1[:new_length1]}")

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
print(f"\nOriginal array: {nums2}, Value to remove: {val2}")
new_length2 = removeElement(nums2, val2)
print(f"New length: {new_length2}, Array after removing elements: {nums2[:new_length2]}")

nums3 = [1, 2, 3, 4, 5]
val3 = 6
print(f"\nOriginal array: {nums3}, Value to remove: {val3}")
new_length3 = removeElement(nums3, val3)
print(f"New length: {new_length3}, Array after removing elements: {nums3[:new_length3]}")

nums4 = [7, 7, 7, 7]
val4 = 7
print(f"\nOriginal array: {nums4}, Value to remove: {val4}")
new_length4 = removeElement(nums4, val4)
print(f"New length: {new_length4}, Array after removing elements: {nums4[:new_length4]}")
