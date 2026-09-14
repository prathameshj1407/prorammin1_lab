def calculate_result(*args):
    sum = 0
    for i in args:
        sum = sum + i

    avg = sum / len(args)
    print("Average : ",avg)

    if avg >= 50:
        print("PASS")
    else:
        print("FAIL")
calculate_result(40,40,40)