import math

def jump_search_dynamic(arr, target):
    n = len(arr)
    
    if n > 10000:
        step = int(math.sqrt(n)) * 2
    else:
        step = int(math.sqrt(n))
        
    prev = 0
    
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
            
    while prev < n and arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
            
    if prev < n and arr[prev] == target:
        return prev
    
    return -1

arr = [i for i in range(0, 20000, 2)]
target = 15000
result = jump_search_dynamic(arr, target)

print(f"Element found at location: {result}")
