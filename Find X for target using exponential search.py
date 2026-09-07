def f(x):
    return x**2

def find_x_for_target(target):
    if f(0) == target:
        return 0
    
    x = 1
    while f(x) < target:
        x *= 2
        
    low = x // 2
    high = x
    
    while low <= high:
        mid = (low + high) // 2
        val = f(mid)
        
        if val == target:
            return mid
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

target_val = 144
result = find_x_for_target(target_val)

if result != -1:
    print(f"The value that satisfies the equation is x = {result}")

else:
    print("No integer solution found for this equation")
