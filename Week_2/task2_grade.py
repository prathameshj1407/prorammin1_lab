#input of all the marks which student get in his assignments
ass = float(input("Please Enter your assignment marks: "))
test = float(input("Please Enter your test marks: "))
exam = float(input("Please Enter your exam marks: "))

print("----------STUDENT RESULT----------")

#printing all the result
print("Assignment mark is : ",ass)
print("Test Mark is : ",test)
print("Exam mark is : ",exam)

#calculating the assignment contribution
ass1 = ass / 100 * 30
test1 = test / 100 * 30
exam1 = exam / 100 * 40

#printing the calculated contribution
print("Assignment Contribution (30%) : ", ass1)
print("Test Contribution (30%) : ", test1)
print("Exam Contribution (40%) : ", exam1)

#calculating the final grade
final = ass1 + test1 + exam1

#printing the calculated grade
print("Final Grade: ", final,"%")
print("-------------------------------------")

#program end