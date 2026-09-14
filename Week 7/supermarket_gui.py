import tkinter as tk

window = tk.Tk()
window.title('Supermarket GUI')
window.geometry('500x500')

tk.Label(window, text="Item name: ").pack()
item_name = tk.Entry(window)
item_name.pack()

tk.Label(window, text="Price: ").pack()
item_price = tk.Entry(window)
item_price.pack()


item_pr = {}
def add():
    name = item_name.get()
    price = item_price.get()
    item_pr[name] = price
    result.config(text="Item added successfully")

def calculate_total():
    total = 0
    for i in item_pr.values():
        total = total + int(i)
    result.config(text="Total: " + str(total))

def display_item():
    cont_text = ""
    for i,j in item_pr.items():
        cont_text = cont_text + str(i) + ": " + str(j) + "\n"
    result.config(text=cont_text)

tk.Button(window, text="Add", command=add).pack()
tk.Button(window, text="Calculate", command=calculate_total).pack()
tk.Button(window, text="Display", command=display_item).pack()

result = tk.Label(window, text="output here: ")
result.pack()

window.mainloop()