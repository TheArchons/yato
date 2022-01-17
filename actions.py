def help():
    helpFile = open('help.txt', 'r')
    print(helpFile.read())
    helpFile.close()

def new(fileLocation):
    print('File created at: ' + fileLocation)
    
def addToList(list, add):
    file = open(list, 'a')
    file.write(add + '\n')
    print(f'Task {add} added.')
    file.close()

def listTasks(fileLocation):
    file = open(fileLocation, 'r')
    print(file.read())
    file.close()