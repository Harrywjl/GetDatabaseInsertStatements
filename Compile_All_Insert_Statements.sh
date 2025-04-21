#!/bin/bash

PDB=Populate_Database
cat Get_Tables.txt | grep 'DROP' > ${PDB}.DROP
cat Get_Tables.txt | grep 'CREATE' > ${PDB}.CREATE
./Get_Students.py > $PDB
cat Get_Departments.txt >> $PDB
./Get_Teachers.py >> $PDB
./Get_Rooms.py >> $PDB
cat Get_AssignmentTypes.txt >> $PDB
cat Get_CourseTypes.txt >> $PDB
./Get_Courses.py >> $PDB
./Sections_Schedules_Assignments_Gradebook.py >> $PDB
