import sys

def getFileLocation(arg):
    try:
        return sys.argv[arg]
    except IndexError: #if no file location is given
        print('No file location given.  Example: /home/user/yato.json')
        sys.exit()

def getTask(arg):
    try:
        return sys.argv[arg]
    except IndexError: #if no task is given
        print('No task given.')
        sys.exit()

def getCmd():
    try:
        return sys.argv[1]
    except:
        print('No command given, use -h or --help for help.')
        sys.exit()

def validDate(date):
    if date[0] > '31' or date[0] < '01':
        return False
    elif date[1] > '12' or date[1] < '01':
        return False
    elif date[2] > '9999' or date[2] < '0001':
        return False
    return True

def getDate(arg):
    try:
        date = sys.argv[arg].split('/')
        if validDate(date):
            return date
        else:
            print('Invalid date.  Example: 01/01/2020')
            sys.exit()
    except:
        print('No date given.')
        sys.exit()