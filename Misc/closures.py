# An example of enclosure
# Enclosure = A function inside another function, which remembers the values of the outer function
def greet(text):

    # This is a closure
    def print_greet(): # This is a nested function, it has access to the outer function variables
        print(text)

    return print_greet

say_hello = greet("Hello")

# This is a free variable
say_hello() # Invoking the closure, it prints "Hello" as it saves the outer function variable
# Free variable = Variables that should already be destroyed, but are still available in a closure

# Another closure example
# A function named make_multiply_closure that accepts a parammeter x
def make_multiply_closure(x):

    # A closure function that accepts a parameter y
    def multiply(y):
        return x * y

    return multiply

# 2 variables are created
multiply_5 = make_multiply_closure(5)   # It invokes the outer function with an argument of 5
multiply_10 = make_multiply_closure(10) # It invokes the outer function with an argument of 10
# The 2 variables above contain the same closure with 2 different values for x: 5 and 10

print(multiply_5(10))
print(multiply_5(20))

print(multiply_10(10))
print(multiply_10(20))
# 50 100 100 200