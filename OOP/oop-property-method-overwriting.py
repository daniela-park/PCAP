# Creating classes
class Animal():
    # Constructor
    def __init__(self):
        self.species = "general"

    # Method
    def produce_sound(self):
        print("General animal sound")

# Class Dog inherits from class Animal
class Dog(Animal):
    pass        

# Creating an object
dog1 = Dog()
# Printing the object's property inherited from the superclass
print(dog1.species) # general
# Calling the objetc's method inherited from the superclass
dog1.produce_sound() # General animal sound

# Overwriting the superclass properties and methods
class Animal():
    def __init__(self):
        self.species = "general"

    def produce_sound(self):
        print("General animal sound")

class Dog(Animal):
    def __init__(self):
        self.species = "Canis familiaris"

    def produce_sound(self):
        print("Woof, woof") 

# Creating an object
dog1 = Dog()
# Printing the object's property
print(dog1.species) # Canis familiaris
# Printing the object's method
dog1.produce_sound() # Woof, woof

# Creating an object for each class
animal1 = Animal()
animal2 = Dog()

# Calling the method of each class
animal1.produce_sound() # General animal sound
animal2.produce_sound() # Woof, woof

# Calling a subclass method in the superclass
class Animal():
    def __init__(self):
        self.species = "general"

    def produce_sound(self):
        print("General animal sound")

    def present(self):
        print("The animal produces the following sound: ")
        self.produce_sound()

class Dog(Animal):
    def __init__(self):
        self.species = "Canis familiaris"

    def produce_sound(self):
        print("Woof, woof")

# Creating an object for each class
animal1 = Animal()
animal2 = Dog()

# Calling the superclass method, which calls a subclass method
animal1.present() # The animal produces the following sound: General animal sound
animal2.present() # The animal produces the following sound: Woof, woof