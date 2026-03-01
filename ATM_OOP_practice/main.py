from bank import Bank
from ATM import Atm

BANK = Bank()
ATM = Atm(BANK)

def main():
    print("1: Create Account \n2: Login \nOther: Terminate program")
    choice = int(input("Enter choice: "))

    if choice == 1: 
        BANK.create_account()
        main()
        return
    elif choice == 2:
        print("Login page!")
        accNum = int(input("Enter account Number: "))
        pin = int(input("Enter pin: "))

        account = ATM.login(accNum, pin)

        if not account:
            main()
            return
        
        print(f"Hello, {account.ownerName}")
        print("1: withdraw \n2: deposit \n3: Display full information: \nothers: Logout")
        ch = int(input("Enter choice: "))

        if ch == 1:
            amount = int(input("Enter withdraw amount: "))
            account.withdraw(amount)
            main()
            return
        elif ch == 2:
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
            main()
            return
        elif ch == 3:
            account.display_full_info()
            main()
            return
        else:
            main()
            return
    else:
        print("Goodbye!")
        return
    

if __name__ == "__main__":
    main()
        



