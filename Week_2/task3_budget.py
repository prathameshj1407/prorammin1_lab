#taking an input of all the expence and income
income = int(input("Please enter your Monthly Income: "))

rent = int(input("Please enter your Total Rent: "))
tcost = int(input("Please enter your Transport Cost: "))
fcost = int(input("Please enter your Food Cost: "))
ecost = int(input("Please enter your Entertainment Cost: "))

#calculating the total and balance left to the user
texpence = rent + tcost + fcost + ecost
bal = income - texpence

#printing all the result of the calculated part
print("-------Monthly Budget Calculator-------")
print("Total Expenditure : $",texpence)
print("Remaining Balance : $",bal)
print("----------------------------------------")