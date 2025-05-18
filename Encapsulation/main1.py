from bank_account import BankAccount

# Creating two bank account instances
account1 = BankAccount("123456", "Alice", 500)
account2 = BankAccount("789012", "Bob", 1000)

# Testing getter methods
print(account1.get_account_number())
print(account1.get_owner_name())
print(account1.get_balance())

print(account2.get_account_number())
print(account2.get_owner_name())
print(account2.get_balance())

# Testing setter methods
account1.set_owner_name("Alice Cooper")
account2.set_balance(1200)

# Testing deposit method
account1.deposit(200)
account2.deposit(500)

# Testing withdraw method
account1.withdraw(100)
account2.withdraw(1500)  # Should show insufficient funds message

# Display final account details
print(account1)
print(account2)
