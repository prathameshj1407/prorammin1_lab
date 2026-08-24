def print_results(students):
    for name, mark in students.items():
        if mark>=60:
            result = "Pass"
        else:
            result="Fail"

        print(name,mark,result)

students={"john":65,"mary":82,"ali":55,"sina":90}
print_results(students)