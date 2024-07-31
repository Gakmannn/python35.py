from abc import ABC, abstractmethod

# Define a Walkable interface with a walk method
class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass

# Define a Flyable interface with a fly method
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

# Ostriche class implementing the Walkable interface
class Ostriche(Walkable):
    def walk(self):
        print("Ostriche is walking")

# Eagle class implementing both Walkable and Flyable interfaces
class Eagle(Walkable, Flyable):
    def fly(self):
        print("Eagle is flying")
    def walk(self):
        print("Eagle is walking")

# Creating instances and calling methods
try:
    obj = Eagle()
    # Expected: "Eagle is flying"
    obj.fly()

    # Expected: "Eagle is walking"
    obj.walk()
    obj2 = Ostriche()

    # Expected: "Ostriche is walking"
    obj2.walk()

except Exception as e:
        # Print any exceptions that might occur
        print(e)