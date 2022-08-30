"""Manipulates JSON Files in the directory."""

import json
import sys
from configparser import ConfigParser


def getFile(filePos):
    """Get the file and return it as a dictionary."""
    try:
        return json.load(open(filePos))
    except FileNotFoundError:
        print('File not found.')
        sys.exit()
    except PermissionError:
        print('Permission denied.')
        sys.exit()


def changeTODOCount(fileName, add):
    """Increment/decrement the TODO count.

    If add is True, increment the count.  If add is False, decrement the count.

    Args:
        fileName (str): The file name.
        add (bool): True if incrementing, False if decrementing.

    Returns:
        None"""
    file = getFile(fileName)
    if add:
        file['todos'] += 1
    else:
        file['todos'] -= 1
    json.dump(file, open(fileName, 'w'))
    return


def listListAdd(add):
    """Add a list to the list of lists."""
    file = getFile('lists.json')
    file['lists'].append(add)
    json.dump(file, open('lists.json', 'w'))
    return


def delTask(fileName, task):
    """Delete a task from the list."""
    file = getFile(fileName)
    del file[task]
    json.dump(file, open(fileName, 'w'))
    return


def delTasksTask(listLoc, task):
    """Delete a task from the tasks list."""
    file = getFile(listLoc)
    for lTask in file['tasks']:
        if lTask[0] == task:
            file['tasks'].remove(lTask)
            break
    json.dump(file, open(listLoc, 'w'))
    return


def prevList():
    file = getFile('lists.json')
    if file['prev'] != '':
        return file['prev']
    else:
        print('No previous list.')
        sys.exit()


def setPrevList(list):
    file = getFile('lists.json')
    file['prev'] = list
    json.dump(file, open('lists.json', 'w'))
    return


def defaultList():
    file = getFile('lists.json')
    if file['default'] != '':
        return file['default']
    else:
        print('No default list. Add a default list with the command -sd or --set-default.')
        sys.exit()


def getListList():
    config = ConfigParser()
    config.read('config.ini')

    return getFile(config['paths']['lists'])


def getListListPath():
    config = ConfigParser()
    config.read('config.ini')

    return config['paths']['lists']
