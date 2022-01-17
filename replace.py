def replaceLine(fileName, oldText, text):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    with open(fileName, 'w') as file:
        for line in lines:
            if oldText in line:
                line = line.replace(oldText, text)
            file.write(line)

#TEST
#replaceLine('test.txt', 'old', 'new')