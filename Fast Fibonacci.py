memo = {}

def fib_fast(n):
    if n in memo: 
        return memo[n]
    if n <= 1: 
        return n
    
    memo[n] = fib_fast(n - 1) + fib_fast(n - 2)
    return memo[n]

index = 50
print(f"Fibonacci at index {index} is: {fib_fast(index)}")
