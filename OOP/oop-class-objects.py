# Creating a class with default values
class Fruit:
    # Class constructor
    def __init__(self):
        self.fruit_name = "banana"
        self.fruit_colour = "yellow"

    # Class method
    def describe_fruit(self):
        print("The", self.fruit_name, "is", self.fruit_colour)

# Creating an object
fruit1 = Fruit()
# Calling the method
fruit1.describe_fruit() # The banana is yellow
# Accessing the object properties
print(fruit1.fruit_name) # banana
print(fruit1.fruit_colour) # yellow

# Creating a class with parameters
class Fruit:
    # Constructor
    def __init__(self, fruit_name, fruit_colour):
        self.fruit_name = fruit_name
        self.fruit_colour = fruit_colour

    # Class method
    def describe_fruit(self):
        print("The", self.fruit_name, "is", self.fruit_colour)

# Creating an object and passing the parameters
fruit1 = Fruit("banana", "yellow")
# Calling the method
fruit1.describe_fruit() # The banana is yellow
# Accessing the object properties
print(fruit1.fruit_name) # banana
print(fruit1.fruit_colour) # yellow

# Creating several objects
fruit1 = Fruit("banana", "yellow")
fruit2 = Fruit("strawberry", "red")
fruit3 = Fruit("cherry", "purple")

# Calling the methods for each object created
fruit1.describe_fruit() # The banana is yellow
fruit2.describe_fruit() # The strawberry is red
fruit3.describe_fruit() # The cherry is purple