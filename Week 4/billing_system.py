item = int(input("how many item you purchase: "))
i=0
grand_total = 0
for i in range(item):
    name = input("enter your item name: ")
    price = float(input("enter your item price: "))
    quantity = int(input("enter your item quantity: "))

    print("---------billing system----------")
    print("item name: ", name)
    print("item price: ", price)
    print("item quantity: ", quantity)
    item_total = price * quantity
    print("total for", name, "is: ", item_total)

    grand_total = grand_total + item_total
    print("----------------------------------")

print("----------------------------------")
print("grand total is: ", grand_total)
print("----------------------------------")
