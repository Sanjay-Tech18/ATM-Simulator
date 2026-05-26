class ATM:
    def __init__(self):
        self.balance = 10000  # Default balance
        self.pin = "1234"     # Default PIN

    def check_pin(self):
        entered_pin = input("Enter your 4-digit PIN: ")
        return entered_pin == self.pin

    def show_menu(self):
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}")

    def deposit_money(self):
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{self.balance}")
        else:
            print("Invalid amount.")

    def withdraw_money(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{self.balance}")

    def run(self):
        print("===== Welcome to Python ATM =====")

        if not self.check_pin():
            print("Incorrect PIN. Access Denied.")
            return

        while True:
            self.show_menu()
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                print("Thank you for using Python ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")


# Run Program
atm = ATM()
atm.run()
