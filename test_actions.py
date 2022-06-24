import pytest
import json
from actions import createListList, ListNameEdit,\
    insert, changeListListPath, createConfig, new, addToList
import os
from pathlib import Path


@pytest.fixture(autouse=True)
def setup_teardown():
    # setup
    if os.path.exists('config.ini'):
        os.remove('config.ini')
    createConfig()
    if os.path.exists('lists.json'):
        os.remove('lists.json')
    createListList()

    # remove json files incase they exist
    if os.path.exists('test.json'):
        os.remove('test.json')

    if os.path.exists('test2.json'):
        os.remove('test2.json')

    if os.path.exists('asd.txt'):
        os.remove('asd.txt')

    if os.path.exists('111.json'):
        os.remove('111.json')

    if os.path.exists(str(Path.home()) + os.path.sep + 'lists.json'):
        os.remove(str(Path.home()) + os.path.sep + 'lists.json')

    yield  # runs tests

    # teardown
    if os.path.exists('test.json'):
        open('test.json', 'w').close()
        os.remove('test.json')

    if os.path.exists('test2.json'):
        open('test2.json', 'w').close()
        os.remove('test2.json')

    if os.path.exists('asd.txt'):
        open('asd.txt', 'w').close()
        os.remove('asd.txt')

    if os.path.exists('111.json'):
        open('111.json', 'w').close()
        os.remove('111.json')

    if os.path.exists('lists.json'):
        open('lists.json', 'w').close()
        os.remove('lists.json')

    if os.path.exists('config.ini'):
        open('config.ini', 'w').close()
        os.remove('config.ini')

    if os.path.exists('listOfLists'):
        open('listOfLists', 'w').close()
        os.rmdir('listOfLists')

    if os.path.exists('test.txt'):
        open('test.txt', 'w').close()
        os.remove('test.txt')


def test_ListNameEdit():
    open('test.json', 'w').close()

    ListNameEdit('test.json', 'test2.json')
    assert os.path.exists('test2.json')
    assert ('test2.json' in json.loads(open('lists.json').read())['lists'])
    assert not ('test.json' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('test2.json', 'test2.json')
    assert os.path.exists('test2.json')
    assert ('test2.json' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('test2.json', 'asd.txt')
    assert os.path.exists('asd.txt')
    assert ('asd.txt' in json.loads(open('lists.json').read())['lists'])
    assert not ('test2.json' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('asd.txt', 'asd.txt')
    assert os.path.exists('asd.txt')
    assert ('asd.txt' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('asd.txt', '111.json')
    assert os.path.exists('111.json')
    assert ('111.json' in json.loads(open('lists.json').read())['lists'])
    assert not ('asd.txt' in json.loads(open('lists.json').read())['lists'])

    ListNameEdit('111.json', 'test.json')
    assert os.path.exists('test.json')
    assert ('test.json' in json.loads(open('lists.json').read())['lists'])
    assert not ('111.json' in json.loads(open('lists.json').read())['lists'])


def test_insert():

    new('test.json')
    insert('test.json', 'task', 1)
    assert json.loads(open('test.json').read())['tasks'][0] == ['task', 1]

    insert('test.json', 'task2', 2)

    assert json.loads(open('test.json').read())['tasks'][1] == ['task2', 2]

    insert('test.json', 'task1', 2)

    assert (json.loads(open('test.json').read())['tasks'][0] == ['task', 1])
    assert (json.loads(open('test.json').read())['tasks'][1] == ['task1', 2])
    assert (json.loads(open('test.json').read())['tasks'][2] == ['task2', 3])

    temp = json.loads(open('test.json').read())['tasks']

    insert('test.json', 'task3', 5)
    # should not change the list
    assert json.loads(open('test.json').read())['tasks'] == temp


def test_changeListListPath():
    sep = os.path.sep

    # Create 2 lists
    new('test.json')
    new('test2.json')

    # add tasks to lists
    addToList('test.json', 'task')
    addToList('test2.json', 'task2')

    # change path of listList
    changeListListPath('listList' + sep + 'listOfLists.json')
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
    changeListListPath(path)
    # check if file exists
    assert(os.path.exists(path))
    # check if file was deleted
    assert(not os.path.exists('listList' + sep + 'listOfLists.json'))

    # check if the lists file's contents remain the same
    assert('test.json' in json.loads(open(path).read())['lists'])
    assert('test2.json' in json.loads(open(path).read())['lists'])


def test_createConfig():
    # check if config file exists
    assert os.path.exists('config.ini')
    # read config file
    temp = open('config.ini').read()
    # create config file (should not change the file)
    createConfig()
    # check if config file contents remain the same
    assert temp == open('config.ini').read()
