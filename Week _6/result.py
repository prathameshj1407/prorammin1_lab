def check_result(mark):
    if mark >= 60:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

mark = [55,70,62,40,90]

for m in mark:
    check_result(m)