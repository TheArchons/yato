import json
import sys


def getFile(filePos):
    try:
        return json.load(open(filePos))
    except FileNotFoundError:
        print('File not found.')
        sys.exit()
    except PermissionError:
        print('Permission denied.')
        sys.exit()


def changeTODOCount(fileName, add):
    file = getFile(fileName)
    if add:
        file['todos'] += 1
    else:
        file['todos'] -= 1
    json.dump(file, open(fileName, 'w'))
    return


def listListAdd(add):
    file = getFile('lists.json')
    file['lists'].append(add)
    json.dump(file, open('lists.json', 'w'))


def delTask(fileName, task):
    file = getFile(fileName)
    del file[task]
    json.dump(file, open(fileName, 'w'))


def delTasksTask(listLoc, task):
    file = getFile(listLoc)
    for lTask in file['tasks']:
        if lTask[0] == task:
            file['tasks'].remove(lTask)
            break
    json.dump(file, open(listLoc, 'w'))
