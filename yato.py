from actions import *
from get import *
import os

def main():
    createListList() # create lists.txt if it doesn't exist
    createConfig() # create config.txt if it doesn't exist
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
        
    elif getCmd() == '-da' or getCmd() == '--date': #Add date to task
        addDate(getFileLocation(2), getTask(3), getDate(4))
    
    elif getCmd() == '-e' or getCmd() == '--edit': #Edit list name
        ListNameEdit(getFileLocation(2), getNewName(3))

    elif getCmd() == '-i' or getCmd() == '--insert': #Insert task
        insert(getFileLocation(2), getTask(3), getuInt(4))
    
    elif getCmd() == '-cll' or getCmd() == '--change-list-list':
        changeListListPath(getFileLocation(2))
    
main()