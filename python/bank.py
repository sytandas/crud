class BankAccount:
    def __init__ (self, account_number, balance, date_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_opening = date_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited in your account")
    
    def withdraw(self, amount, customer_name):
        if amount >= self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"customer: {self.customer_name} after withdrawing {amount} balance: {self.balance}")
    
    def check_balance(self, balance):
        print(f"current balance is: {self.balance}")

    def acc_info(self):
        print(f"account number: {self.account_number}, name: {self.customer_name}, balance: {self.balance}")
        print("-------------------------------------------------------------------------------------------")

ba_1 = BankAccount("P00001", 5000000, "31-05-2023", "user_a")
ba_2 = BankAccount("P00010", 7000000, "11-05-2023", "user_b")
ba_3 = BankAccount("P00011", 9000000, "06-05-2023", "user_c")

ba_1.acc_info()
ba_2.acc_info()
ba_3.acc_info()

ba_1.deposit(200)
ba_1.acc_info()

ba_2.withdraw(500, "user_b")
ba_2.acc_info()
