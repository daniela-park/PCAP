def count_occurences(file_name, word):
    counter = 0
    stream = open(file_name)
    lines = stream.readlines()
    #print(lines)
    i = 0
    while i < len(lines):
        newList = lines[i].split()
        i += 1

        for w in newList:
            if w == word:
                counter += 1

    stream.close()
    print(counter)
    
    return counter

count_occurences("fruits.txt", "Apple")