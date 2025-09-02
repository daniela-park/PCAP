# Creating a subclass that inherits from 2 superclasses
class Vehicle:
    def go(self):
        print("Going!")

class Flyable():
    def fly(self):
        print("Flying!")

class Airplane(Vehicle, Flyable):
    pass

# Creating an object
plane1 = Airplane()
# Calling the methods
plane1.go() # Going!
plane1.fly() # Flying!

# Adding methods with the same name in the 2 superclasses
class Vehicle:
    def go(self):
        print("Going!")

    def introduce(self):
        print("This is a Vehicle.")

class Flyable():
    def fly(self):
        print("Flying!")

    def introduce(self):
        print("This is flyable.")

class Airplane(Vehicle, Flyable):
    pass

# Creating an object
plane1 = Airplane()
# Calling the methods
plane1.go() # Going!
plane1.fly() # Flying!
plane1.introduce() # This is a Vehicle.

# Changing the class order which the subclass inherits from
class Vehicle:
    def go(self):
        print("Going!")

    def introduce(self):
        print("This is a Vehicle.")

class Flyable():
    def fly(self):
        print("Flying!")

    def introduce(self):
        print("This is flyable.")
        
# Changing the class order
class Airplane(Flyable, Vehicle):
    pass

# Creating an object
plane1 = Airplane()
# Calling the methods
plane1.go() # Going!
plane1.fly() # Flying!
plane1.introduce() # This is flyable.

# Adding a method with the same name to the subclass
class Vehicle:
    def go(self):
        print("Going!")

    def introduce(self):
        print("This is a Vehicle.")

class Flyable():
    def fly(self):
        print("Flying!")

    def introduce(self):
        print("This is flyable.")

class Airplane(Flyable, Vehicle):
    def introduce(self):
        print("This is an airplane.")

# Creating an object
plane1 = Airplane()
# Calling the methods
plane1.go() # Going!
plane1.fly() # Flying!
plane1.introduce() # This is an airplane.