# Creating a class
class House():
    # Class variable
    counter = 0
    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1

    # Class method
    def show_house_dets(self):
        print("The house at", self.address, "has an area of", self.area, "and costs", self.price)

# Creating an object
house1 = House("A", 100, 500000)
# Calling the method
house1.show_house_dets() # The house at A has an area of 100 and costs 500000
# Printing the class counter
print(House.counter) # 1 

# Creating 3 types of variables: class, object, local
class House():
    counter = 0
    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1

        House.quality = "low" # Class variable, even though it was created in the constructor
        self.quality = "medium" # Object variable as it's pointing to itself
        quality = "high" # Local variable that only exists inside the constructor
        print(House.quality, self.quality, quality) # low medium high

    def show_house_dets(self):
        print("The house at", self.address, "has an area of", self.area, "and costs", self.price)

# Printing the class variable
print(House.quality) # low

# Printing the object variable
print(house1.quality) # medium

# Trying to print the local variable 
# The local variable only exists within the method and will never be accessible
print(quality) # NameError: name 'quality' is not defined