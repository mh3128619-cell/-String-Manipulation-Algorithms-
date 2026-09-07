def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data = [10, 50, 30, 70, 80, 20]
target1 = 30
result1 = linear_search(data, target1)

print(f"Searching for {target1}:")
if result1 != -1:
    print(f"Found at Index: {result1}")
else:
    print("Element not found.")

print("-" * 20)

target2 = 99
result2 = linear_search(data, target2)

print(f"Searching for {target2}:")
if result2 != -1:
    print(f"Found at Index: {result2}")
else:
    print("Element not found (returned -1).")
