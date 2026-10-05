class student:
    def __init__(self, name, course, mark):
        self.name = name
        self.course = course
        self.marks = mark

    def display_info(self):
        print("name:", self.name)
        print("course:", self.course)
        print("marks:", self.marks)

## Part 2 Activity 1
## 1)class is a user define datatype and it is a collection of data. here the class is "student"
## 2)"__init__" stands for intializing the variable where we store data


## Part 2 Activity 2
student1 = student("Abdullah muhammad", "python", 95)
student2 = student("Nikshey Chandell", "python", 79)
student3 = student("Sandip Bhatta", "python", 69)
student4 = student("Prathamesh Jaiswal", "python", 80)

print("----------------------------------------")
print("output of Part 2 Activity 2")

student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()

## Part 2 Activity 3
print("-----------------------------")
print("output of Part 2 Activity 3")
student1.marks = 80
student1.display_info()

## 1)python got to know about the changes because we selected the particular object/instance to make changes
## 2)the reason only student1 change because we selected the particular object/instance to make a changes only in that data
## 3)yes, the other student data going to be same as we gave the data
