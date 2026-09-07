def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
            
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
        
    return ptr1 


nums1 = [1, 3, 4, 2, 2]
print(f"Array: {nums1}, Duplicate: {findDuplicate(nums1)}") 

nums2 = [3, 1, 3, 4, 2]
print(f"Array: {nums2}, Duplicate: {findDuplicate(nums2)}") 

nums3 = [1, 1]
print(f"Array: {nums3}, Duplicate: {findDuplicate(nums3)}") 

nums4 = [1, 1, 2]
print(f"Array: {nums4}, Duplicate: {findDuplicate(nums4)}") 
