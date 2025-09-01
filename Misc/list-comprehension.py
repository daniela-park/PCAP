# A way of creating a list with numbers from 1 to 100
numbers = []
for i in range(1, 101):
    numbers.append(i)
print("Numbers:", numbers)
# A list with numbers from 1 to 100

# List comprehesion
numbers = [i for i in range(1, 101)]
print("Numbers:", numbers)
# A list with numbers from 1 to 100

# List comprehension accepts more tasks within the line
numbers = [i for i in range(1, 101) if i % 3 != 0]
print("Numbers:", numbers)
# A list with numbers from 1 to 100 not divisible by 3

# List comprehemsion to create a list with 100 numbers, alternating between 0 and 1
numbers = [0 if i % 2 == 0 else 1 for i in range(100)]
# Add 0 if i % 2 == 0, otherwise add 1 in a range of 100
print("Numbers:", numbers)
# A list with 100 numbers, alternating between 0 and 1

# To create a nested list comprehension (for loop inside a for loop)
table = [i for i in range(1, 6)]
print(table)
# [1, 2, 3, 4, 5]

table = [[i for i in range(1, 6)] for j in range(5)]
print(table)
# [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
