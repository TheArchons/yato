import actions
from get import getCmd, getFileLocation, getTask, getNewName, getDate, getuInt


def main():
    actions.createConfig()  # create config.ini if it doesn't exist
    actions.createListList()  # create lists.txt if it doesn't exist

    if getCmd() == '-n' or getCmd() == '--new':  # New List
        actions.new(getFileLocation(2))

    elif getCmd() == '-a' or getCmd() == '--add':  # Add to list
        actions.addToList(getFileLocation(2), getTask(3))

    elif getCmd() == '-l' or getCmd() == '--list':  # List all tasks
        actions.listTasks(getFileLocation(2))

    elif getCmd() == '-c' or getCmd() == '--complete':  # Complete task
        actions.completeTask(getFileLocation(2), getTask(3))

    elif getCmd() == '-r' or getCmd() == '--remove':  # Remove task
        actions.removeTask(getFileLocation(2), getTask(3))

    elif getCmd() == '-ll' or getCmd() == '--list-all':  # lists all lists
        actions.listAllLists()

    elif getCmd() == '-d' or getCmd() == '--delete':  # Delete list
        actions.removeList(getFileLocation(2))

    elif getCmd() == '-da' or getCmd() == '--date':  # Add date to task
        actions.addDate(getFileLocation(2), getTask(3), getDate(4))

    elif getCmd() == '-e' or getCmd() == '--edit':  # Edit list name
        actions.ListNameEdit(getFileLocation(2), getNewName(3))

    elif getCmd() == '-i' or getCmd() == '--insert':  # Insert task
        actions.insert(getFileLocation(2), getTask(3), getuInt(4))

    elif getCmd() == '-cll' or getCmd() == '--change-list-list':
        actions.changeListListPath(getFileLocation(2))

    elif getCmd() == '-cl' or getCmd() == '--change-list':
        actions.changeListPath(getFileLocation(2), getFileLocation(3))

    elif getCmd() == '-b' or getCmd() == '--backup':
        actions.backup(getFileLocation(2), getFileLocation(3))

    elif getCmd() == '-rb' or getCmd() == '--restore-backup':
        actions.restoreBackup(getFileLocation(2), getFileLocation(3))

    else:
        help()


main()
