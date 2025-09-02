# Creating a class with some methods, including a private method
class Doctor():
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
        self.__format_names()

    def __format_names(self):
        self.fname = self.fname.title()
        self.lname = self.lname.title()

    def introduce(self):
        print("The first name is", self.fname)

    def compare_name(self, name_to_compare):
        if self.fname == name_to_compare:
            print("They have the same name!")
        else:
            print("The name is different")

    def get_first_last_name_together():
        return self.fname + " " + self.lname

# Creating an object
doc1 = Doctor("A", "B")
# Calling the methods
doc1.introduce() # The first name is A
doc1.compare_name("B") # The name is different
print(doc1.__dict__) # {'fname': 'A', 'lname': 'B'}
print(Doctor.__dict__)

# Printing the object will print the memory location
print(doc1) # <__main__.Doctor object at 0x00000218BB8D9E80>

# Printing the class will print the type of data
print(Doctor) # <class '__main__.Doctor'>

# Adding method __str__(self) to print the data contained in the memory location for the object
class Doctor():
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
        self.__format_names()

    def __format_names(self):
        self.fname = self.fname.title()
        self.lname = self.lname.title()

    def introduce(self):
        print("The first name is", self.fname)

    def compare_name(self, name_to_compare):
        if self.fname == name_to_compare:
            print("They have the same name!")
        else:
            print("The name is different")

    def get_first_last_name_together():
        return self.fname + " " + self.lname

    # Method
    def __str__(self):
        return "Doctor: " + self.fname + " " + self.lname
        
# Printing the object
print(doc1) # Doctor: A B

# Printing the class
print(Doctor) # <class '__main__.Doctor'>