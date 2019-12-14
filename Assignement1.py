from collections import defaultdict

students_marks = []
with open('student_marks.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = int(columns[-1].rstrip('\n'))
        students_marks.append(tuple(columns))


subject_faculty = []
with open('subject_faculty.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = columns[-1].rstrip('\n')
        subject_faculty.append(tuple(columns))


# Student with least number of marks as total
d = {}
for stud, sub, marks in students_marks:
    if stud not in d:
        d[stud] = [marks]
    else:
        d[stud].append(marks)
stud, marks = min(d.items(), key=lambda x: sum(x[1]))
print("Student with least marks as total in all subjects is:", stud, sum(marks))

# Student who is top with maximum number of total marks
d1 = {}
for stud, sub, marks in students_marks:
    if stud not in d1:
        d1[stud] = [marks]
    else:
        d1[stud].append(marks)


stud, marks = max(d1.items(), key=lambda x: sum(x[1]))
print("Student with highest marks as total in all subjects is:", stud, sum(marks))

# Best student in mathematics
d2 = {}
for stud, sub, marks in students_marks:
    if stud not in d2 and sub == "Mathematics":
        d2[stud] = marks

stud, marks = max(d2.items(), key=lambda x: x[1])
print("Student who got maximum marks in mathematics is:", stud, "got", marks, "marks")

# finding the average mark of each subject ignoring failure

d4 = defaultdict(list)
for stud, sub, marks in students_marks:
    if marks not in d4 and marks > 40:
        d4[sub].append(marks)

d5 = {}
for sub, marks in d4.items():
    d5[sub] = sum(marks)/len(marks)
print("Average marks of each subject is", d5)

# Faculty with highest pass percentage(more than 40%)

d6 = defaultdict(list)
for stud, sub, marks in students_marks:
    if marks not in d6 and marks <= 40:
        d6[sub].append(marks)

sub, marks = max(d6.items(), key=lambda x: len(x[1]))

for subject_of_faculty, name in subject_faculty:
    if subject_of_faculty == sub:
        print("Faculty with most number of students with less that or equal to 40% is:", name, sub, len(marks))

# Faculty with highest pass percentage (i.e > 40)

d6 = defaultdict(list)
for stud, sub, marks in students_marks:
    if marks not in d6 and marks > 40:
        d6[sub].append(marks)

sub, marks = max(d6.items(), key=lambda x: len(x[1]))

for subject_of_faculty, name in subject_faculty:
    if subject_of_faculty == sub:
        print("Faculty with most number of students with greater than 40% is:", name, sub, len(marks))

# Faculty with highest student count who got more than 90%

d7 = defaultdict(list)
for stud, sub, marks in students_marks:
    if marks not in d7 and marks > 90:
        d7[sub].append(marks)

sub, marks = max(d7.items(), key=lambda x: len(x[1]))

for subject_of_faculty, name in subject_faculty:
    if subject_of_faculty == sub:
        print("Faculty with most students got above 90% is:", sub, name, len(marks))
