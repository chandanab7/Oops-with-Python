# Task/Assignment
# Task-1: Polymorphism – Payment System
# Problem Statement
# Create a program for a Payment System using method overriding.
# Requirements
# Create a parent class Payment
# method: pay()
# Create child class GooglePay (inherits Payment)
# override pay()
# Create child class PhonePe (inherits Payment)
# override pay()
# Create child class CreditCard (inherits Payment)
# override pay()
# Create one object for each class and call pay() method.


class Payment:
    def pay(self):
        print("Payment method not specified.")

class GooglePay(Payment):
    def pay(self):
        print("Payment made using Google Pay.")

class PhonePe(Payment):
    def pay(self):
        print("Payment made using PhonePe.")

class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card.")
    
#the object of the classes are created and the methods of each class are called.

object1 = GooglePay()
object2 = PhonePe()
object3 = CreditCard()
object1.pay()
object2.pay()
object3.pay()

