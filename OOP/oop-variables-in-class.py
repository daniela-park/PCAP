# Class Dog with a class variable inside
class Dog():
    counter = 0 # Counts how many instances of the object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1

# Creating objects
dog1 = Dog("A", 1)
dog2 = Dog("B", 2)
dog3 = Dog("C", 3)

# Printing the counter for each object created
print(dog1.counter) # 3
print(dog2.counter) # 3
print(dog3.counter) # 3

# Printing the object's dictionary
dog1.__dict__ # {'name': 'A', 'age': 1}
# Counter is not printed because it's a class variable, not instance variable

# Printing the class variable
print(Dog.counter) # 3

# Class Dog with a private class variable
class Dog():
    __counter = 0 # Counts how many instances of the object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.__counter += 1

# Accessing the private class variable through mangling
print(Dog._Dog__counter) # 0

# Printing the class dictionary
Dog.__dict__

# Checking if an object has a specified attribute
class Dog():
    __counter = 0 # Counts how many instances of the object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.__counter += 1

dog1 = Dog("A", 1)

if hasattr(dog1, "name"):
    print("The dog is called", dog1.name)
else:
    print("The dog has no name.")
# The dog is called A

# Checking if a private attribute (__name) can be accessed
class Dog():
    __counter = 0 # Counts how many instances of the object is created
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.__counter += 1

dog1 = Dog("A", 1)

if hasattr(dog1, "name"):
    print("The dog is called", dog1.name)
else:
    print("The dog has no name.")
# The dog has no name.

# Checking if a private attribute (__name) can be accessed through mangling
class Dog():
    __counter = 0 # Counts how many instances of the object is created
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.__counter += 1

dog1 = Dog("A", 1)

if hasattr(dog1, "name"):
    print("The dog is called", dog1._Dog__name)
else:
    print("The dog has no name.")
# The dog has no name.

# Accessing a class variable
class Dog():
    counter = 0 ## Counts how many instances of the object is created
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.counter += 1

dog1 = Dog("A", 1)

if hasattr(Dog, "counter"):
    print("There are", Dog.counter, "dogs.")
else:
    print("There are no dogs.")
# There are 1 dogs.

# Creating an object and printing the object type
dog1 = Dog("A", 1)
type(dog1).__name__ # 'Dog'

# Creating an object and printing the object module
dog1 = Dog("A", 1)
dog1.__module__ # '__main__'

# Creating an object and printing the class module
dog1 = Dog("A", 1)
Dog.__module__ # '__main__'