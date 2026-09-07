import random

def findKthLargest(nums, k):
    target_index = len(nums) - k
    
    def quick_select(left, right):
        pivot_index = random.randint(left, right)
        pivot_value = nums[pivot_index]
        
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        if store_index == target_index:
            return nums[store_index]
        elif store_index > target_index:
            return quick_select(left, store_index - 1)
        else:
            return quick_select(store_index + 1, right)

    return quick_select(0, len(nums) - 1)

nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"Original array: {nums1}, k = {k1}")
print(f"The {k1}th largest element is: {findKthLargest(nums1, k1)}")

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(f"\nOriginal array: {nums2}, k = {k2}")
print(f"The {k2}th largest element is: {findKthLargest(nums2, k2)}")

nums3 = [1]
k3 = 1
print(f"\nOriginal array: {nums3}, k = {k3}")
print(f"The {k3}th largest element is: {findKthLargest(nums3, k3)}")
