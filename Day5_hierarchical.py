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
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance =0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited amount", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            self.display_balance()
        else:           
            print("Insufficient balance.")

    def display_balance(self):
        print(" the Balance is :", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder) 
#why we use super() here because we want to call the constructor of the parent class BankAccount
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance = self.balance + interest
        self.display_balance() # This will display the new balance after adding interest.

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        #overdraft is allowing the account holder to withdraw more money than they have in 
        # their account, up to a certain limit.
        if amount <= self.balance + self.overdraft_limit: # 590<=100+500 =600 True
            self.balance -= amount  #500-590=-90
            self.display_balance()
        else:
            print("Withdrawal amount exceeds overdraft limit. Transaction denied.")

# Object Creation and Testing
SA=SavingsAccount("alice", 10)
CA=CurrentAccount("bob", 100)

# SA.deposit(100)
# SA.withdraw(30)
# SA.add_interest()

CA.deposit(500)
CA.withdraw_with_overdraft(590)