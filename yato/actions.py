from termcolor import colored
from JSONManip import getFile, delTask, delTasksTask, \
     changeTODOCount, listListAdd
import os
import json
import configparser
from shutil import copyfile


def checkTaskExists(list, task):
    """"Checks if a task exists in a TODO list"""
    file = getFile(list)
    if task in file:
        return True
    return False


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
    -cll or --change-list-list: change the location of the list of lists\n\
    -cl or --change-list:     change the location of a TODO list\n")


def new(fileLocation):
    json.dump({"todos": 0, "tasks": []}, open(fileLocation, 'w'))
    listListAdd(fileLocation.split('/')[-1])
    print('File created at: ' + fileLocation)


def addToList(list, add):
    if checkTaskExists(list, add):
        print(f'Task {add} already exists.')
        return
    changeTODOCount(list, True)
    file = getFile(list)
    file[add] = {'complete': False, 'index': file['todos']}
    file["tasks"].append((add, file['todos']))
    json.dump(file, open(list, 'w'))
    print(f'Task {add} added.')


def listTasks(fileLocation):
    file = getFile(fileLocation)
    for pos, task in enumerate(file['tasks']):
        task[1] = pos+1
        if file[task[0]]["complete"]:
            # print completed tasks green
            print(colored(str(task[1]) + '. ' + task[0], 'green'))
        else:
            # print uncompleted tasks red
            print(colored(str(task[1]) + '. ' + task[0], 'red'))


def completeTask(list, task):
    file = getFile(list)
    try:
        file[task]['complete'] = not file[task]['complete']
    except KeyError:
        print(f'Task {task} not found.')
    json.dump(file, open(list, 'w'))


def removeTask(list, task):
    try:
        # remove task from tasks list
        delTasksTask(list, task)
        # delete task from list
        delTask(list, task)
        # update todos
        changeTODOCount(list, False)
    except KeyError:
        print(f'Task {task} not found.')


def listAllLists():
    file = getFile('lists.json')
    for list in file['lists']:
        print(list)


def createListList():  # create lists.txt if it doesn't exist
    # open config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    # create lists.txt if it doesn't exist
    if not os.path.exists(config['paths']['lists']):
        json.dump({"lists": []}, open('lists.json', 'w'))


def removeList(listPos):  # removes a TODO list
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
    except ValueError:
        pass
    file['lists'].append(newName)
    json.dump(file, open('lists.json', 'w'))


def insert(list, task, pos):
    file = getFile(list)
    # find highest index
    highest = 0
    for listTask in file['tasks']:
        if listTask[1] > highest:
            highest = listTask[1]
    if pos > highest+1:
        return print('Position too high.')
    # move up tasks in list that are greater or equal to pos
    firstPos = -1
    for fileTask in file['tasks']:
        if fileTask[1] >= pos:
            if firstPos == -1:
                firstPos = fileTask[1]
            fileTask[1] += 1
    # insert task into list
    if firstPos == -1:
        file['tasks'].insert(len(file['tasks'])+1, [task, pos])
    else:
        file['tasks'].insert(firstPos-1, [task, pos])
    file[task] = {'complete': False, 'index': pos}
    json.dump(file, open(list, 'w'))


def changeListListPath(newPath):
    # open config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    # change path
    oldPath = config['paths']['lists']
    config['paths']['lists'] = newPath

    # write config.ini
    with open('config.ini', 'w') as configFile:
        config.write(configFile)

    # move file
    os.renames(oldPath, newPath)

    print('List list file location changed.')


def createConfig():
    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as config:
            config.write('[paths]\n')
            config.write("lists = lists.json \n")


def changeListPath(oldPath, newPath):
    # update lists.json
    file = getFile('lists.json')
    try:
        file['lists'].remove(oldPath)
    except ValueError:
        print(f'List {oldPath} not found, please check the path.')
        return

    file['lists'].append(newPath)
    json.dump(file, open('lists.json', 'w'))

    # move file
    os.renames(oldPath, newPath)

    print(f'List {oldPath} moved to {newPath}.')


def backup(original, backup):
    """Backup a list to a new location."""
    if os.path.exists(original):
        try:
            copyfile(original, backup)
        except FileNotFoundError:
            print(f'File {original} not found.')
        print(f'List {original} backed up to {backup}.')
    else:
        print(f'List {original} not found.')


def restoreBackup(backup, original):
    """Restore a list from a backup."""
    if os.path.exists(backup):
        try:
            copyfile(backup, original)
        except FileNotFoundError:
            print(f'File {backup} not found.')
        print(f'List {backup} restored to {original}.')
    else:
        print(f'List {backup} not found.')
