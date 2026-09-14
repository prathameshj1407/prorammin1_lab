import tkinter as tk

#GUI window size
window = tk.Tk()
window.title("Requisition System: Prathamesh(20261341)")
window.geometry("500x650")


# Requisition counter
requisition_counter = 10000

# Date
tk.Label(window, text="Date:").pack()
date = tk.Entry(window)
date.pack()


# Staff Name
tk.Label(window, text="Staff Name:").pack()
staff_name = tk.Entry(window)
staff_name.pack()


# Staff ID
tk.Label(window, text="Staff ID:").pack()
staff_id = tk.Entry(window)
staff_id.pack()


# Item Name
tk.Label(window, text="Item Name:").pack()
item_name = tk.Entry(window)
item_name.pack()


# Item Price
tk.Label(window, text="Item Price:").pack()
item_price = tk.Entry(window)
item_price.pack()


# Store items
items = []

# Store total
total = 0

# Store requisition ID
requisition_id = 0

# Add Item function
def add_item():

    name = item_name.get()
    price = float(item_price.get())

    items.append({
        "name": name,
        "price": price
    })

    item_name.delete(0, tk.END)
    item_price.delete(0, tk.END)

    result.config(text="Item added successfully")


# Calculate Total function
def calculate_total():

    #in the below line you can see the term global which help to use the variable which is outside the function. for this i got lots of error to resolve that i took the help from google and learn about  global
    global total
    global requisition_counter
    global requisition_id


    # Create new requisition ID
    requisition_counter = requisition_counter + 1
    requisition_id = requisition_counter

    # Calculate total
    total = 0

    for item in items:
        total = total + item["price"]

    result.config(
        text="Requisition ID: " + str(requisition_id) +
             "\nTotal: $" + str(total)
    )


# Check Approval function with display part
def check_approval():

    if total < 500:
        status = "Approved"
        approval_reference = staff_id.get() + str(requisition_id)[-3:]
    else:
        status = "Pending"
        approval_reference = ""

    output = "Requisition ID: " + str(requisition_id) + "\n"
    output = output + "Date: " + date.get() + "\n"
    output = output + "Staff Name: " + staff_name.get() + "\n"
    output = output + "Staff ID: " + staff_id.get() + "\n"
    output = output + "Total: $" + str(total) + "\n"
    output = output + "Status: " + status + "\n"

    if approval_reference:
        output = output + "Approval Reference Number: " + approval_reference

    result.config(text=output)


# Add Item button
tk.Button(
    window,
    text="Add Item",
    command=add_item
).pack(pady=10)


# Calculate Total button
tk.Button(
    window,
    text="Calculate Total",
    command=calculate_total
).pack(pady=10)


# Check Approval button
tk.Button(
    window,
    text="Check Approval",
    command=check_approval
).pack(pady=10)

#output
result = tk.Label(
    window,
    text="Print of requisition below",
    justify="left"
)

result.pack(pady=20)


window.mainloop()