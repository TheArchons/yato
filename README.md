# yato
yato - Yet another Todo app, a cli program for TODO lists

![https://i.imgur.com/zqr15Za.png](https://i.imgur.com/zqr15Za.png)

# Installation

## From pip
To install from pip, run `pip install yato` with pip installed

## From source
To build from source, clone the repository and run `pip install .` in the yato directory

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

Run `yato` and add arguments to the command line

For example, to create a new TODO list, run `yato -n`

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
| `-b` or `--backup` | backup the TODO list
| `-rb` or `--restore-backup` | restore a backup of a TODO list
| `-sd` or `--set-default` | set the default TODO list

To select the previous TODO list, replace the list location with `-p`. \
To select the default TODO list, replace the list location with `-d`.

# Dependencies
If you're installing from pip, these are automatically installed. \
1.termcolor
