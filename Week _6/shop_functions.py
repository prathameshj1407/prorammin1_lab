def get_items():
    items={}
    name=""
    print("----------------------------------------------------")
    while name!="done":

        name=input("Enter your item name: ")
        if name != "done":
            price = float(input("Enter your item price: "))
            items[name]=price
    print("-----------------------------------------------------")

    return items

def print_items(items):
    print("--------------------------------------------")
    print("Items: ")

    total=0
    for name,price in items.items():
        print(name,price)
        total = total + price
    print("Total= ", total)
    print("---------------------------------------------")
