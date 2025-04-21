#!/usr/bin/python3
for i in range(5000):
   print("INSERT INTO Students ( student_id, name ) VALUES ( " + str(i + 1) + ", 'Student" + str(i + 1) + "' );")
