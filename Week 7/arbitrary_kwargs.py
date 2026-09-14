def fruit_price(**kwargs):
    sum = 0
    for i in kwargs.keys():
        print(i)
fruit_price(apple=10,mango=40,orange=20,peach=30)
