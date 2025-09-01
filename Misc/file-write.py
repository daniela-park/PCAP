# Writing to a new file
try:
    stream = open("newFile.txt", "w") # A new file is created
    # Modes: r (read), w (write)
    stream.write("Message 1\n")
    stream.write("Message 2\n")
    stream.write("Message 3\n")
    stream.close()
except Exception as e:
    print("An error occurred: ", e)

# Writing to an existing file will overwrite the previous content
try:
    stream = open("newFile.txt", "w") # A new file is created
    # Modes: r (read), w (write)
    stream.write("New message 1\n")
    stream.close()
except Exception as e:
    print("An error occurred: ", e)