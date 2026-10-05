class BankingOperation:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def display_info(self):
        print(self.name)
        print(self.course)
        print(self.marks)

student1 = BankingOperation(1, "", 500)
student2 = BankingOperation(2, "", 500)
student3 = BankingOperation(3, "", 500)
student4 = BankingOperation(4, "", 500)

# 1)then we need to create 100 instance/object
# 2)then the code we need to create variable for each 100 student for that it will
# alot line of code
# 3)if we use the class and object it will be easy to use easy to add or remove instance/object,
# but if we use 100 variable for each 100 students then its difficult to manage the code