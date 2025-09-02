# Creating a class that accepts 2 parameters
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Puppy", 3)

# Creating an object and passing 2 attributes
dog1 = Dog("Puppy", 3)

# Adding a new property, although there are only 2 in the class constructor
dog1.colour = "brown"

# Deleting a property defined in the constructor
del dog1.name 

# Printing the object dictionary
dog1 = Dog("Puppy", 3)
dog1.__dict__ # {'name': 'Puppy', 'age': 3}

# Adding a new property and printing the dict
dog1.colour = "brown"
dog1.__dict__ # {'name': 'Puppy', 'age': 3, 'colour': 'brown'}

# Deleting a property and printing the dict
del dog1.name
dog1.__dict__ # {'age': 3, 'colour': 'brown'}

# Setting a privvate property (__name)
class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.age = age

dog1 = Dog("Puppy", 3)
dog1.__dict__ # {'_Dog__name': 'Puppy', 'age': 3}

# Trying to access the private property outside the class
dog1 = Dog("Puppy", 3)
dog1.__dict__
print(dog1.name) # AttributeError: 'Dog' object has no attribute 'name'

# Accessing the private property outside the class through name mangling
dog1 = Dog("Puppy", 3)
dog1.__dict__
print(dog1._Dog__name) # Puppy

# Modifying the private property outside the class through name mangling
dog1 = Dog("Puppy", 3)
dog1.__dict__
dog1._Dog__name = "Another name"
print(dog1._Dog__name)

