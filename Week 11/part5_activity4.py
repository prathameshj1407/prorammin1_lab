class Assessment:
    def __init__(self, student_name, assessment_name, marks):
        self.student_name = student_name
        self.assessment_name = assessment_name
        self.marks = marks

    def display_results(self):
        print("Student: ",self.student_name)
        print("Assessment: ",self.assessment_name)
        print("Marks: ",self.marks)

    def check_pass(self):
        if self.marks >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

student1 = Assessment("Abdullah muhammad", "Python", 95)
student2 = Assessment("Nikshey Chandell", "Python", 79)

student1.display_results()
student1.check_pass()
student2.display_results()
student2.check_pass()

## code here
print("------------------------------------------")
print("output of Part 4 Activity 4")

class Lecturer:
    def __init__(self, lecturer_name, department, course, years_experience):
        self.name = lecturer_name
        self.department = department
        self.course = course
        self.years = years_experience

    def display_info(self):
        print("Lecturer Name: ",self.name)
        print("Department: ",self.department)
        print("Course: ",self.course)
        print("Years of Experience: ",self.years)

    def check_experience(self):
        if self.years >= 5:
            print("Experience Lecturer")
        else:
            print("Junior Lecturer")

lecturer1 = Lecturer("Sarah Ahmed", "Information Technology", "Python Programming", 5)
lecturer1.display_info()
lecturer1.check_experience()