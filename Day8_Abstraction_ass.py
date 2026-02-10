# Task 1 (Abstraction) – Simple Problem Statement
# Problem: Animal Sound System
# You want to create an Animal system where every animal must make a sound.
# What to do
# Create an abstract class Animal
# Create an abstract method sound()
# Create a normal method sleep() (common for all animals)
# Then create child classes:
# Dog → sound() prints Bark

# Cat → sound() prints Meow

# Cow → sound() prints Moo

# How it works
# Animal class will force all child classes to write their own sound()

# But sleep() is common so it can be used directly.

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("sleeping")

class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("meow")
      
class Cow(Animal):
    def sound(self):
        print("Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()