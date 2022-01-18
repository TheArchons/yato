from actions import *
from get import *
import os

def main():
    createListList() #create lists.txt if it doesnt exist
    if getCmd() == '-h' or getCmd() == '--help': #help at help.txt
        help()
    elif getCmd() == '-n' or getCmd() == '--new': #New List
        new(getFile(2)) #getFile(2) is the file location
    elif getCmd() == '-a' or getCmd() == '--add': #Add to list
        addToList(getFile(2), getTask(3))
    elif getCmd() == '-l' or getCmd() == '--list': #List all tasks
        listTasks(getFile(2))
    elif getCmd() == '-c' or getCmd() == '--complete': #Complete task
        completeTask(getFile(2), getTask(3))
    elif getCmd() == '-r' or getCmd() == '--remove': #Remove task
        removeTask(getFile(2), getTask(3))
    elif getCmd() == '-ll' or getCmd() == '--list-all':#lists all lists
        listAllLists()
main()