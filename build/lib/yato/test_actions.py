"""pytest tests for actions.py"""

import pytest
import json
import yato.actions as actions
from JSONManip import getFile as getFile
import os
from pathlib import Path
from shutil import rmtree


def remove():
    """Remove all files created by the tests"""

    removeFiles = [
        'config.ini',
        'lists.json',
        'test.json',
        'test2.json',
        'asd.txt',
        '111.json',
        'testMoved.json',
        'testBackup.json',
        str(Path.home()) + os.path.sep + 'lists.json',
        str(Path.home()) + os.path.sep + 'testMoved.json'
    ]
    removePaths = [
        'listOfLists',
        'lists',
    ]

    # remove json files incase they exist
    for file in removeFiles:
        if os.path.exists(file):
            os.remove(file)

    # remove directories incase they exist
    for path in removePaths:
        if os.path.exists(path):
            rmtree(path)


@pytest.fixture(autouse=True)
def setup_teardown():
    """Automatic setup and teardown of tests"""

    # setup
    remove()

    actions.createConfig()
    actions.createListList()

    yield  # runs tests

    # teardown
    remove()


def test_ListNameEdit():
    """Test ListNameEdit"""

    open('test.json', 'w').close()

    actions.ListNameEdit('test.json', 'test2.json')
    assert os.path.exists('test2.json')
    assert ('test2.json' in json.loads(open('lists.json').read())['lists'])
    assert not ('test.json' in json.loads(open('lists.json').read())['lists'])

    actions.ListNameEdit('test2.json', 'test2.json')
    assert os.path.exists('test2.json')
    assert ('test2.json' in json.loads(open('lists.json').read())['lists'])

    actions.ListNameEdit('test2.json', 'asd.txt')
    assert os.path.exists('asd.txt')
    assert ('asd.txt' in json.loads(open('lists.json').read())['lists'])
    assert not ('test2.json' in json.loads(open('lists.json').read())['lists'])

    actions.ListNameEdit('asd.txt', 'asd.txt')
    assert os.path.exists('asd.txt')
    assert ('asd.txt' in json.loads(open('lists.json').read())['lists'])

    actions.ListNameEdit('asd.txt', '111.json')
    assert os.path.exists('111.json')
    assert ('111.json' in json.loads(open('lists.json').read())['lists'])
    assert not ('asd.txt' in json.loads(open('lists.json').read())['lists'])

    actions.ListNameEdit('111.json', 'test.json')
    assert os.path.exists('test.json')
    assert ('test.json' in json.loads(open('lists.json').read())['lists'])
    assert not ('111.json' in json.loads(open('lists.json').read())['lists'])


def test_insert():
    """Test insert"""

    actions.new('test.json')
    actions.insert('test.json', 'task', 1)
    assert json.loads(open('test.json').read())['tasks'][0] == ['task', 1]

    actions.insert('test.json', 'task2', 2)

    assert json.loads(open('test.json').read())['tasks'][1] == ['task2', 2]

    actions.insert('test.json', 'task1', 2)

    assert (json.loads(open('test.json').read())['tasks'][0] == ['task', 1])
    assert (json.loads(open('test.json').read())['tasks'][1] == ['task1', 2])
    assert (json.loads(open('test.json').read())['tasks'][2] == ['task2', 3])

    temp = json.loads(open('test.json').read())['tasks']

    actions.insert('test.json', 'task3', 5)
    # should not change the list
    assert json.loads(open('test.json').read())['tasks'] == temp


def test_changeListListPath():
    """test changeListListPath"""

    sep = os.path.sep  # separator for the operating system

    # Create 2 lists
    actions.new('test.json')
    actions.new('test2.json')

    # add tasks to lists
    actions.addToList('test.json', 'task')
    actions.addToList('test2.json', 'task2')

    # change path of listList
    actions.changeListListPath('listList' + sep + 'listOfLists.json')
    # check if file exists
    assert(os.path.exists('listList' + sep + 'listOfLists.json'))
    # check if file was deleted
    assert(not os.path.exists('lists.json'))

    # check if the lists file's contents remain the same
    file = json.loads(open('listList' + sep + 'listOfLists.json').read())
    file = file['lists']
    assert('test.json' in file)
    assert('test2.json' in file)

    # move the lists file to home directory
    path = str(Path.home()) + os.path.sep + 'lists.json'
    # os.path.sep is the path separator, usually ' + sep + ' or \
    actions.changeListListPath(path)
    # check if file exists
    assert(os.path.exists(path))
    # check if file was deleted
    assert(not os.path.exists('listList' + sep + 'listOfLists.json'))

    # check if the lists file's contents remain the same
    assert('test.json' in json.loads(open(path).read())['lists'])
    assert('test2.json' in json.loads(open(path).read())['lists'])


