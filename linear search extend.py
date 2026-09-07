def linear_search_extended(arr, target, find_all=False):
    if find_all:
        indices = []
        for i in range(len(arr)):
            if arr[i] == target:
                indices.append(i)
        
        return {
            "indices": indices,
            "count": len(indices)
        }
    
    else:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

my_list = [10, 30, 50, 30, 80, 30]
target = 30

first_index = linear_search_extended(my_list, target, find_all=False)
print(f"First occurrence of {target} is at index: {first_index}")

all_results = linear_search_extended(my_list, target, find_all=True)
print(f"The number {target} appeared {all_results['count']} times at indices: {all_results['indices']}")
