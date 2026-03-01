from account import Account
from transaction import Transaction
from datetime import datetime

class SavingAccount(Account):
    def __init__(self, accountNumber, ownerName, pin, balance):
        super().__init__(accountNumber, ownerName, pin, balance)
        self.interestRate = 0.07
    
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._adjust_balance(amount)
            now = datetime.now()
            now.strftime("%Y-%m-%d %H:%M:%S")
            transaction = Transaction("withdraw", amount, now)
            self.transactions.append(transaction)
            print(f"Amount {amount} withdrawn successfully! current amount is {self.get_balance()}")
        elif amount < 0:
            print("Invald Amount")
        print(f"Insufficient amount")
    
    
# another account types can be added below
    
