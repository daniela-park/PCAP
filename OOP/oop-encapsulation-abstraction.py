# Creating a class that accepts 3 parameters
class Car():
    def __init__(self, model, colour, speed):
        self.model = model
        self.colour = colour
        self.speed = speed
# Creating an object with 3 attributes
car1 = Car("Tucson", "black", 100)

# Creating a class with a default value
class Car():
    def __init__(self, model, colour, speed = 0):
        self.model = model
        self.colour = colour
        self.speed = speed
# Creating an object with 2 attributes only, since speed has a default value
car1 = Car("Tucson", "black")

# Creating a class and adding methods to it
class Car():
    def __init__(self, model, colour, speed = 0):
        self.model = model
        self.colour = colour
        if speed < 0:
            self.speed = 0
        else:
            self.speed = speed

    def speed_up(self):
        self.speed += 5

    def slow_down(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def show_current_speed(self):
        print("The new speed of the", self.colour, self.model, "is", self.speed)
# Creating an object with 2 attributes only, since speed has a default value
car1 = Car("Tucson", "black")

# Calling the methods
car1.speed_up()
car1.speed_up()
car1.speed_up()
car1.slow_down()
car1.show_current_speed() # The new speed of the black Tucson is 10

# Calling the methods to force the speed to be negative
car1.slow_down()
car1.slow_down()
car1.show_current_speed() # The new speed of the black Tucson is 0

# Creating an object with 3 attributes, including a negative speed
car1 = Car("Tucson", "black", -50)
car1.show_current_speed() # The new speed of the black Tucson is 0

# Accessing the property and assigning a negative value to speed
car1.speed = -10
car1.show_current_speed() # The new speed of the black Tucson is -10
# To prevent the user from accessing the property
# mark it as private, so it can only be accessed within the class
# and it cannot be accessed after the objetc is created

# Creating a class with 3 parameters, including one private
class Car():
    def __init__(self, model, colour, speed = 0):
        self.model = model
        self.colour = colour
        if speed < 0:
            self.__speed = 0
        else:
            self.__speed = speed

    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_current_speed(self):
        print("The new speed of the", self.colour, self.model, "is", self.__speed)

car1 = Car("Tucson", "black")

# Trying to access the private parameter and assigning a value to it
car1.speed = -10
car1.show_current_speed() # The new speed of the black Tucson is 0
# Since the property is private, the class handles the user trying to assign a value to it