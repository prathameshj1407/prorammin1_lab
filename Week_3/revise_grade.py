m1 = float(input("Please Enter your course 1 marks: "))
m2 = float(input("Please Enter your course 2 marks: "))
m3 = float(input("Please Enter your course 3 marks: "))
m4 = float(input("Please Enter your course 4 marks: "))

print("----------STUDENT RESULT----------")

#printing all the result
total = m1 + m2 + m3 + m4
grade = total / 4

print("Final Grade: ", grade, "%")

if grade >= 85:
    print("GRADE: A")
    print("Remark: Excellent")

elif grade >= 75:
    print("GRADE: B")
    print("Remark: Very Good")

elif grade >= 65:
    print("GRADE: C")
    print("Remark: Good")

elif grade >= 50:
    print("GRADE: D")
    print("Remark: Pass")

else:
    print("GRADE: F")
    print("Remark: Fail")

print("-------------------------------------")