class BankingOperation:
    def __init__(self, identity, name, balance):
        self.id = identity
        self.name = name
        self.balance = balance

    def open_account(self):
        print("Account has opened successfully", self.name)

    def deposit(self, amount):
        self.balance += amount
        print("deposited successfully")
        print("New balance is", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= amount
            print("withdrawn successfully", self.balance)
            print("New balance is", self.balance)
        else:
            print("Withdraw failed")
            print("Sorry, insufficient balance")

    #def loan(self, amount):


    def transfer(self, amount):
        self.balance -= amount
        self.balance += amount
        print("Transfer successfully", self.balance)
        print("New balance is", self.balance)

customer1 = BankingOperation(23232323, "nick", 100)
customer2 = BankingOperation(98989898, "Abdullah", 100)

customer1.open_account()
customer1.deposit(100)
customer1.withdraw(100)
customer1.transfer(100)
