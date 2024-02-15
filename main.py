import datetime


class BankAccount:
    account_counter = 0
        
    def __init__(self, account_holder, balance=0):
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter
        self.account_holder = account_holder
        self.balance = balance
             

        #Bank deposit
    def bank_deposit(self, amount):
        self.balance += amount
        print()
        print("\nCurrent Date and Time:", datetime.datetime.now())
        print(f"Deposit of ${amount:.2f} successful.")
        self.get_balance()
              
        #Bank withdraw
    def bank_withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print()
            print("\nCurrent Date and Time:", datetime.datetime.now())
            print(f"Withdrawal of ${amount:.2f} successful.")
            self.get_balance()
        else:
            print("Insufficient funds.")

        #Get the the current balance of the account
    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
                
        #Display the bank info
    def display_bank_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

#Sample output
account = BankAccount("John Doe", 1000.00)
print("\nCurrent Date and Time:", datetime.datetime.now())
account.display_bank_info()


#Loop the option
while True:
        bank_option = input("\nA) Withdraw\nB) Deposit\n\n").lower()
        
        if bank_option == "a":
                withdraw_amount = float(input("Withdraw amount: $"))
                account.bank_withdraw(withdraw_amount)
        
        elif bank_option == "b":
                deposit_amount = float(input("Deposit amount: $"))
                account.bank_deposit(deposit_amount)
        
        else:
                print("Invalid Input.")
                break
