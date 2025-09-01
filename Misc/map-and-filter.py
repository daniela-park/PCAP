# map() applies a function to all elements in the sequence
# It accepts two arguments: a function and a sequence
# It returns an iterator
# When printed, the identifier in the memory is printed
lamb_func = lambda a: a * 2
init_list = [1, 2, 3, 4, 5]
map(lamb_func, init_list)
# <map at 0x2a420d13e80>

# To print the value, instead of the memory identifier, use next()
map_result = map(lamb_func, init_list)
next(map_result) # 2

# next() can be used in a sequence, but it's not very efficient
map_result = map(lamb_func, init_list)
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result)) 
# It returns a StopIteration error, as there are only 5 elements in ini_list
# 2 4 6 8 10

# Using a for loop instead
map_result = map(lamb_func, init_list)
for element in init_list:
    print(next(map_result))
# 2 4 6 8 10

# Another way of using a for loop
map_result = map(lamb_func, init_list)
for element in map_result:
    print(element) 
# 2 4 6 8 10

# Another way of using map, returning a list
map_result = map(lamb_func, init_list)
print(list(map_result))
# [2, 4, 6, 8 10]

# Single line code
print(list(map(lambda a: a * 2, [1, 2, 3, 4, 5])))
# [2, 4, 6, 8 10]

# filter() is very similart to map()
# It accepts two parameters: function and sequence
# The difference between them is that filter() keeps the elements that satisfies the condition
print(list(filter(lambda a: a % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# [2, 4, 6, 8 10]

# Using filter() to remove fake email addresses (which doesn't have @)
emails = [
    "abc@email.com",
    "123",
    "xyz@e.co.uk"
]
list(filter(lambda x: '@' in x, emails))
# ['abc@email.com', 'xyz@e.co.uk']
