from termcolor import colored

def help():
    helpFile = open('help.txt', 'r')
    print(helpFile.read())
    helpFile.close()

def new(fileLocation):
    print('File created at: ' + fileLocation)
    
def addToList(list, add):
    file = open(list, 'a')
    file.write(add + ',incomplete' + '\n')
    print(f'Task {add} added.')
    file.close()

def listTasks(fileLocation):
    file = open(fileLocation, 'r')
    lines = file.readlines()
    for line in reversed(lines):
        if line.split(',')[1] == 'completed\n':
            print(colored(line.split(',')[0], 'green'))
        else:
            print(colored(line.split(',')[0], 'red'))
    file.close()

def completeTask(list, task):
    file = open(list, 'r')
    lines = file.readlines()
    file.close()
    file = open(list, 'w')
    for line in lines:
        if line == task + ',incomplete\n':
            line = task+',completed\n'
            file.write(line)
            file.close()
            print(f'Task {task} completed.')
            return
        elif line == task + ',completed\n':
            line = task+',incomplete\n'
            file.write(line)
            file.close()
            print(f'Task {task} uncompleted.')
            return
    print(f'Task {task} not found.')