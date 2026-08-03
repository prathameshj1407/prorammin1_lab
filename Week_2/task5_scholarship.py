#taking an input that is student info
name = input("Please Enter your full Name :")
age = int(input("Please Enter your Age :"))
GPA = float(input("Please Enter your GPA :"))
stud = input ("Are you a Domestic Student ? (YES/NO) :")
income = float(input("Please Enter your income :"))

#printing the student info
print("-------Scholarship Result-------")
print("Student: ",name)
print("Age:",age)
print("GPA:",GPA)

#checking is student eligible or not and printing the result accordingly
if GPA >= 8.5 and income < 40000:
    print("Congratulations! You Qualify for FULL SCHOLARSHIP.")
else:
    print("Unfortunately you are not eligible for our scholarship.")

print("----------------------------------")