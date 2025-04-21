#!/usr/bin/python3
def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

teachers = get_file_data("teachers.txt")
teacher_id = 0
department_id = 1
for t in teachers:
    if t == "*":
        department_id += 1
    else:
        teacher_id += 1
        print("INSERT INTO Teachers ( teacher_id, department_id, name ) VALUES ( " + str(teacher_id) + ", " + str(department_id) + ", '" + str(t) + "' );")
