# Creating 3 simple classes which inherits from each other
class Vehicle():
    pass

class LandVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass 

# Checking if Car is a subclass of LandVehicle
issubclass(Car, LandVehicle) # True

# Checking if Car is a subclass of Vehicle
issubclass(Car, Vehicle) # True

# Checking if Vehicle is a subclass of Car
issubclass(Vehicle, Car) # False

# A class is a subclass of itself
issubclass(Car, Car) # True