import sys

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    helpFile = open('help.txt', 'r')
    print(helpFile.read())
    helpFile.close()
    sys.exit()
elif sys.argv[1] == '-n' or sys.argv[1] == '--new':
    try:
        fileLocation = sys.argv[2]
        open(fileLocation, 'x')
        print('File created at: ' + fileLocation)
    except IndexError:
        print('No file location given.  Example: /home/user/TODO.txt')
        sys.exit()
    except FileExistsError:
        print('File already exists.')
        sys.exit()
    except PermissionError:
        print('Permission denied.')
        sys.exit()