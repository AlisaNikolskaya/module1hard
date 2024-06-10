grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))

dict_ = {}

for i in range(len(students)):
    student_name = students[i]
    grade_list = grades[i]
    dict_[student_name] = sum(grade_list) / len(grade_list)

print(dict_)