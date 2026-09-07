def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

try:
    n_terms = int(input("Enter the index of the Fibonacci number: "))
    if n_terms < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"The number is: {fib(n_terms)}")
except ValueError:
    print("Invalid input. Please enter a number.")
