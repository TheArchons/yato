import sys

if sys.argv[1] == '-h' or sys.argv[1] == '--help': #help at help.txt
    helpFile = open('help.txt', 'r')
    print(helpFile.read())
    helpFile.close()
    sys.exit()
elif sys.argv[1] == '-n' or sys.argv[1] == '--new': #New List
    try:
        fileLocation = sys.argv[2]
        open(fileLocation, 'x')
        print('File created at: ' + fileLocation)
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
        file = open(fileLocation, 'a')
        try:
            file.write(sys.argv[3] + '\n')
        except IndexError: #if no task is given
            print('No task given.')
            sys.exit()
        print(f'Task {sys.argv[3]} added.')
        file.close()
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
        fileLocation = sys.argv[2]
        file = open(fileLocation, 'r')
        print(file.read())
        file.close()
    except FileNotFoundError:
        print('File not found.')
        sys.exit()
    except PermissionError:
        print('Permission denied.')
        sys.exit()
    except IndexError:
        print('No file location given.')
        sys.exit()