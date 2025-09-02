# Creating a class
class Vehicle():
    # Class variable
    class_message = "This is the Vehicle class"
    # Constructor
    def __init__(self, speed):
        self.speed = speed

# Creating a class from Vehicle,
# inheriting speed from superclass Vehicle and printing superclass variable
class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(Vehicle.class_message)
        # print(super().class_message) # Another way of accessing the superclass variable

# Creating a class from LandVehicle
class Car(LandVehicle):
    pass

# Creating an object with 2 attributes required from the superclass LandVehicle
car1 = Car(50, 4) # This is the Vehicle class

# Accessing the superclass message through the object
car1.class_message # 'This is the Vehicle class'

# Adding methods to subclasses LandVehicle and Car
class Vehicle():
    class_message = "This is the Vehicle class"
    def __init__(self, speed):
        self.speed = speed

# Method speed_up added
class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(super().class_message)

    def speed_up(self):
        self.speed += 5

# Method super_speed added, which inherits from LandVehicle.speed_up()
class Car(LandVehicle):
    def super_speed(self):
        print("Super speed activated")
        super().speed_up()

car1 = Car(50, 4) # This is the Vehicle class
print(car1.__dict__) # {'speed': 50, 'wheel_count': 4}
car1.super_speed() # Super speed activated
print(car1.__dict__) # {'speed': 55, 'wheel_count': 4}