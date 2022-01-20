from actions import *
from get import *
import os

def main():
    createListList() #create lists.txt if it doesnt exist
    if getCmd() == '-h' or getCmd() == '--help': #help at help.txt
        help()
        
    elif getCmd() == '-n' or getCmd() == '--new': #New List
        new(getFileLocation(2)) #getFileLocation(2) is the file location

    elif getCmd() == '-a' or getCmd() == '--add': #Add to list
        addToList(getFileLocation(2), getTask(3))

    elif getCmd() == '-l' or getCmd() == '--list': #List all tasks
        listTasks(getFileLocation(2))

    elif getCmd() == '-c' or getCmd() == '--complete': #Complete task
        completeTask(getFileLocation(2), getTask(3))
        
    elif getCmd() == '-r' or getCmd() == '--remove': #Remove task
        removeTask(getFileLocation(2), getTask(3))

    elif getCmd() == '-ll' or getCmd() == '--list-all':#lists all lists
        listAllLists()

    elif getCmd() == '-d' or getCmd() == '--delete': #Delete list
        removeList(getFileLocation(2))
    """elif getCmd() == '-i' or getCmd() == '--insert': #Insert task
        insertTask(getFileLocation(2), getTask(3), getTask(4))""" #deprecated
main()