def reverse_log_entries(log_list):
     Helper function to reverse elements within a specific range (In-place)
    def reverse_range(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    n = len(log_list)
    
     1. Reverse the entire array (reverses both word order and characters)
    reverse_range(log_list, 0, n - 1)
    
     2. Reverse each word individually to correct the character order
    start = 0
    for end in range(n + 1):
        # When we find a space or reach the end of the array
        if end == n or log_list[end] == ' ':
            # Reverse the range of the found word
            reverse_range(log_list, start, end - 1)
            # Update the start point for the next word
            start = end + 1

 Testing the code with log data example
log_data = ['2', '0', '2', '6', ' ', 'E', 'D', 'O', 'C', ' ', 'D', 'E', 'T', 'A', 'D', 'P', 'U']

print("Before processing:", log_data)
reverse_log_entries(log_data)
print("After processing: ", log_data)
# Expected output: ['U', 'P', 'D', 'A', 'T', 'E', 'D', ' ', 'C', 'O', 'D', 'E', ' ', '2', '0', '2', '6']