def test_createConfig():
    """Test createConfig"""

    # check if config file exists
    assert os.path.exists('config.ini')
    # read config file
    temp = open('config.ini').read()
    # create config file (should not change the file)
    actions.createConfig()
    # check if config file contents remain the same
    assert temp == open('config.ini').read()


def test_changeListPath():
    """Test changeListPath"""

    # create list
    actions.new('test.json')

    # add task to lists
    actions.addToList('test.json', 'task')

    # move and assert
    # save test.json as a variable
    temp = json.loads(open('test.json').read())
    # change path of list
    actions.changeListPath('test.json', 'testMoved.json')
    # assert
    assert os.path.exists('testMoved.json')\
        and not os.path.exists('test.json')\
        and json.loads(open('testMoved.json').read()) == temp

    # move to folder lists and assert
    # save list as variable
    temp = json.loads(open('testMoved.json').read())
    # change path of list
    path = 'lists' + os.path.sep + 'testMoved.json'
    actions.changeListPath('testMoved.json', path)
    # assert
    assert os.path.exists(path)\
        and not os.path.exists('testMoved.json')\
        and json.loads(open(path).read()) == temp

    # move to root directory and assert
    # save list as variable
    temp = json.loads(open('lists' + os.path.sep + 'testMoved.json').read())
    # change path of list
    prevPath = path
    path = str(Path.home()) + os.path.sep + 'testMoved.json'
    actions.changeListPath(prevPath, path)
    # assert
    assert os.path.exists(path)\
        and not os.path.exists(prevPath)\
        and json.loads(open(path).read()) == temp


def test_checkTaskExists():
    """Test checkTaskExists"""

    # create list
    actions.new('test.json')

    # add task to lists
    actions.addToList('test.json', 'task')

    # check if task exists
    assert actions.checkTaskExists('test.json', 'task')
    # check if task does not exist
    assert not actions.checkTaskExists('test.json', 'task2')
    # check if list does not exist
    assert not actions.checkTaskExists('test.json', 'task312')
    # check if list does not exist
    assert not actions.checkTaskExists('test.json', 'task22')


def test_addToList():
    """Test addToList"""

    # create list
    actions.new('test.json')

    # add task to test.json
    actions.addToList('test.json', 'task')

    # check if task exists
    assert actions.checkTaskExists('test.json', 'task')

    # add same task to test.json
    actions.addToList('test.json', 'task')

    # check if only one task exists
    file = getFile('test.json')
    assert len(file['tasks']) == 1
    assert file['tasks'][0] == ['task', 1]

    # add different task to test.json
    actions.addToList('test.json', 'task2')
    # check if two tasks exist
    file = getFile('test.json')
    assert len(file['tasks']) == 2
    assert file['tasks'][0] == ['task', 1]
    assert file['tasks'][1] == ['task2', 2]


def test_backup():
    """Test backup"""

    actions.new('test.json')
    actions.addToList('test.json', 'task')
    actions.backup('test.json', 'testBackup.json')

    assert os.path.exists('testBackup.json')
    testBackup = json.loads(open('testBackup.json').read())
    test = json.loads(open('test.json').read())
    assert test == testBackup

    os.remove('test.json')

    assert not os.path.exists('test.json')
    assert os.path.exists('testBackup.json')


def test_restoreBackup():
    """Test restoreBackup"""

    actions.new('test.json')
    actions.addToList('test.json', 'task')

    actions.backup('test.json', 'testBackup.json')

    testFile = json.loads(open('test.json').read())

    os.remove('test.json')

    actions.restoreBackup('testBackup.json', 'test.json')

    assert os.path.exists('test.json')

    restoredFile = json.loads(open('test.json').read())

    assert testFile == restoredFile
