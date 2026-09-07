def insertion_sort_students(grades):
    for i in range(1, len(grades)):
        key = grades[i]
        j = i - 1
        while j >= 0 and grades[j] > key:
            print(f"Shifting element {grades[j]} to the right...")
            grades[j + 1] = grades[j]
            j -= 1
        grades[j + 1] = key
        print(f"Current array: {grades}")
        print("-" * 30)
    return grades

student_grades = [70, 80, 90, 0]
final_result = insertion_sort_students(student_grades)
print(f"Final sorted result: {final_result}")
