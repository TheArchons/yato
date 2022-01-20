from termcolor import colored
from JSONManip import *
import sys
import os
import json

def help():
    helpFile = open('help.txt', 'r')
    print(helpFile.read())
    helpFile.close()

def new(fileLocation):
    json.dump({"todos" : 0, "tasks" : []}, open(fileLocation, 'w'))
    listListAdd(fileLocation.split('/')[-1])
    print('File created at: ' + fileLocation)

def addToList(list, add):
    changeTODOCount(list, True)
    file = getFile(list)
    #print('loaded json') #debug
    file[add] = {'complete' : False, 'index' : file['todos']}
    file["tasks"].append((add, file['todos']))
    json.dump(file, open(list, 'w'))
    print(f'Task {add} added.')

def listTasks(fileLocation):
    file = getFile(fileLocation)
    for pos, task in enumerate(file['tasks']):
        task[1] = pos+1
        if file[task[0]]["complete"]:
            print(colored(str(task[1]) + '. ' + task[0], 'green')) #print completed tasks green
        else:
            print(colored(str(task[1]) + '. ' + task[0], 'red')) #print uncompleted tasks red

def completeTask(list, task):
    file = getFile(list)
    try:
        file[task]['complete'] = not file[task]['complete']
    except KeyError:
        print(f'Task {task} not found.')
    json.dump(file, open(list, 'w'))

def removeTask(list, task):
    try:
        #remove task from tasks list
        delTasksTask(list, task)
        #delete task from list
        delTask(list, task)
        #update todos
        changeTODOCount(list, False)
    except KeyError:
        print(f'Task {task} not found.')

def listAllLists():
    file = getFile('lists.json')
    for list in file['lists']:
        print(list)

def createListList(): #create lists.txt if it doesnt exist
    if not os.path.exists('lists.json'):
        json.dump({"lists" : []}, open('lists.json', 'w'))

def removeList(listPos): #removes a TODO list
    file = getFile('lists.json')
    try:
        file['lists'].remove(listPos)
        os.remove(listPos)
        json.dump(file, open('lists.json', 'w'))
        print(f'List {listPos} removed.')
    except ValueError:
        print(f'List {listPos} not found.')

def addDate(list, task, date):
    file = getFile(list)
    try:
        file[task]['date'] = [int(date[0]), int(date[1]), int(date[2])]
        json.dump(file, open(list, 'w'))
        date = '-'.join(date)
        print(f'Task {task} due at {date}.')
    except KeyError:
        print(f'Task {task} not found.')

"""def insertTask(list, task, find):
    file = open(list, 'r')`
    lines = file.readlines()
    for line in reversed(lines):
        if line.split(',')[0] == find:
            print(f'Task {task} inserted after {find}.')
            replaceLine(list, line, task + ',' + 'incomplete' + '\n' + line)
            file.close()
            return
    print(f'Task {find} not found.')
    file.close()"""
