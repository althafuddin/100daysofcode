def student_grade(x):
    length = len(x)
    total = sum(x)
    avg = total/length
    return avg, total, length


students = [{"name": "Jose", "marks": [56, 77, 97]},
            {"name": "Rolf", "marks": [45, 80]},
            {"name": "Anna", "marks": [87, 75, 100, 95, 98]},
            {"name": "Mary", "marks": [67, 70, 80]},
            {"name": "Stuart", "marks": [44, 55]},
            {"name": "Sophie", "marks": [86, 90, 100, 100]}, ]

for student in students:
    average, marks, count = student_grade(student['marks'])
    print('For Student:' + student['name'] + ' Gained Sum of ' + str(marks) + ' with an average of ' + str(average) +
          ' in subjects of ' + str(count))
