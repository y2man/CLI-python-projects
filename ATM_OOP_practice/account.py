from abc import ABC, abstractmethod
from datetime import datetime
from transaction import Transaction

class Account(ABC):
    @abstractmethod
    def __init__(self, accountNumber, ownerName, pin, balance):
        self.accountNumber = accountNumber
        self.ownerName = ownerName
        self.transactions = []
        self.__pin = pin
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def auth_pin(self, pin):
        if pin == self.__pin:
            return True
        return False

    def deposit(self, amount):
        if amount <= 0:
            print(f"the input amount {amount} is invalid, should be greater than 0!")
        self.__balance += amount
        now = datetime.now()
        now.strftime("%Y-%m-%d %H:%M:%S")
        transaction = Transaction("deposit", amount, now)
        self.transactions.append(transaction)
        print(f"Amount {amount} deposited successfully!, current balance is {self.__balance}")
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_full_info(self):
        message = f"Account number : {self.accountNumber} \n Name : {self.ownerName} \n Balance : {self.__balance}"
        print(message)
        if len(self.transactions) == 0:
            print("No transactions yet!")
        for i,transaction in enumerate(self.transactions):
            print(f"Transaction {i+1}:")
            print(f"transaction type : {transaction.type}")
            print(f"transaction amount : {transaction.amount}")
            print(f"transaction time : {transaction.timestamp}")
    
    def _adjust_balance(self, amount):
        self.__balance -= amount




        

    
