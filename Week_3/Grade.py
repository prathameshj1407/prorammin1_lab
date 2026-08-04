#input of all the marks which student get in his assignments
m1 = float(input("Please Enter your first marks: "))
m2 = float(input("Please Enter your second marks: "))
m3 = float(input("Please Enter your third marks: "))
m4 = float(input("Please Enter your fourth marks: "))

print("----------STUDENT RESULT----------")

#printing all the result
total = m1 + m2 + m3 + m4
grade = total / 4

print("Grade: ", grade, "%")

if grade < 50:
    print("Fail - Try again next time ")
else:
    print("Pass - Congratulations")

print("-------------------------------------")

#program end