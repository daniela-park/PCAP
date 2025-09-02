# Creating 3 classes that inherits from each other
class Vehicle():
    pass

class LandVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass

# Creating an object from class Car and printing its dictionary
car1 = Car()
print(car1.__dict__) # {}

# Adding a constructor to class Vehicle, which accepts a parameter
class Vehicle():
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass

# Creating an object, passing the speed as parameter and printing the dict
car1 = Car(5)
print(car1.__dict__) # {'speed': 5}
# Car inherited the property from Vehicle, since LandVehicle didn't have any

# Adding a constructor to class LandVehicle, which also accepts a parameter
class Vehicle():
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

class Car(LandVehicle):
    pass

# Creating an object, passing the wheel_count as parameter and printing the dict
car1 = Car(5)
print(car1.__dict__) # {'wheel_count': 5}
# Car inherits the constructor from LandVehicle, instead of Vehicle

# Calling the superclass constructor in the subclass
class Vehicle():
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        Vehicle.__init__(self, speed) # Superclass constructor
        # Another way of calling the superclass constructor:
        # super().__init__(speed) # Note that self is not needed
        self.wheel_count = wheel_count

class Car(LandVehicle):
    pass

# Creating an object, passing the wheel_count as parameter and printing the dict
car1 = Car(50, 4)
print(car1.__dict__) # {'speed': 50, 'wheel_count': 4}

# Accessing the spped of the object
car1.speed # 50
# The value extracted from superclass Vehicle