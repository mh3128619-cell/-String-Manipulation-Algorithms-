def sort_students(students):
    if not students: return students

    max_grade = max(s[0] for s in students)
    count = [0] * (max_grade + 1)
    output = [None] * len(students)

    for grade, name in students:
        count[grade] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(students) - 1, -1, -1):
        grade, name = students[i]
        position = count[grade] - 1
        output[position] = (grade, name)
        count[grade] -= 1

    return output

data = [(5, "Ali"), (2, "Mona"), (5, "Seif")]
result = sort_students(data)
print("Stable order of students:")
for s in result:
    print(f"Name: {s[1]}, Grade: {s[0]}")
