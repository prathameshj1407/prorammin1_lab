name = ["Jack","Raihan","Ben","Simon"]
marks = [65,82,55,90]

student = {}

for i in range (len(name)):
    student[name[i]] = marks[i]

for name, marks in student.items():
    if marks >= 60:
        grade = "Pass"
    else:
        grade = "Fail"

    print(name, marks, grade)