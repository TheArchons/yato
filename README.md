# yato
yato - Yet another Todo app, a cli program for TODO lists

# Dependencies
Use `pip install -r requirements.txt` in the yato directory

# Installation
I will add this to pip in the future. For now, \
1. clone the source code
2. run `pip install -r requirements.txt`
3. run `python yato.py` to start the app

# Usage

<!---
    -h or --help:       show this help\
    -n or --new:        create a new TODO list\
    -a or --add:        add a task to a TODO list\
    -c or --complete:   complete a task\
    -r or --remove:     remove a task\
    -l or --list:       list all tasks\
    -ll or --list-all:  list all TODO lists\
    -d or --delete:     delete a TODO list\
    -da or --date:      add a date to a task\
    -e or --edit:       edit a TODO list's name\
    -i or --insert:     insert a task into a TODO list\
    -cll or --change-list-list:     change the location of the list of lists file
-->

Run `python yato.py` and add arguments to the command line

For example, to create a new TODO list, run `python yato.py -n`

# Supported arguments

| Command | Description |
| ------- | ----------- |
| `-h` or `--help` | list these commands
| `-n` or `--new` | create a new TODO list
| `-a` or `--add` | add a task to a TODO list
| `-c` or `--complete` | complete a task
| `-r` or `--remove` | remove a task
| `-l` or `--list` | list all tasks
| `-ll` or `--list-all` | list all TODO lists
| `-d` or `--delete` | delete a TODO list
| `-da` or `--date` | add a date to a task
| `-e` or `--edit` | edit a TODO list's name
| `-i` or `--insert` | insert a task into a TODO list
| `-cll` or `--change-list-list` | change the location of the list of lists file