import datetime
import sys

class BankAccount:
        account_counter = 0
        
        def __init__(self, acc_id):
                self.id = acc_id
                self.acc_holder = {1: "John Doe", 2: "Christian", 3: "Prince", 4: "Adrian", 5: "Markus", 6: "Sherwin"}
                self.fixed_balance = {1: 1000.00, 2: 500.00, 3: 1500, 4: 0.00, 5: 1000000, 6: 69}
                self.current_balance = self.fixed_balance.get(self.id, 0.00)
        
        # Deposit money on bank account
        def bank_deposit(self, amount):
                self.current_balance += amount
                print("Date and Time:", datetime.datetime.now())
                print(f"Deposit of ${amount:.2f} successful.")
                self.get_balance()
            
        # Withdraw money on bank account
        def bank_withdraw(self, amount):
                if self.current_balance >= amount:
                        self.current_balance -= amount
                        print()
                        print("Date and Time:", datetime.datetime.now())
                        print(f"Withdrawal of ${amount:.2f} successful.")
                        self.get_balance()
                else:
                        print("Insufficient funds.")
        
        # Get the current balance of the account
        def get_balance(self):
                print(f"Current Balance: ${self.current_balance:.2f}")
            
        # Display the bank info
        def display_bank_info(self):
                print(f"Account Holder: {self.acc_holder[self.id]}")
                print(f"Current Balance: ${self.current_balance:.2f}")
            
        # Display bank option
        def bank_option(self):
                bank_option = input("\nA) Withdraw\nB) Deposit\nC) Exit\n\n").lower()
                
                if bank_option == "a":
                        withdraw_amount = float(input("Withdraw amount: $"))
                        self.bank_withdraw(withdraw_amount)
                        
                elif bank_option == "b":
                        deposit_amount = float(input("Deposit amount: $"))
                        self.bank_deposit(deposit_amount)
                
                elif bank_option == "c":
                        print("Thank you, come again.")
                        print()
                        sys.exit()
                        
                else:
                        print()
                        print("Invalid Input.")

# Main
if __name__ == "__main__":
        while True:
                try:
                        print()
                        acc_id = int(input("Account Number: "))
                        
                        if acc_id not in [1, 2, 3, 4, 5, 6]:
                                print("Account Number Not Found\n")
                                continue
        
                        account = BankAccount(acc_id)
                        account.display_bank_info()
                        
                        #Loop after every transaction to perform another transaction
                        while True:
                                account.bank_option()
                                print()
                                continue_option = input("Do you want to perform another transaction?\nA) Yes\nB) No\n\n").lower()
                                
                                if continue_option == "a":
                                    break
                                
                                elif continue_option == "b":
                                    print()
                                    print("Thank you, come again.")
                                    print()
                                    sys.exit()
                                else:
                                    print("Invalid input..")
                                    sys.exit()

                except ValueError:
                    print("Invalid Input. Try Again")
                    continue



