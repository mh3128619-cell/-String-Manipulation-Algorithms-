def bucket_sort_stable(arr):
    buckets = [[] for _ in range(10)]

    for name, grade in arr:
        index = int(grade / 10)
        if index == 10:
            index = 9
        buckets[index].append((name, grade))

    result = []
    for b in buckets:
        b.sort(key=lambda x: x[1])
        result.extend(b)
    return result

students = [("Ahmed", 90), ("Mohammed", 50), ("Sarah", 90)]
print(f"Original students: {students}")
stable_sorted_students = bucket_sort_stable(students)
print(f"Stable sorted students: {stable_sorted_students}")

students_2 = [("Alice", 75), ("Bob", 88), ("Charlie", 75), ("David", 92)]
print(f"\nOriginal students 2: {students_2}")
stable_sorted_students_2 = bucket_sort_stable(students_2)
print(f"Stable sorted students 2: {stable_sorted_students_2}")
