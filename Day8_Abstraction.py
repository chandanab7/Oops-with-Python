
#SYNTAX-------------------------------------------

# from abc import ABC, abstractmethod

# class ClassName(ABC):
#     @abstractmethod
#     def abs_method(self):
#         pass
#     def concrete_method(self):
#         implementation of concrete method

# class ClassName2(ClassName):
#     def abs_method(self):
#        implementation of abstract method




from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod #decorator is used to declare a method as abstract method
    def method1(self):
        pass
    def concrete_method(self): #concrete method means normal method present in abstract class
        print(" i am a concrete method from class A")
class B(A):
    def method2(self):
        print("Method 2 from class B")
    def method1(self):
        print("Method 1 from class B")

obj=B()
obj.method1()
obj.concrete_method() #MRO method