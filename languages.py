class BankManager:
    def __init__(self,bank_account,balance=0):
        self.bank_account=bank_account
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        self.balance-=amount
        if amount>self.balance:
            print("Insufficient balance")
            return self.balance
    def balance(self):
        return self.balance

accounts={}
while True:
    print("Pick 1. to create a KZIP account ")
    print("Pick 2. to deposit money to your KZIP account")
    print("Pick 3. to withdraw cash from your KZIP account")
    print ("Pick 4.to check your KZIP account balance")

    choice=int(input("Pick from 1-5\n"))

    if choice==1:
        print ("Welcome to KZIP Bank")
        print ("See you want to create an account With Us")
        account_number=int (input("Create your New account number\n"))
        initial_balance=int (input("Enter your initial balance\n"))
        accounts[account_number]=BankManager(account_number,initial_balance)
        print ("Successfully Created Account")

    if choice==2:
        account=int(input("Enter you KZIP account number\n"))
        if account not in accounts:
            print ("You dont have a KZIP bank account")
            print('')
            print("Press 1.to create")

        else:
            deposit = int(input("Enter the money you want to deposit\n"))
            n = accounts[account].deposit(deposit)
            print("Your balance is", n)
    if choice==3:
        account = int(input("Enter you KZIP account number\n"))
        if account not  in accounts:
            print("You dont have a KZIP account")
        else:
            withdraw = int(input("Enter the money you want to deposit\n"))
            w=accounts[account].withdraw(withdraw)
            print("Your balance is",w)

        if choice==4:
            account = int(input("Enter you KZIP account number\n"))
        if account not in accounts:
                print("You dont have a KZIP account")
        else:
                b=accounts[account].balance()
                print(b)
