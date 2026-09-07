import collections
import random

def topKFrequent(nums, k):
    count = collections.Counter(nums)
    unique_elements = list(count.keys())
    
    def quick_select(left, right, k_smallest):
        if left == right:
            return
        
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return
        elif k_smallest < pivot_index:
            quick_select(left, pivot_index - 1, k_smallest)
        else:
            quick_select(pivot_index + 1, right, k_smallest)

    def partition(left, right, pivot_index):
        pivot_frequency = count[unique_elements[pivot_index]]
        unique_elements[pivot_index], unique_elements[right] = unique_elements[right], unique_elements[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if count[unique_elements[i]] < pivot_frequency:
                unique_elements[store_index], unique_elements[i] = unique_elements[i], unique_elements[store_index]
                store_index += 1
                
        unique_elements[right], unique_elements[store_index] = unique_elements[store_index], unique_elements[right]
        return store_index

    n = len(unique_elements)
    quick_select(0, n - 1, n - k)
    
    return unique_elements[n - k:] 

nums1 = [1,1,1,2,2,3]
k1 = 2
print(f"Original array: {nums1}, k = {k1}")
print(f"Top {k1} frequent elements: {topKFrequent(nums1, k1)}")

nums2 = [1]
k2 = 1
print(f"\nOriginal array: {nums2}, k = {k2}")
print(f"Top {k2} frequent elements: {topKFrequent(nums2, k2)}")

nums3 = [4,1,-1,2,-1,2,3]
k3 = 2
print(f"\nOriginal array: {nums3}, k = {k3}")
print(f"Top {k3} frequent elements: {topKFrequent(nums3, k3)}")
