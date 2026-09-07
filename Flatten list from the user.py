import ast

def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print("Welcome! Please enter your nested list here.")
print("Example: [1, [2, [3, 4]], 5, [[6]]]")

user_input = input("\nEnter the list: ")

try:
    actual_list = ast.literal_eval(user_input)
    if isinstance(actual_list, list):
        final_result = flatten(actual_list)
        print(f"\nFlattened list: {final_result}")
    else:
        print("The input provided is not a list, please try again.")
except Exception as e:
    print(f"Formatting error: {e}")
    print("Ensure brackets [] and commas , are used correctly.")
