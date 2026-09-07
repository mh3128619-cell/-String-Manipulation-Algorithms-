def f(x):
    return -1 * (x**2) + 40 * x

def find_max_ternary(low, high):
    for _ in range(100):
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        
        if f(mid1) < f(mid2):
            low = mid1
        else:
            high = mid2
            
    return (low + high) / 2

max_x = find_max_ternary(0, 100)
print(f"The value of x that gives the maximum is approximately: {max_x:.4f}")
print(f"The maximum value of the function is: {f(max_x):.4f}")
