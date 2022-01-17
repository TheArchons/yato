from actions import *
from get import *

def main():
    if getCmd() == '-h' or getCmd() == '--help': #help at help.txt
        help()
    elif getCmd() == '-n' or getCmd() == '--new': #New List
        new(getFile(2)) #getFile(2) is the file location
    elif getCmd() == '-a' or getCmd() == '--add': #Add to list
        fileLocation = getFile(2)
        addToList(fileLocation, getTask(3))
    elif getCmd() == '-l' or getCmd() == '--list': #List all tasks
        listTasks(getFile(2))

main()