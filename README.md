# Bank-Account-Management-System
Create a simple bank account management system using classes in Python. Add date and time on top of your output. 

1. The BankAccount class should have the following:
   > account_number - a unique identifief for the bank account (you can use a simple incremental integer starting from 1).
   > account_holder - the name of the account holder
   > balance - the current balance of the account (initialized to 0).

2. implement the following methods in the BankAccount class:
   > deposit(amount) - Add the specified amount to the account balance
   > withdraw(amount) - Subtracts the specified amount from the account balance. Ensure that the account has suffiecient funds before allowing the withdrawals.
   > get_balance() - returns the current balance of the account
   > display_info() - prints out the account information, including the account number, account holder name, and current balance.

3. create an instance of the BankAccount classs and demonstrate the functionality by performing the following actions.
   > deposit an initial amount into the account.
   > Withdraw some funds from the account.
   > Display the current balance and account information.

**sample output**
account number: 1
acount holder: John Doe
Balance: $1000.00

Withdrawal of $500.00 successful.
Current Balance: $500.00
