#!/usr/bin/python3
def get_file_data(file_name):
   f = open(file_name)
   data = []
   for line in f:
       data.append(line.rstrip())
   return data


courses = get_file_data("courses.txt")


course_id = 1
course_type_id = -1


for c in courses:
    if str(c[0:2]).upper() == "AP":
        course_type_id = 1
    elif str(c[0:7].upper()) == "REGENTS":
        course_type_id = 3
    else:
        course_type_id = 2
    print("INSERT INTO Courses ( course_id, course_type_id, course_name ) VALUES ( " + str(course_id) + ", " + str(course_type_id) + ", '" + str(c) + "' );")
    course_id += 1
