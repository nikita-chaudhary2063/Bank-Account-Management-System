
'''
Bank Account Management System
'''

class BankAccount:
    bank_name = "Nepal Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} has Rs. {self.balance} in their account at {self.bank_name}."

    def show_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print(f"Owner's name: {self.owner}")
        print(f"Balance: Rs. {self.balance}")
        print(f"Bank: {self.bank_name}")

    def deposit_amount(self):
        amount = int(input("How much do you want to deposit? Rs. "))

        if amount > 0:
            self.balance = self.balance + amount
            print("Amount deposited successfully!")
            print(f"Updated balance: Rs. {self.balance}")
        else:
            print("Sorry! Amount must be greater than zero.")

    def withdraw_amount(self):
        amount = int(input("How much do you want to withdraw? Rs. "))

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - amount
            print("Amount withdrawn successfully!")
            print(f"Remaining balance: Rs. {self.balance}")


account1 = BankAccount("Nikita", 20000)
account2 = BankAccount("Ram", 50000)

while True:
    print("\n===== WELCOME TO NEPAL BANK =====")
    print("Choose your account:")
    print("1. Nikita")
    print("2. Ram")
    print("3. Exit")

    account_choice = input("Choose your account: ")

    if account_choice == "1":
        selected_account = account1

    elif account_choice == "2":
        selected_account = account2

    elif account_choice == "3":
        print("Thank you for using Nepal Bank!")
        break

    else:
        print("Invalid account choice!")
        continue

    # Transaction menu for the selected account
    while True:
        print(f"\n===== {selected_account.owner}'s ACCOUNT =====")
        print("1. Deposit amount")
        print("2. Withdraw amount")
        print("3. Check balance")
        print("4. Show account details")
        print("5. Switch account")

        choice = input("What do you want to do? ")

        if choice == "1":
            selected_account.deposit_amount()

        elif choice == "2":
            selected_account.withdraw_amount()

        elif choice == "3":
            print(f"Current balance: Rs. {selected_account.balance}")

        elif choice == "4":
            selected_account.show_details()

        elif choice == "5":
            print("Returning to account selection...")
            break

        else:
            print("Invalid choice! Please choose 1 to 5.")
