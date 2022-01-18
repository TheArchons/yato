def replaceLine(fileName, oldText, text):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    with open(fileName, 'w') as file:
        for line in lines:
            if oldText in line:
                line = line.replace(oldText, text)
            file.write(line)

def changeTODOCount(fileName, add):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    with open(fileName, 'w') as file:
        for line in lines:
            if str(line).strip('\n').isdigit():
                if add:
                    line = str(int(line) + 1) + '\n'
                else:
                    line = str(int(line) - 1) + '\n'
            file.write(line)

#TEST
#replaceLine('test.txt', 'old', 'new')