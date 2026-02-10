# Task 2 (Class Variable + Classmethod + Staticmethod) – Simple Problem Statement
# Problem: Student College System
# You want to create a student system where college name is same for all students.
# What to do
# Create class Student with:
# Class Variable
# college_name = "ABC College"
#  (common for all students)
# Constructor
# takes name and roll_no
# Classmethod
# change_college(new_name)
#  to update the college name for all students.
# Staticmethod
# is_pass(marks)
#  returns pass or fail (example: pass if marks >= 35)
# Instance method
# display() prints student details
# How it works
# Create 2 students
# Print both details
# Change college using classmethod
# Print again → both students should show new college name
# Use staticmethod to check pass/fail

class Student:

    college_name = "ABC College"

    #constructor
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name
    
    @staticmethod
    def is_pass(marks):
        if marks>=35:
            print("Result:" ,"pass")
        else:
            print("Result:","fail")
    
    #instance method
    def display(self):
        print("name:",self.name)
        print("roll num:",self.roll_no)
        print("college:",Student.college_name)
        print("---------------------------")

s1=Student("chandu",9)
s2=Student("Anu",10)

s1.display()
s2.display()

#class method
Student.change_college("bdc college")

s1.display()
s2.display()

#static method
Student.is_pass(35)
Student.is_pass(30)





