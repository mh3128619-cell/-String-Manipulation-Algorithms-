import math

def master_theorem(a, b, d):
    b_pow_d = math.pow(b, d)
    
    print(f"--- Analysis: T(n) = {a}T(n/{b}) + n^{d} ---")
    
    if a < b_pow_d:
        return f"Result: Case 1 -> O(n^{d})"
    
    elif a == b_pow_d:
        return f"Result: Case 2 -> O(n^{d} * log n)"
    
    else:
        log_a_base_b = math.log(a, b)
        return f"Result: Case 3 -> O(n^{log_a_base_b:.2f})"

print(master_theorem(a=2, b=2, d=1))
print(master_theorem(a=4, b=2, d=0))
