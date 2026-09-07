def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1_example = [1, 2, 3, 0, 0, 0]
m_example = 3
nums2_example = [2, 5, 6]
n_example = 3

print(f"Before merge: nums1 = {nums1_example}, nums2 = {nums2_example}")
merge(nums1_example, m_example, nums2_example, n_example)
print(f"After merge: nums1 = {nums1_example}")

nums1_example_2 = [4, 5, 6, 0, 0, 0]
m_example_2 = 3
nums2_example_2 = [1, 2, 3]
n_example_2 = 3

print(f"\nBefore merge: nums1 = {nums1_example_2}, nums2 = {nums2_example_2}")
merge(nums1_example_2, m_example_2, nums2_example_2, n_example_2)
print(f"After merge: nums1 = {nums1_example_2}")
