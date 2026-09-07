def sum_digits(n):
    if n < 10:
        return n
    
    last_digit = n % 10
    rest_of_number = n // 10
    
    return last_digit + sum_digits(rest_of_number)

number = 1234
print(f"Sum of digits for {number} is: {sum_digits(number)}")
