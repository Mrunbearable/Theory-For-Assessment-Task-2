class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def get_owner_name(self):
        return self.owner_name

    def get_balance(self):
        return self.balance

    def set_owner_name(self, new_name):
        if new_name:
            self.owner_name = new_name
        else:
            print("Please insert a name")

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.balance = new_balance
        else:
            print("Balance Not Accepted")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Balance Not Accepted.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        return f"BankAccount({self.__account_number}, {self.__owner_name}, Balance: ${self.__balance})"
