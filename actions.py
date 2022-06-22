from termcolor import colored
from JSONManip import *
import sys
import os
import json
import configparser

def warningDataLoss():
    print(colored('WARNING: Data will be lost.  Continue? (y/n)', 'red'))
    if input().lower() == 'y':
        return True
    else:
        return False

def help():
    print("yato - yet another TODO list\n\
    -h or --help:       show this help\n\
    -n or --new:        create a new TODO list\n\
    -a or --add:        add a task to a TODO list\n\
    -c or --complete:   complete a task\n\
    -r or --remove:     remove a task\n\
    -l or --list:       list all tasks\n\
    -ll or --list-all:  list all TODO lists\n\
    -d or --delete:     delete a TODO list\n\
    -da or --date:      add a date to a task\n\
    -e or --edit:       edit a TODO list's name\n\
    -i or --insert:     insert a task into a TODO list\n\
    -cll or --change-list-list: change the location of the list of lists file\n")

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

def createListList(): #create lists.txt if it doesn't exist
    if not os.path.exists('lists.json'):
        json.dump({"lists" : []}, open('lists.json', 'w'))

def removeList(listPos): #removes a TODO list
    if not warningDataLoss():
        return
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

def ListNameEdit(list, newName):
    os.rename(list, newName)
    file = getFile('lists.json')
    try:
        file['lists'].remove(list)
    except:
        pass
    file['lists'].append(newName)
    json.dump(file, open('lists.json', 'w'))

def insert(list, task, pos):
    file = getFile(list)
    #find highest index
    highest = 0
    for listTask in file['tasks']:
        if listTask[1] > highest:
            highest = listTask[1]
    if pos > highest+1:
        return print('Position too high.')
    #move up tasks in list that are greater or equal to pos
    firstPos = -1
    for fileTask in file['tasks']:
        if fileTask[1] >= pos:
            if firstPos == -1:
                firstPos = fileTask[1]
            fileTask[1] += 1
    #insert task into list
    if firstPos == -1:
        file['tasks'].insert(len(file['tasks'])+1, [task, pos])
    else:
        file['tasks'].insert(firstPos-1, [task, pos])
    file[task] = {'complete' : False, 'index' : pos}
    json.dump(file, open(list, 'w'))

def changeListListPath(newPath):
    # open config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    # change path
    oldPath = config['paths']['lists']
    config['paths']['lists'] = newPath

    # write config.ini
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    
    # move file
    os.renames(oldPath, newPath)

def createConfig():
    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as config:
            config.write('[paths]\n')
            config.write("lists = lists.json \n")