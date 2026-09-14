
def add_requisition():
    #requisition counter set to 10000
    requisition_counter = 10000

    #displaying to enter the information
    print("Enter your information:")

    #at the start ask the user to enter the date,id and name
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    #requisition_counter should start adding 1
    requisition_counter = requisition_counter + 1
    requisition_id = requisition_counter

    print("Requisition ID:", requisition_id)

    #item is a dictionary to store item name and te price of it
    items = []
    total = 0

    print("\nAdd items:")

    ans = "yes"

    while ans == "yes":
        item_name = input("Item Name: ")
        item_price = float(input("Item Price ($): "))

        #we use .append to add the items in te dictionary
        items.append({"name": item_name, "price": item_price})

        total = total + item_price

        ans = input("Add another item (yes/no): ")

    #print total
    print("Total: ", total)

    return date, staff_id, staff_name, requisition_id, items, total
add_requisition()