def power(num, p):
    if p == 0:
        return 1
    return num * power(num, p - 1)

user_num = int(input("Enter the number: "))
user_power = int(input("Enter the power: "))

result = power(user_num, user_power)
print(f"The result is: {result}")
