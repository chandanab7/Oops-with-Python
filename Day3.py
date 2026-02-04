class Parent_class:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def parent_mathod(self):
        print("This is parent class method")

class child_class(Parent_class):
    def __init__(self,c1,c2):
        super().__init__(3,4)
        print(super().p1) #3
        self.c1=c1
        self.c2=c2
    def child_method(self):
        print("This is child class method")
# # Create an object of child_class
# child_object=child_class("child1_value","child2_value","parent1_value","parent2_value")
