info = {}
while True:
    name = input("Enter your Item Name: ")
    if name == "done" or name == "end" or name == "quit" or name == "":
        break
    price = float(input("Enter your Price: "))
    info[name] = price
print("Items entered: ")
print(info)

sum = 0
for price in info:
    sum = sum + info[price]

print("Grand Total: ",sum)