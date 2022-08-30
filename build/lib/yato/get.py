"""Get the command line argument."""

import sys
import datetime
from yato.JSONManip import prevList, defaultList, setPrevList


def getFileLocation(arg):
    """Get the file location from the command line."""

    try:
        return sys.argv[arg]
    except IndexError:  # if no file location is given
        print('No file location given.  Example: /home/user/yato.json')
        sys.exit()


def getTask(arg):
    """Get the task from the command line."""

    try:
        return sys.argv[arg]
    except IndexError:  # if no task is given
        print('No task given.')
        sys.exit()


def getNewName(arg):
    """Get the new name from the command line."""

    try:
        return sys.argv[arg]
    except IndexError:  # if no new name is given
        print('No new name given.')
        sys.exit()


def getCmd():
    """Get the command line argument at index 1."""

    try:
        return sys.argv[1]
    except IndexError:
        print('No command given, use -h or --help for help.')
        sys.exit()


def validDate(date):
    """Check if a date is valid."""

    try:
        datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        return True
    except ValueError:
        return False


def getDate(arg):
    """Get the date from the command line."""

    try:
        date = sys.argv[arg].split('/')
        if validDate(date):
            return date
        else:
            print('Invalid date.  Example: 01/01/2020')
            sys.exit()
    except IndexError:  # if no date is given
        print('No date given.')
        sys.exit()


def getuInt(arg):
    """Get an unsigned integer from the command line."""

    try:
        integer = int(sys.argv[arg])
        if integer > 0:
            return integer
        else:
            print('Invalid integer, must be positive.')
            sys.exit()
    except ValueError:
        print('Invalid, please enter a number.')
        sys.exit()


def getList(arg):
    """Get the list from the command line."""

    try:
        if sys.argv[arg] == '-p':
            # if they specified previous list, get the previous list
            return prevList()

        list = sys.argv[arg]

        if sys.argv[arg] == '-d':
            # if they specified the default list, get the default list
            list = defaultList()

        setPrevList(list)

        return list
    except IndexError:  # if no list is given
        print('No list given. Example: todo')
        sys.exit()
