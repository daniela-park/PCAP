# A way of reading a file
# The code is enclosed in try/except argument because issues can occur:
# Non-existent file, inaccessible file, corrupted file, etc
try:
    stream = open("fruits.txt")
    # Code
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Reading a file
try:
    stream = open("fruits.txt")
    print(stream.read())
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Reading a file, specifying the first 10 bytes to be read
try:
    stream = open("fruits.txt")
    print(stream.read(10))
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Reading a file, specifying the first 10 bytes to be read and the following 10
try:
    stream = open("fruits.txt")
    print(stream.read(10))
    print(stream.read(10))
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Reading a file with more bytes than the file contains and the following 1
try:
    stream = open("fruits.txt")
    print(stream.read(100))
    print(stream.read(1))
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Nothing bad happens, Python just returns an empty string

# Reading a file character by character
try:
    stream = open("fruits.txt")
    character = stream.read(1)
    while character != " ":
        print(character, end = "-")
        character = stream.read(1)
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Reading a file character by character
# This can be useful to count the number of characters in a file
try:
    stream = open("fruits.txt")
    counter = 0
    character = stream.read(1)
    while character != " ":
        counter += 1
        print(character, end = "-")
        character = stream.read(1)
    stream.close()
    print("\nNumber of characters: ", counter)
except Exception as e:
    print("An error occured: ", e)

# Reading a file line by line
try:
    stream = open("fruits.txt")
    counter = 0
    line = stream.readline()
    while line != " ":
        counter += 1
        print(line, end = "-")
        line = stream.readline()
    stream.close()
    print("\nNumber of lines: ", counter)
except Exception as e:
    print("An error occured: ", e)

# Reading the whole file and returning them as a list of strings
try:
    stream = open("fruits.txt")
    lines = stream.readlines()
    print("Content of the lines: ", lines)
    print("Number of lines in the file :", len(lines))
    for line in lines:
        print(line, end="")
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Reading the whole file, specifying the max byte and a buffer
# This is useful to avoid reading the whole file at once and crashing the program
try:
    stream = open("fruits.txt")
    lines = stream.readlines(2)
    while len(lines) != 0:
        for line in lines:
            print(line, sep=" ")
        lines = stream.readlines(2)
    stream.close()
except Exception as e:
    print("An error occured: ", e)

# Reading the file, using the stream
# If using this method, there is no need to close the stream
try:
    stream = open("fruits.txt")
    for line in stream:
        print(line)
except Exception as e:
    print("An error occured: ", e)

"""
Modes:
r = read file, the file should be readable, otherwise an error will be raised
w = write to a new file or overwrite an existing file
x = write for exclusive creation, which means a file should not exist
a = append to the end of an existing file, without overwriting the contents
b = reads the file as a binary file
t = read the file as a text file
+= open for updating, both reading and writing
"""

