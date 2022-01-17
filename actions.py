from termcolor import colored
import fileinput
from replace import replaceLine

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
        if line.split(',')[1] == 'complete\n':
            print(colored(line.split(',')[0], 'green')) #print as green if completed
        else:
            print(colored(line.split(',')[0], 'red')) #print as red if incomplete
    file.close()

def completeTask(list, task):
    task = task.split()[0]
    file = open(list, 'r')
    lines = file.readlines()
    for line in reversed(lines):
        if line.split(',')[0] == task:
            if line.split(',')[1] == 'complete\n':
                complete = 'incomplete'
            else:
                complete = 'complete'
            print(complete)
            replaceLine(list, line, line.replace(line, task + ',' + complete + '\n'))
            print(f'Task {task} marked as {complete}.')
            file.close()
            return
    print(f'Task {task} not found.')
    file.close()

def removeTask(list, task):
    task = task.split()[0]
    file = open(list, 'r')
    lines = file.readlines()
    for line in reversed(lines):
        if line.split(',')[0] == task:
            print(f'Task {task} removed.')
            replaceLine(list, line, '')
            file.close()
            return