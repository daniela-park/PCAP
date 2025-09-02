# Creating a function that modifies all string properties by turning them into empty strings
def empty_strings(user_object):
    for prop_name in user_object.__dict__.keys():
        prop_value = getattr(user_object, prop_name) # getattr = reflection
        if isinstance(prop_value, str):
            setattr(user_object, prop_name, " ") # setattr = introspection

# An example of reflection/instrospection
class Doctor():
    # Constructor
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
        self.__format_names() # Private method

    # Private method
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

    def __str__(self):
        return "Doctor: " + self.fname + " " + self.lname

# Creating an object
doc1 = Doctor("A", "B")
# Calling the method
doc1.introduce() # The first name is A
empty_strings(doc1) # Calling the function that changes the properties
doc1.introduce() # The first name is 