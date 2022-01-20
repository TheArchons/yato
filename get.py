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