account_balance = 1000
print("----------ATM----------")
print("insert ATM card")
pin = float(input("Please enter your PIN: "))

int = 1234
if pin != int:
    print("Invalid PIN")
    exit()

else:
    amount = float(input("Please enter your Withdrawal Amount: "))


if account_balance < amount:
    print("Sorry - Insufficient funds")

else:
    print("Dispensing cash")
    print("Printing receipt")
    print("Please take your cash")
    new_balance = account_balance - amount
    print("Your remaining balance is: ", new_balance, "$")

print("-----------------------")
