def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(f"Original intervals: {intervals1}")
print(f"Merged intervals: {merge_intervals(intervals1)}")

intervals2 = [[1,4],[4,5]]
print(f"\nOriginal intervals: {intervals2}")
print(f"Merged intervals: {merge_intervals(intervals2)}")

intervals3 = [[1,4],[0,4]]
print(f"\nOriginal intervals: {intervals3}")
print(f"Merged intervals: {merge_intervals(intervals3)}")

intervals4 = [[1,4],[0,0]]
print(f"\nOriginal intervals: {intervals4}")
print(f"Merged intervals: {merge_intervals(intervals4)}")
