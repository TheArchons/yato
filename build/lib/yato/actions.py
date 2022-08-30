"""Perform various actions on TODO lists"""

from termcolor import colored
import yato.JSONManip as JSONManip
import os
import json
import configparser
from shutil import copyfile


def main():
    return


def checkTaskExists(list, task):
    """"Check if a task exists in a TODO list"""

    file = JSONManip.getFile(list)
    if task in file:
        return True
    return False


def warningDataLoss():
    """Warn user about data loss"""

    print(colored('WARNING: Data will be lost.  Continue? (y/n)', 'red'), end='')
    if input().lower() == 'y':
        return True
    else:
        return False


def help():
    """Print help message"""

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
    -cl or --change-list:     change the location of a TODO list\n\
    -b or --backup:     backup a TODO list\n\
    -rb or --restore:   restore a TODO list\n\
    -sd or --set-default: set the default TODO list\n\
    \n\
    To specify the previous TODO list, replace the list location with -p\n\
    To specify the default TODO list, replace the list location with -d\n")


def new(fileLocation):
    """create a new TODO list at fileLocation"""

    json.dump({"todos": 0, "tasks": []}, open(fileLocation, 'w'))
    JSONManip.listListAdd(fileLocation.split('/')[-1])
    print('File created at: ' + fileLocation)


def addToList(list, add):
    """add a task to a TODO list

    args:
        list: the TODO list to add the task to
        add: the task to add"""

    if checkTaskExists(list, add):
        print(f'Task {add} already exists.')
        return
    JSONManip.changeTODOCount(list, True)
    file = JSONManip.getFile(list)
    file[add] = {'complete': False, 'index': file['todos']}
    file["tasks"].append((add, file['todos']))
    json.dump(file, open(list, 'w'))
    print(f'Task {add} added.')


def listTasks(fileLocation):
    """list all tasks in a TODO list"""

    file = JSONManip.getFile(fileLocation)
    for pos, task in enumerate(file['tasks']):
        task[1] = pos + 1
        if file[task[0]]["complete"]:
            # print completed tasks green
            print(colored(str(task[1]) + '. ' + task[0], 'green'))
        else:
            # print uncompleted tasks red
            print(colored(str(task[1]) + '. ' + task[0], 'red'))


def completeTask(list, task):
    """mark a task as complete"""

    file = JSONManip.getFile(list)
    try:
        file[task]['complete'] = not file[task]['complete']
    except KeyError:
        print(f'Task {task} not found.')
    json.dump(file, open(list, 'w'))


def removeTask(list, task):
    """remove a task from a TODO list"""

    try:
        # remove task from tasks list
        JSONManip.delTasksTask(list, task)
        # delete task from list
        JSONManip.delTask(list, task)
        # update todos
        JSONManip.changeTODOCount(list, False)
    except KeyError:
        print(f'Task {task} not found.')


def listAllLists():
    """List all TODO lists"""

    file = JSONManip.getListList()

    for list in file['lists']:
        print(list)


def createListList():
    """If the list of lists doesn't exist, create it"""

    # get list
    filePath = JSONManip.getListListPath()

    # create lists.txt if it doesn't exist
    if not os.path.exists(filePath):
        json.dump({"lists": [], 'prev': '', 'default': ''}, open(filePath, 'w'))


def removeList(listPos):
    """Remove a TODO list at listPos"""

    if not warningDataLoss():
        return
    file = JSONManip.getFile('lists.json')
    try:
        file['lists'].remove(listPos)
        try:
            os.remove(listPos)
        except FileNotFoundError:  # if the list doesn't exist, don't worry about it
            pass
        json.dump(file, open('lists.json', 'w'))
        print(f'List {listPos} removed.')
    except ValueError:
        print(f'List {listPos} not found.')


def addDate(list, task, date):
    """Add a date to a task in a TODO list"""

    file = JSONManip.getFile(list)
    try:
        file[task]['date'] = [int(date[0]), int(date[1]), int(date[2])]
        json.dump(file, open(list, 'w'))
        date = '-'.join(date)
        print(f'Task {task} due at {date}.')
    except KeyError:
        print(f'Task {task} not found.')


def ListNameEdit(list, newName):
    """Edit a TODO list's name"""

    os.rename(list, newName)
    file = JSONManip.getFile('lists.json')
    try:
        file['lists'].remove(list)
    except ValueError:
        pass
    file['lists'].append(newName)
    json.dump(file, open('lists.json', 'w'))


def insert(list, task, pos):
    """Insert a task into a TODO list at pos"""

    file = JSONManip.getFile(list)
    # find highest index
    highest = 0
    for listTask in file['tasks']:
        if listTask[1] > highest:
            highest = listTask[1]
    if pos > highest + 1:
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
        file['tasks'].insert(len(file['tasks']) + 1, [task, pos])
    else:
        file['tasks'].insert(firstPos - 1, [task, pos])
    file[task] = {'complete': False, 'index': pos}
    json.dump(file, open(list, 'w'))


def changeListListPath(newPath):
    """Change the location of the list of lists"""

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
    """Create config.ini if it doesn't exist"""

    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as config:
            config.write('[paths]\n')
            config.write("lists = lists.json \n")


def changeListPath(oldPath, newPath):
    """Change the location of a TODO list"""

    # update lists.json
    file = JSONManip.getFile('lists.json')
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


def setDefault(list):
    """Set a list as the default list"""

    file = JSONManip.getListList()

    try:
        file['default'] = list
        json.dump(file, open('lists.json', 'w'))
        print(f'List {list} set as default.')
    except KeyError:
        print(f'List {list} not found.')


def invalidCmd():
    """Print invalid command message"""

    print('Invalid command. Add -h for help.')
