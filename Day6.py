#encapsulation
#syntax
# class class_name:
#     var1=value1
#     _var2=value2
#     __var3=value3
#     def __init__(self):
#         #initialization code
#     def method_name(self):
#         #implementation code
#     def getter_method(self): # getter method to access private variable
#         return self.__var3
    
#     def setter_method(self, value):# setter method to update private variable
#         self.__var3=value


#banking system using encapsulation

class BankAccount:
    account_holder_name = "unknown" 
    _account_type="Savings"

    def __init__(self,pin):
        self.__pin=pin #unknown pin that is givin by bank to the account holder
        self.__balance=0

    def set_account_name(self,name):
        self.account_holder_name=name

    def get_account_name(self):
        return self.account_holder_name
    
    def set_pin(self,new_pin): #setted a new pin
        self.__pin=new_pin
        print("PIN updated successfully")

    def get_pin(self): #getter method to access private variable
        return self.__pin

    def get_balance(self,new_pin):
        if new_pin==self.__pin:
            return self.__balance
        else:
            print("Access Denied! Incorrect PIN")

    def set_balance(self,amount,new_pin):
        if new_pin==self.__pin:
            self.__balance+=amount
            print("Balance updated successfully")
        else:
            print("Access Denied! Incorrect PIN")

object=BankAccount(1234)
print(object.account_holder_name) 
object.account_holder_name="John Doe"
print("the updated account holder name is:",object.account_holder_name)
# print("the account old pin is:",object.get_pin())
object.set_pin(5678) 
print("the account new pin is:",object.get_pin())
print("the current balance is:",object.get_balance(5678))
object.set_balance(1000,5678)
print("the updated balance is:",object.get_balance(5678))
object.set_balance(500,1234)