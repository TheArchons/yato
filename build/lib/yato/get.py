import sys
import datetime


def getFileLocation(arg):
    try:
        return sys.argv[arg]
    except IndexError:  # if no file location is given
        print('No file location given.  Example: /home/user/yato.json')
        sys.exit()


def getTask(arg):
    try:
        return sys.argv[arg]
    except IndexError:  # if no task is given
        print('No task given.')
        sys.exit()


def getNewName(arg):
    try:
        return sys.argv[arg]
    except IndexError:  # if no new name is given
        print('No new name given.')
        sys.exit()


def getCmd():
    try:
        return sys.argv[1]
    except IndexError:
        print('No command given, use -h or --help for help.')
        sys.exit()


def validDate(date):
    try:
        datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        return True
    except ValueError:
        return False


def getDate(arg):
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
