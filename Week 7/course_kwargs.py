def calculate_score(**kwargs):
    sum = 0
    for j,i in kwargs.items():
        sum = sum + i

    avg = sum/len(kwargs)
    print("Average: ",avg)

calculate_score(IT5014=60,IT7809=80,IT6798=50,IT5048=70)
