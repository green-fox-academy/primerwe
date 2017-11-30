accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

#search_account = str(input("Your Account number please!: "))
#
#def list_by_account(accounts):
#    for i in range(len(accounts)):
#        if search_account in str(accounts[i]['account_number']):
#            return accounts[i]['client_name'], accounts[i]['balance']
#        else:
#            return "404 - account not found"
#
#print(list_by_account(accounts))

#to_account = int(input("Where do you want to transfer money to? Enter account please!: "))
#from_account = int(input("Where do you want to transfer money from? Enter account please!: "))
#amount = int(input("How much money you would like to transfer? Enter amount please!: "))

def transfer(to_account, from_account, amount):
    test = False
    for i in range(len(accounts)):
        if from_account == accounts[i]['account_number']:
            a = i
            test = True
        if to_account == accounts[i]['account_number']:
            b = i
            test = True
            
    if test is True:
        if accounts[a]['balance'] - amount < 0:
            return "Not enough money"
        else:
            accounts[a]['balance'] -= amount
            accounts[b]['balance'] += amount
            return "Transaction complete!"
    else:
        return "404 - account not found"
    
print(transfer(11234543, 43546712, 5204100072))