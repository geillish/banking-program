#################################################################
def run_program():
	user_name = input("Hello Human/Robot/Other. Please enter your name: \n\t")
	print()	
	
	user_balance = -1
	while user_balance < 0:
		user_balance = float(input(f"Now - tell me {user_name}, how much money do you have? \n\t€"))
		if user_balance < 0:
			print()
			print("Uh-oh! You can't start with a minus balance - try again.")
			print()
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	
	end_flag = False
	transaction_list = [f"\t\tStarting Balance: {user_balance:.2f}"]
	while end_flag == False:
		print()
		print()
		print()
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print()
		print(f"""{user_name}, your current balance is: €{user_balance:.2f}\n
Here is a list of things I can do for you:
		\n\t1.\t Withdraw
		\n\t2.\t Deposit
		\n\t3.\t Interest
		\n\t4.\t Transactions
		\n\t5.\t Quit""")
		print()
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

		print()
		user_command = input("Let me know what you would like to do: \n\t").lower()
		print()

		if user_command == "withdraw" or user_command == "1":
			user_balance, transaction_list = withdraw_money(user_name,user_balance,transaction_list)

		if user_command == "deposit" or user_command == "2":
			user_balance, transaction_list = deposit_money(user_name,user_balance,transaction_list)

		if user_command == "Interest" or user_command == "3":
			interest_rate = 1.5
			user_interest(user_name,user_balance, interest_rate)
			print()

		if user_command == "transactions" or user_command == "4":
			user_transactions(user_name,user_balance,transaction_list)
			print()

		if user_command == "quit" or user_command == "5":
			end_flag = True
	
	print()
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print(f"Thank you for using our services, Human/Robot/Other named {user_name}. Have a good day.")

#################################################################
def withdraw_money(name,balance,transactions):
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print(f"\tSo {name} you want to take your money, huh?")
	print()
	withdraw_end_flag = False
	while withdraw_end_flag == False:
		withdraw_ammount = float(input("\tHow much would you like to take out?\n\t\t€"))
		new_balance = balance - withdraw_ammount
		if new_balance >= 0:
			balance = new_balance
			transactions.append(f"\t\tWithdrawl: €{withdraw_ammount}\n\t\tRemaining Balance: €{balance:.2f}")
			withdraw_end_flag = True
			return balance, transactions
		else:
			print()
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print()
			print("\tUh-oh! You can't go into a minus balance - try again.")
			print()
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#################################################################
def deposit_money(name,balance,transactions):
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print(f"\tSo {name} you want to give us your money, huh?")
	print()
	deposit_ammount = float(input("\tHow much would you like to add?\n\t\t€"))
	balance = balance + deposit_ammount
	transactions.append(f"\t\tDeposit: €{deposit_ammount}\n\t\tRemaining Balance: €{balance:.2f}")
	return balance, transactions

#################################################################
def user_interest(name,balance,rate):
	interest = (balance/100)*rate
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print(f"""\tSo {name} you want to know how much you can make off of us, huh?\n\n
	Well you would be pleased to know your current interest rate is: {rate}
	Meaning with your current balance of €{balance:.2f} - you can have an extra €{interest:.2f} 
	in your account this time next year without even lifting a finger!""")

#################################################################
def user_transactions(name,balance,transactionList):
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print(f"\tSo {name} you want a list of transactions, huh?\n\tWell, here you go:\n")
	for item in transactionList:
		print(item)
	print()
	print(f"\t\tCurrent Balance: €{balance}")

#################################################################
run_program()
