
class Atm:
    def __init__(self, bank):
        self.bank = bank

    def login(self, accNum, pin):
        account = self.get_account(accNum)
        if not account:
            print("login failed")
            return
        auth = account.auth_pin(pin)
        if auth:
            print(f"Hello, {account.ownerName}")
            return account
        print("login Failed")
        return

    def get_account(self, accNum):
        if accNum in self.bank.accounts:
            return self.bank.accounts[accNum]
        print("account does not exist")
        return

    def authenticate(self, accNum, pin):
        acc = self.bank.accounts[accNum]
        if acc.pin == pin:
            return True
        return False
    
