score = int(input("enter your score: "))
while score != 7:

    if score < 7:
        print("too low ")
        score = int(input("enter your score: "))

    elif score > 7:
        print("too high ")
        score = int(input("enter your score: "))

print("-----------------")
print("Correct !!!...")
print("-----------------")