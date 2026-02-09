# Task-2: Abstraction – Vehicle System
# Problem Statement
# Create a program for a Vehicle System using Abstraction.
# Requirements
# Create an abstract class Vehicle
# abstract method: start_engine()
# Create child class Car
# implement start_engine()
# Create child class Bike
# implement start_engine()
# Create child class Bus
# implement start_engine()
# Create objects and call start_engine() method.


from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def concrete_method(self):
        print("I am a concrete method from class Vehicle")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started.")

object1 = Car()
object2 = Bike()
object3 = Bus()
object1.start_engine()
object3.concrete_method() #MRO method