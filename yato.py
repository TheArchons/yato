import sys
from actions import *

def main():
    #DEBUGGING
    print("command: " + sys.argv[1])
    #print(sys.argv[3])
    #END DEBUGGING
    if sys.argv[1] == '-h' or sys.argv[1] == '--help': #help at help.txt
        help()
    elif sys.argv[1] == '-n' or sys.argv[1] == '--new': #New List
        try:
            new(sys.argv[2])
        except IndexError: #if no file location is given
            print('No file location given.  Example: /home/user/yato.txt')
            sys.exit()
        except FileExistsError: #if file already exists
            print('File already exists.')
            sys.exit()
        except PermissionError: #if file location is not writable
            print('Permission denied.')
            sys.exit()
    elif sys.argv[1] == '-a' or sys.argv[1] == '--add': #Add to list
        try:
            fileLocation = sys.argv[2]
            try:
                add = sys.argv[3]
                addToList(fileLocation, add)
            except IndexError:
                print('No task given.')
                sys.exit()
        except FileNotFoundError:
            print('File not found.')
            sys.exit()
        except PermissionError:
            print('Permission denied.')
            sys.exit()
        except IndexError:
            print('No file location given.')
            sys.exit()
    elif sys.argv[1] == '-l' or sys.argv[1] == '--list': #List all tasks
        try:
            listTasks(sys.argv[2])
        except FileNotFoundError:
            print('File not found.')
            sys.exit()
        except PermissionError:
            print('Permission denied.')
            sys.exit()
        except IndexError:
            print('No file location given.')
            sys.exit()

main()