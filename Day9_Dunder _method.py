#Dunder - Double underscore methods

#__new__
#__init__
#__len__
#__str__
#__repr__
#__add__
#__equal__
#__enter__
#__exit__

""""class Test:
    def __new__(cls):
        print("Object is being created")
        return super().__new__(cls)
    
    def __init__(self):
        print("Initializd object")

t=Test()"""


class emp():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # def __str__(self):
    #     return  f"employee name is {self.name} and {self.salary} in his salary"
    
    # def __repr__(self):
    #     return self.name
        
    def __len__(self):
        arr=[1,2,3,4,5,6]
        sum=0
        for i in arr:
            sum+=1
        return sum

# e=emp("chandu",5000)
# print(e) # chandu
# print(len(e))  #6


    def __add__(self,other):
        return self.salary + other.salary
    
e1=emp("chandu",500)
e2=emp("anu",1000)

print(e1+e2)