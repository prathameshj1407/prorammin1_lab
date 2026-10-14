class shopping_cart:
    def __init__(self, customer_name, product_name, price, quantity,):
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        self.total = self.price * self.quantity
        #return total

    def display_cart(self):
        print("--------------------Your Cart----------------------")
        print("Customer Name:", self.customer_name)
        print("Product Name:", self.product_name)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total price", self.calculate_total())

    def apply_discount(self):
        #if self.calculate_total() >= 500:
        if self.total >= 500:
            # 10% Discount
            discount = self.total * 0.10

            #subtracting the discount from total
            discount_price = self.total - discount

            #display the discount is apply or not
            print("YAY! You got Discount of 10%")
            print("Disount: ", "-",discount)
            print("Discounted price: ", discount_price)

        else:
            print("Sorry, No Discount for you")

customer1 = shopping_cart("Sandip", "book", 7, 3)
customer2 = shopping_cart("Nikshey", "airpods", 428, 2)
customer1.display_cart()
customer1.apply_discount()
print()
customer2.display_cart()
customer2.apply_discount()