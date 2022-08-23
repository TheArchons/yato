"""run functions based on command line arguments"""

import yato.actions as actions
import yato.get as get


def main():
    """Main function"""

    actions.createConfig()  # create config.ini if it doesn't exist
    actions.createListList()  # create lists.json if it doesn't exist

    # get command
    cmd = get.getCmd()

    if cmd == '-h' or cmd == '--help':  # help at help.txt
        actions.help()

    elif cmd == '-n' or cmd == '--new':  # New List
        actions.new(get.getFileLocation(2))

    elif cmd == '-a' or cmd == '--add':  # Add to list
        actions.addToList(get.getFileLocation(2), get.getTask(3))

    elif cmd == '-l' or cmd == '--list':  # List all tasks
        actions.listTasks(get.getFileLocation(2))

    elif cmd == '-c' or cmd == '--complete':  # Complete task
        actions.completeTask(get.getFileLocation(2), get.getTask(3))

    elif cmd == '-r' or cmd == '--remove':  # Remove task
        actions.removeTask(get.getFileLocation(2), get.getTask(3))

    elif cmd == '-ll' or cmd == '--list-all':  # lists all lists
        actions.listAllLists()

    elif cmd == '-d' or cmd == '--delete':  # Delete list
        actions.removeList(get.getFileLocation(2))

    elif cmd == '-da' or cmd == '--date':  # Add date to task
        actions.addDate(get.getFileLocation(2), get.getTask(3), get.getDate(4))

    elif cmd == '-e' or cmd == '--edit':  # Edit list name
        actions.ListNameEdit(get.getFileLocation(2), get.getNewName(3))

    elif cmd == '-i' or cmd == '--insert':  # Insert task
        actions.insert(get.getFileLocation(2), get.getTask(3), get.getuInt(4))

    elif cmd == '-cll' or cmd == '--change-list-list':
        actions.changeListListPath(get.getFileLocation(2))

    elif cmd == '-cl' or cmd == '--change-list':
        actions.changeListPath(get.getFileLocation(2), get.getFileLocation(3))

    elif cmd == '-b' or cmd == '--backup':
        actions.backup(get.getFileLocation(2), get.getFileLocation(3))

    elif cmd == '-rb' or cmd == '--restore-backup':
        actions.restoreBackup(get.getFileLocation(2), get.getFileLocation(3))


main()
