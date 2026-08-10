"""while True:
    score = int(input("enter your score: "))
    if score >=0 and score <= 100:
        break
    else:
        print("invalid score, Please enter again ")"""
score = int(input("enter your score: "))
while score < 0 or score > 100:
    print("Invalid score, Please enter again ")
    score = int(input("enter your score: "))

print("------------------------------")
if score >= 80:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Fail")
print("------------------------------")