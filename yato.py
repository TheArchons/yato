import sys

def help():
    helpFile = open('help.txt', 'r')
    print(helpFile.read())
    helpFile.close()

def new(fileLocation):
    print('File created at: ' + fileLocation)
    
def addToList(list, add):
    file = open(list, 'a')
    file.write(add + '\n')
    print(f'Task {sys.argv[3]} added.')
    file.close()

def listTasks(fileLocation):
    file = open(fileLocation, 'r')
    print(file.read())
    file.close()

def main():
    print(sys.argv[1])
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
            except:
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