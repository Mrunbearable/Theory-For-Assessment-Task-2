from bank_account import BankAccount

account1 = BankAccount("178456", "Alice", 123)
account2 = BankAccount("789012", "Jaquavis", 10000000)

print(account1.get_account_number())
print(account1.get_owner_name())
print(account1.get_balance())

print(account2.get_account_number())
print(account2.get_owner_name())
print(account2.get_balance())

account1.set_owner_name("Alice Cooper")
account1.deposit(200)
account1.withdraw(100)
account2.set_balance(1200)
account2.deposit(500)
account2.withdraw(1500)
print(account1)
print(account2)
