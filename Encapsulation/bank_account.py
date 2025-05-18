class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0):
        """Initialize a bank account with private attributes."""
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = balance

    # Getter methods
    def get_account_number(self):
        return self.__account_number

    def get_owner_name(self):
        return self.__owner_name

    def get_balance(self):
        return self.__balance

    # Setter methods
    def set_owner_name(self, new_name):
        if new_name:
            self.__owner_name = new_name
        else:
            print("Invalid name. Owner name cannot be empty.")

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative.")

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def __str__(self):
        return f"BankAccount({self.__account_number}, {self.__owner_name}, Balance: ${self.__balance})"
