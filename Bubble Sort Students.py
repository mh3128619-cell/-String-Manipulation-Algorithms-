def bubble_sort_students(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][1] > students[j + 1][1]:
                students[j], students[j + 1] = students[j + 1], students[j]
    return students

students_list = [("Mohamed", 90), ("Ahmed", 70), ("Sara", 85)]
print(bubble_sort_students(students_list))
