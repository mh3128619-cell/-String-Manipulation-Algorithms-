DISK_PAGE_SIZE = 1024
total_file_size = 5000

def read_page_from_disk(index):
    return index

def load_page_to_ram(start, end):
    return list(range(start, end))

def linear_search_in_ram(data, target):
    try:
        return data.index(target)
    except ValueError:
        return "Not Found"

def disk_aware_jump_search(file_handler, target):
    step = DISK_PAGE_SIZE
    prev = 0
    
    while read_page_from_disk(step - 1) < target:
        prev = step
        step += DISK_PAGE_SIZE
        if prev >= total_file_size:
            return "Not Found"
            
    data_in_ram = load_page_to_ram(prev, step)
    return linear_search_in_ram(data_in_ram, target)

result = disk_aware_jump_search(None, 2048)
print(f"Search result: {result}")
