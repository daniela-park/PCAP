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