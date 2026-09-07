def f(t):
    return (t**2) - (100*t) + 5000

def g(t):
    return -1 * f(t)

def find_min_ternary(low, high):
    for _ in range(100):
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        
        if g(mid1) < g(mid2):
            low = mid1
        else:
            high = mid2
            
    return (low + high) / 2

min_t = find_min_ternary(0, 100)
print(f"The day with the minimum cost is approximately: {min_t:.2f}")
print(f"The minimum cost is: {f(min_t):.2f}")
