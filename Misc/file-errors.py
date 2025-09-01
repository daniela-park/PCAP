# Trying to open a non-existent file
try:
    stream = open("non_existent.txt")
    stream.close()
except Exception as e:
    print("An error occured: ", e)
#An error occured:  [Errno 2] No such file or directory: 'non_existent.txt'

# Printing the error number when trying to open a non-existent file
try:
    stream = open("non_existent.txt")
    stream.close()
except Exception as e:
    print(e.errno)
# 2

# Printing the error message when trying to open a non-existent file
from os import strerror
try:
    stream = open("non_existent.txt")
    stream.close()
except Exception as e:
    print(strerror(e.errno))
# No such file or directory