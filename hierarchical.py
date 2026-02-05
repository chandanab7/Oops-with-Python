# Task-1: Hierarchical Inheritance 
# Problem Statement
# Create a program for a Bank System using Hierarchical Inheritance.
# Requirements
# Create a parent class BankAccount
# Attributes:
# account_holder
# balance
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# Create a child class SavingsAccount that inherits from BankAccount
# Attribute:
# interest_rate
# Method:
# add_interest()
# Create another child class CurrentAccount that inherits from BankAccount
# Attribute:
# overdraft_limit
# Method:
# withdraw_with_overdraft(amount)
# Create one object of SavingsAccount and one object of CurrentAccount and test all methods.


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount", amount, "New balance is :",self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrew amount.", amount, "New balance is", self.balance)

    def display_balance(self):
        print("Account holder:",self.account_holder, ", Balance:", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Added interest:",interest, "New balance is", self.balance)

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        # the withdrawal amount method checking the overdraft limit which means if the amount is greater than balance + overdraft limit
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print("Withdrew amount with overdraft. New balance is", self.balance)


# Object Creation and Testing
savings_account = SavingsAccount("Alice", 1000, 5)
savings_account.display_balance()
savings_account.deposit(500)
savings_account.add_interest()
savings_account.withdraw(200)
savings_account.display_balance()



current_account = CurrentAccount("Bob", 500, 200)
current_account.display_balance()
current_account.withdraw_with_overdraft(700)
current_account.display_balance()