# Creating a class
class Vehicle():
    def show_power_type(self):
        print("This Vehicle can use different power sources.")

# Creating a class which inherits from Vehicle
class Elec_Vehicle(Vehicle):
    def show_power_type(self):
        print("This Electric Vehicle can use electricty.")

# Creating another class which inherits from Vehicle
class Petr_Vehicle(Vehicle):
    def show_power_type(self):
        print("This Petrol Vehicle can use petrol.")

# Creating a class that inherits from both Elec_Vehicle and Petr_Vehicle
class Hybrid_Car(Elec_Vehicle, Petr_Vehicle):
    pass

# Creating an object and calling the method
hyb_car = Hybrid_Car()
hyb_car.show_power_type() # This Electric Vehicle can use electricty.

# Python solves the diamond problem by reading the classes from L to R
# Changing the order which the superclasses are written
class Hybrid_Car(Petr_Vehicle, Elec_Vehicle):
    pass

# Creating an object and calling the method
hyb_car = Hybrid_Car()
hyb_car.show_power_type() # This Petrol Vehicle can use petrol.