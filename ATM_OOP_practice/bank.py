from account_types import SavingAccount
import random

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self):
        accNum = random.randint(10001000, 10009999)
        while accNum in self.accounts:
            accNum = random.randint(10001000, 10009999)
        print("Enter the type of account to create!")
        print("1: Savings account \n2: Checking account")
        t = int(input("Enter: "))

        if t < 1 or t > 2:
            print("invalid input!")
            return
        
        if t == 1:
            name = input("Enter owner full name: ")
            tries = 0
            while tries < 4:
                pin = int(input("Enter a 4 digit pin: "))
                pinTest = int(input("Enter pin again: "))
                if pin == pinTest:
                    break
                tries += 1
                print("Pin doesn't match")
            if tries == 4:
                print("aborting...")
                return
            
            balance = int(input("Enter initial balance: "))

            account = SavingAccount(accNum, name, pin, balance)
            self.accounts[accNum] = account
            print("Account created successfully!")
            print("Account details: ")
            print(f"Account number : {accNum} \nCustomer Name : {name} \nPin : {pin} \nInitial balance : {balance}")



        else:
            print("Feature coming soon...")

        
    def get_account(self, accNum):
        if accNum in self.accounts:
            return self.accounts[accNum]
        print("Account does not exist")
        return
    
    
    



            





    