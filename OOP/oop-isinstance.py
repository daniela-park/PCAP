# Creating 3 classes that inherits from each other
class Vehicle():
    # Constructor
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    # Constructor
    def __init__(self, speed, wheel_count):
        super().__init__(speed) # Calling the superclass constructor
        self.wheel_count = wheel_count

class Car(LandVehicle):
    pass

# Creating objects for each class
veh = Vehicle(50)
lveh = LandVehicle(50, 4)
car1 = Car(100, 4)

# Checks if all objects are instances of class Vehicle
print(isinstance(veh, Vehicle)) # True
print(isinstance(lveh, Vehicle)) # True
print(isinstance(car1, Vehicle)) # True

# Checks if all objects are instances of class LandVehicle
print(isinstance(veh, LandVehicle)) # False
print(isinstance(lveh, LandVehicle)) # True
print(isinstance(car1, LandVehicle)) # True

# Checks if all objects are instances of class Car
print(isinstance(veh, Car)) # False
print(isinstance(lveh, Car)) # False
print(isinstance(car1, Car)) # True

# Copying the object to a new variable that will point to the same memory location
veh = Vehicle(50)
new_veh = veh

# Checking if the objects are identical
print(veh is new_veh) # True

# Printing the dict for both original object and the copied one
print(veh.__dict__) # {'speed': 50}
print(new_veh.__dict__) # {'speed': 50}

# Checking if changing the object also changes its copy
veh.speed = 25
print(veh.__dict__) # {'speed': 25}
print(new_veh.__dict__) # {'speed': 25}

# To make the copy point to another memory location, create a new object in the same var
veh = Vehicle(50)
new_veh = Vehicle(25)

# Checking if changing the object ad its copy will have different values
print(veh.__dict__) # {'speed': 50}
print(new_veh.__dict__) # {'speed': 25}

# Checking how it works with int
first_num = 5
second_num = 5
print(first_num is second_num) # True

# Checking how it works with int
first_num = 5
second_num = 2
second_num += 3
print(first_num is second_num) # True

# Checking how it works with str
str1 = "Hello"
str2 =  "Hello"
print(str1 is str2) # True

# Checking how it works with str
str1 = "Hello"
str2 =  "Hell"
str2 += "o"
print(str2) # Hello
print(str1 is str2) # False
print(str1 == str2) # True