# Creating a binary file with 100 bytes all equals to 0
data = bytearray(100)

# Assigning a value to a byte
# The values can range from 0 to 255
data[0] = 100

# Assigning a value greater than 255 will raise an error
data[0] = 300
# ValueError: byte must be in range(0, 256)

# Creating a byte array and writing it into a file
data = bytearray(100)
data[0] = 100
data[1] = 150

try:
    stream = open("file.bin", "wb") # wb = writebinary, so it shouldn't treat the file as a text file
    stream.write(data)
    stream.close()
except Exception as e:
    print("An error occured :", e)

# Reading a binary file
try:
    bf = open("file.bin", "rb") # rb = readbinary, so it shouldn't treat the file as a text file
    byte_array = bf.read()
    stream.close()
except Exception as e:
    print("An error occured :", e)
print(byte_array)

# To read the binary files as hexadecimal
for byte in byte_array:
    print(hex(byte), end=" ")

# To read the binary files as base 10
for byte in byte_array:
    print(int(byte), end=" ")

# Reading a binary file, limiting the number of bytes to read
# by passing an argument in read(), so it doesn't compromise the memory
try:
    bf = open("file.bin", "rb") # rb = readbinary, so it shouldn't treat the file as a text file
    byte_array = bf.read(10)
    stream.close()
except Exception as e:
    print("An error occured :", e)

for byte in byte_array:
    print(int(byte), end=" ")

# Another way to create a bytearray
data = bytearray(10)
try:
    bf = open("file.bin", "rb")
    bf.readinto(data)
    bf.close()
except Exception as e:
    print("An error occured: ", e)