#!/usr/bin/python3
import random

class Teacher:
    def __init__(self, id, period):
        self.id = id #1-304
        self.period = period #1-10


class Room:
    def __init__(self, id, period):
        self.id = id #1-720
        self.period = period#1-10


class Section:
    def __init__(self, id, period):
        self.id = id #1-(98-490)
        self.period = period #1-10


class Schedule:
    def __init__(self, student_id, section_id):
        self.student_id = student_id #1-5000
        self.section_id = section_id #1-(98-490)


class Assignment:
    def __init__(self, id, section_id):
        self.id = id #Sections * 15
        self.section_id = section_id #1-(98-490)


teachers = []
for t in range(1, 305):
    for p in range(1, 11):
        teachers.append(Teacher(t, p))

rooms = []
for r in range(1, 721):
    for p in range(1, 11):
        rooms.append(Room(r, p))

section_id = 1 #Total Sections: 98-490
courses = []
course_id = 1 #1-98
while course_id <= 98:
    times_offered = random.randint(1, 5)
    for t in range(times_offered):
        random_teacher = random.choice(teachers)
        teacher_id = random_teacher.id
        period = random_teacher.period
        random_room = Room("placeholder", -1)
        while random_room.period != period:
            random_room = random.choice(rooms)
        room_id = random_room.id
        #Sections
        print("INSERT INTO Sections ( section_id, course_id, teacher_id, room_id, period ) VALUES ( " + str(section_id) + ", " + str(course_id) + ", " + str(teacher_id) + ", " + str(room_id) + ", " + str(period) + " );")
        teachers.remove(random_teacher)
        rooms.remove(random_room)
        section_id += 1
    course_id += 1
total_sections = section_id - 1

sections = []
for r in range(1, total_sections + 1):
    for p in range(1, 11):
        sections.append(Section(r, p))

schedules = []
for student_id in range(1, 5001):
    for p in range(1, 11):
        random_section = random.choice(sections)
        while random_section.period != p:
            random_section = random.choice(sections)
        section_id = random_section.id
        #Schedules
        print("INSERT INTO Schedules ( student_id, section_id ) VALUES ( " + str(student_id) + ", " + str(section_id) + " );")
        schedules.append(Schedule(student_id, section_id))

assignments = []
assignment_id = 1
for s in range(1, total_sections + 1):
    for minor in range(12):
        #Assignments(Minor)
        print("INSERT INTO Assignments ( assignment_id, section_id, assignment_type_id, assignment_name ) VALUES ( " + str(assignment_id) + ", " + str(s) + ", " + str(1) + ", 'Assignment" + str(assignment_id) + "' );")
        assignments.append(Assignment(assignment_id, s))
        assignment_id += 1
    for major in range(3):
        #Assignments(Major)
        print("INSERT INTO Assignments ( assignment_id, section_id, assignment_type_id, assignment_name ) VALUES ( " + str(assignment_id) + ", " + str(s) + ", " + str(2) + ", 'Assignment" + str(assignment_id) + "' );")
        assignments.append(Assignment(assignment_id, s))
        assignment_id += 1

for a in range(len(assignments)):
    for schedule in schedules:
        if schedule.section_id == assignments[a].section_id:
            random_grade = random.randint(75, 100)
            #Gradebook
            print("INSERT INTO Gradebook ( assignment_id, student_id, grade ) VALUES ( " + str(a + 1) + ", " + str(schedule.student_id) + ", " + str(random_grade) + " );")
