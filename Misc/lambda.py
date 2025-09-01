# Traditional way of creating a function
def functionName(parameter1, parameter2):
    # Instruction1
    # Instruction2
    pass

# Lamdba function
lambda parameter1, parameter2: #Instruction

# Traditional function
def sum(a, b):
    return a + b

# Lambda function
lambda a, b : a + b
# <function __main__.<lambda>(a, b)>

# Calling a function and passing the parameters
sum(10, 5)
# 15

# Storing the lambda function in a variable, since it doesn't have a name
lambsum = lambda a, b : a + b

# Calling the variable which stores the lambda function and passing arguments
lambsum(5, 10)
# 15

# Lambda functions can be useful as can be passed as paramters
def apply_func(elements, func):
    for element in elements:
        print(func(element))

# Example
func_name = lambda x: x * x
apply_func([1, 2, 3, 4, 5], func_name)
# 1 4 9 16 25

# Another example
func_name = lambda x: 1/x
apply_func([1, 2, 3, 4, 5], func_name)
# 1.0 0.5 0.333 0.25 0.2

# The lambda function doesn't even need to be stored in a variable
apply_func([1, 2, 3, 4, 5], lambda x: x * x)
# 1 4 9 16 25