#Interface Segregation Principle

"""This principle states that no clients should be forced to depend upon interface that they do not use.
The interface should contain only the necessary abstract method and not more than that.
This principle include imposing the client with the burden of implementing methods that they don't 
acutally need or use. The interface with many additional useless methods are called fat interface.
This type of interface are less re-usable and the useless methods in interface leads to high coupling 
between classes."""

#Interface Segregation Principle Example:

"""Suppose we have an interface called "Bird".
This interface has many bird behaviours."""
from abc import ABC, abstractmethod

class Bird(ABC):
    
    @abstractmethod
    def sing(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def swim(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

"""Now, this interface is implemented by two bird classes. They are:"""

class Duck(Bird):
    def sing(self):
        return # Duck don't sing
    
    def run(self):
        return "Duck run fast"
    
    def swim(self):
        return "Duck swim beautifully"
    
    def fly(self):
        return # Duck cannot fly

"""The "Duck" class implements the "Bird" interface. It has to implement fly()
and sing() method unnecessarily (Duck doens't fly and sing)."""


class Parrot(Bird):
    
    def sing(self):
        return "Parrot sing joyfully"
    
    def run(self):
        return "Parrot run"
    
    def swim(self):
        return # Parrot cannot swim
    
    def fly(self):
        return "Parrot fly high up"
        

""" The "Parrot" class implements the "Bird" interface. It has to implement
swim() unnecessarily(Parrot doesn't swim)."""
# Both the above classes violates the Interface Segregation Principle.
            
"""Inorder to solve the above problem, the interface is splitted into two different
interfaces for two different classes so that each is not forced to implement the
methods they don't need."""

class NonFlyBird(ABC):
    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def swim(self):
        pass
    

class Duck(NonFlyBird):
    def run(self):
        return "Duck run fast"
    def swim(self):
        return "Duck swim beautifully"

"""The "Duck" class implements "NonFlyBird" interface as it contains only necessary
methods for "Duck" class."""

class FlyBird(ABC):
    @abstractmethod
    def fly(self):
        pass
    @abstractmethod
    def sing(self):
        pass
    @abstractmethod
    def run(self):
        pass
    

class Parrot(FlyBird):
    def fly(self):
        return "Parrot fly high up"
    def sing(self):
        return "Parrot sing joyfully"
    def run(self):
        return "Parrot run"
    
"""The "Parrot" class implements "FlyBird" interface as it contains only necessary
methods for "Parrot" class.

Interface Segregation Principle splits the interface into smaller and more specific
ones so that the clients will only use the methods they are interested in."""

