import sys

def getFile(arg):
    try:
        return sys.argv[arg]
    except IndexError: #if no file location is given
        print('No file location given.  Example: /home/user/yato.txt')
        sys.exit()
    except FileExistsError: #if file already exists
        print('File already exists.')
        sys.exit()
    except PermissionError: #if file location is not writable
        print('Permission denied.')
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