from termcolor import colored
import fileinput
from replace import *
import sys
import os

def help():
    helpFile = open('help.txt', 'r')
    print(helpFile.read())
    helpFile.close()

def new(fileLocation):
    try:
        file = open(fileLocation, 'x')
        #number of todos
        file.write('0' + '\n')
        file.close()
    except FileExistsError:
        print('File already exists.')
        sys.exit()
    except PermissionError:
        print('Permission denied.')
        sys.exit()
    file = open('lists.txt', 'a')
    file.write(fileLocation + '\n')
    file.close()
    print('File created at: ' + fileLocation)
    
def addToList(list, add):
    file = open(list, 'a')
    file.write(add + ',incomplete' + '\n')
    changeTODOCount(list, True)
    print(f'Task {add} added.')
    file.close()

def listTasks(fileLocation):
    file = open(fileLocation, 'r')
    lines = file.readlines()
    for line in reversed(lines):
        #ignore tagless
        if len(line.split(',')) == 1:
            continue
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
            #subtract one from task count
            changeTODOCount(list, False)
            file.close()
            return
    print(f'Task {task} not found.')
    file.close()
    
def listAllLists():
    file = open('lists.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line.split('\n')[0])
    file.close()

def createListList(): #create lists.txt if it doesnt exist
    if not os.path.exists('lists.txt'):
        file = open('lists.txt', 'x')
        file.close()

def insertTask(list, task, find):
    file = open(list, 'r')
    lines = file.readlines()
    for line in reversed(lines):
        if line.split(',')[0] == find:
            print(f'Task {task} inserted after {find}.')
            replaceLine(list, line, task + ',' + 'incomplete' + '\n' + line)
            file.close()
            return
    print(f'Task {find} not found.')
    file.close()
