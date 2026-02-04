#single inheretance

class father:
    def __init__(self,surname,father_name):
        self.surname=surname
        self.father_name=father_name
    def display_surname(self):
        print("Father's surname is:",self.surname)
    def display_father_name(self):
        print("Father's name is:",self.father_name)
        
class son(father):
    def __init__(self,name,surname,father_name):
        super().__init__(surname,father_name)
        self.name=name
    def display_name(self):
        print("Son's name is:",self.name)

child_object=son("John","C","smith")
child_object.display_surname()
child_object.display_father_name()
child_object.display_name()