#taking the input from the user about his item, price and quantity
item = input("Please Enter your Item: ")
price = int(input("Please Enter your Price: "))
qn = int(input("Please Enter your Item Quantity Purchased: "))

#calculating the total cost, gst and the total price of the item
tcost = price * qn
gst = tcost / 100 * 15
total = tcost + gst

#printin the calculated all the subtotal cost gst and total user need to pay
print("-------Receipt-------")
print("Item: ",item)
print("Price per Item: ",price)
print("Quantity: ",qn)
print("SubTotal : ",tcost)
print("GST (15%) : ",gst)
print("TOTAL : $",total)
print("----------------------")