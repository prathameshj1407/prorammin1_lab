scores = [65,72,80,55,90,68,77]
count = 0

for score in scores:
    if score > 70:
        count = count + 1
print("-----------------------------------------")
print("Student scoring above 70: ", count)
print("-----------------------------------------")

for score in scores:
    if score < 60:
        print(score, " FAIL")

    else:
        print(score, " PASS")
print("------------------------------------------")