#class method 
#class variable
#instance variable
#instance method
#static method
#static variable


from symtable import Class


class A:
    x=10 #class variable
    def __init__(self):
        pass
    
    @classmethod #class method
    def class_method(cls):
        cls.x+=1 #class variable

    @staticmethod
    def static_method(a,b): #static method
        print("I am a static method")
        print(a+b)

class B(A):
    def inc(self): #instance method
        self.x+=1 #instance variable
        print(self.x)
class C(A):
    def inc(self):
        self.x+=1 #instance variable
        print(self.x)

# a=A()
# a.x+=1 
# print(a.x)   #class variable is accessed and modified using class name
    # # A.x+=1
    # # print(a.x)   

# b=B()
# print(b.x) 

# c=C()
# print(c.x) 

A.static_method(5,10) # no need to create object to call static method, it can be called using class name.